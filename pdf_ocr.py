"""
pdf_ocr.py — PDF → Markdown + LaTeX

Two backends, selectable with --backend:

  docling (default)
      IBM Docling layout-aware pipeline. Good general-purpose choice: handles
      multi-column layouts, tables, figures, and formula regions. Works well on
      all UIL events. Use --no-ocr for digitally-created PDFs (faster).

  marker
      Marker-PDF pipeline, trained on academic PDFs. Produces cleaner LaTeX for
      math-dense events (Mathematics, Calculator Applications, Number Sense,
      Science). Slower on first run (downloads ~1 GB of models once).

Usage:
    python pdf_ocr.py input.pdf
    python pdf_ocr.py input.pdf --backend marker
    python pdf_ocr.py input.pdf -o output.md
    python pdf_ocr.py input.pdf --pages 1-5
    python pdf_ocr.py input.pdf --pages 1,3,7-10
    python pdf_ocr.py input.pdf --no-ocr          # docling only; skip OCR step
    python pdf_ocr.py input.pdf --rotate 90        # rotate pages before OCR
    python pdf_ocr.py input.pdf --rasterize        # render to PNG first (docling only)
    python pdf_ocr.py input.pdf --rasterize --dpi 400

Requirements:
    pip install docling pypdf pymupdf   # docling backend
    pip install marker-pdf             # marker backend
"""

import argparse
import sys
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# SSL helper — must run before any network-touching imports
# ---------------------------------------------------------------------------

def disable_ssl_verification() -> None:
    """
    Suppress SSL certificate checks across every HTTP layer Python uses.
    Required on networks where a corporate proxy re-signs TLS traffic with
    an internal CA that Python does not trust.
    """
    import os, ssl, warnings

    os.environ["REQUESTS_CA_BUNDLE"]              = ""
    os.environ["CURL_CA_BUNDLE"]                  = ""
    os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"
    os.environ["PYTHONHTTPSVERIFY"]               = "0"

    ssl._create_default_https_context = ssl._create_unverified_context

    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except ImportError:
        pass

    try:
        import requests
        _orig_request = requests.Session.request
        def _patched_request(self, method, url, **kwargs):
            kwargs["verify"] = False
            return _orig_request(self, method, url, **kwargs)
        requests.Session.request = _patched_request
    except ImportError:
        pass

    try:
        import httpx
        _orig_client = httpx.Client.__init__
        def _patched_client(self, *args, **kwargs):
            kwargs["verify"] = False
            _orig_client(self, *args, **kwargs)
        httpx.Client.__init__ = _patched_client

        _orig_async = httpx.AsyncClient.__init__
        def _patched_async(self, *args, **kwargs):
            kwargs["verify"] = False
            _orig_async(self, *args, **kwargs)
        httpx.AsyncClient.__init__ = _patched_async
    except ImportError:
        pass

    warnings.filterwarnings("ignore", message="Unverified HTTPS request")


# ---------------------------------------------------------------------------
# Page selection / preprocessing helpers
# ---------------------------------------------------------------------------

def parse_page_range(spec: str, total_pages: int) -> list:
    """
    Convert a page-range string to a sorted list of 1-based page numbers.
        "3"        → [3]
        "1-5"      → [1, 2, 3, 4, 5]
        "1,3,5"    → [1, 3, 5]
        "1-3,7-9"  → [1, 2, 3, 7, 8, 9]
    """
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            pages.update(range(int(lo), int(hi) + 1))
        else:
            pages.add(int(part))
    valid = sorted(p for p in pages if 1 <= p <= total_pages)
    if not valid:
        sys.exit(f"No valid pages in '{spec}' for a {total_pages}-page document.")
    return valid


def get_total_pages(pdf: Path) -> int:
    try:
        import pypdf
        with open(str(pdf), "rb") as fh:
            return len(pypdf.PdfReader(fh).pages)
    except ImportError:
        sys.exit("pypdf is required for page selection.\nInstall with: pip install pypdf")


def preprocess_pdf(src: Path, page_numbers: list | None, rotate: int) -> Path:
    """
    Write a preprocessed copy of the PDF (page selection + rotation) to a
    temp file. Returns the temp Path — caller is responsible for unlinking.
    """
    try:
        import pypdf
    except ImportError:
        sys.exit("pypdf is required for page selection / rotation.\nInstall with: pip install pypdf")

    writer = pypdf.PdfWriter()
    with open(str(src), "rb") as fh:
        reader = pypdf.PdfReader(fh)
        pages_to_use = (
            [reader.pages[p - 1] for p in page_numbers]
            if page_numbers
            else list(reader.pages)
        )
        for page in pages_to_use:
            if rotate:
                page = page.rotate(rotate)
            writer.add_page(page)

    tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    writer.write(tmp)
    tmp.close()
    return Path(tmp.name)


# ---------------------------------------------------------------------------
# Rasterization (PDF → PNG via PyMuPDF) — used by docling backend
# ---------------------------------------------------------------------------

def rasterize_to_images(src: Path, page_nums: list | None, rotate: int, dpi: int) -> list:
    """
    Render each selected page to a temp PNG. Returns list of temp Paths.
    """
    try:
        import fitz  # pymupdf
    except ImportError:
        sys.exit("pymupdf is required for rasterization.\nInstall with: pip install pymupdf")

    doc     = fitz.open(str(src))
    scale   = dpi / 72
    mat     = fitz.Matrix(scale, scale)
    if rotate:
        mat = mat.prerotate(rotate)

    indices   = [p - 1 for p in page_nums] if page_nums else range(len(doc))
    tmp_paths = []
    for i, page_idx in enumerate(indices):
        page = doc[page_idx]
        pix  = page.get_pixmap(matrix=mat, alpha=False)
        tmp  = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        pix.save(tmp.name)
        tmp.close()
        tmp_paths.append(Path(tmp.name))
        print(f"  Rasterized page {page_idx + 1} → {dpi} DPI PNG ({i+1}/{len(indices)})")

    doc.close()
    return tmp_paths


# ---------------------------------------------------------------------------
# Docling backend
# ---------------------------------------------------------------------------

def run_docling(
    pdf_path: str,
    output_path: str,
    pages_spec: str | None,
    no_ocr: bool,
    rotate: int,
    rasterize: bool,
    dpi: int,
) -> None:
    try:
        from docling.document_converter import DocumentConverter, PdfFormatOption
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
    except ImportError as exc:
        sys.exit(f"Missing dependency: {exc}\nInstall with: pip install docling")

    pdf = Path(pdf_path)
    if not pdf.exists():
        sys.exit(f"File not found: {pdf_path}")

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr             = not no_ocr
    pipeline_options.do_table_structure = True
    if hasattr(pipeline_options, "do_formula_enrichment"):
        pipeline_options.do_formula_enrichment = True

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )

    page_nums = None
    if pages_spec:
        page_nums = parse_page_range(pages_spec, get_total_pages(pdf))

    if rasterize:
        print(f"Rasterizing {pdf.name} at {dpi} DPI...")
        tmp_pngs = rasterize_to_images(pdf, page_nums, rotate, dpi)
        sections = []
        try:
            for i, png in enumerate(tmp_pngs):
                print(f"  OCR page {i + 1}/{len(tmp_pngs)}...")
                res = converter.convert(str(png))
                if res and res.document:
                    sections.append(res.document.export_to_markdown())
        finally:
            for p in tmp_pngs:
                if p.exists():
                    p.unlink()
        markdown = "\n\n---\n\n".join(sections)
    else:
        src      = pdf
        tmp_file = None
        if pages_spec or rotate:
            desc_parts = []
            if page_nums:
                desc_parts.append(f"pages {page_nums}")
            if rotate:
                desc_parts.append(f"rotated {rotate}deg")
            print(f"Preprocessing {pdf.name}: {', '.join(desc_parts)}...")
            src      = preprocess_pdf(pdf, page_nums, rotate)
            tmp_file = src

        print(f"Converting {pdf.name} (docling)...")
        try:
            result = converter.convert(str(src))
        finally:
            if tmp_file and tmp_file.exists():
                tmp_file.unlink()

        if result is None or result.document is None:
            sys.exit("Conversion failed — Docling returned no output.")
        markdown = result.document.export_to_markdown()

    _write_output(markdown, output_path)


# ---------------------------------------------------------------------------
# Marker backend
# ---------------------------------------------------------------------------

def run_marker(
    pdf_path: str,
    output_path: str,
    pages_spec: str | None,
    rotate: int,
) -> None:
    """
    Convert using marker-pdf. Better LaTeX quality on math-dense PDFs.
    Models (~1 GB) are downloaded to ~/.cache/huggingface on first run.

    Note: --no-ocr and --rasterize are docling-specific flags and are ignored
    here; marker handles OCR internally. --rotate still works via pypdf
    preprocessing when needed.
    """
    try:
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered
        from marker.config.parser import ConfigParser
    except ImportError:
        sys.exit(
            "marker-pdf is not installed.\n"
            "Install with: pip install marker-pdf"
        )

    pdf = Path(pdf_path)
    if not pdf.exists():
        sys.exit(f"File not found: {pdf_path}")

    # Apply page selection / rotation via pypdf preprocessing if needed.
    src      = pdf
    tmp_file = None
    if pages_spec or rotate:
        page_nums = parse_page_range(pages_spec, get_total_pages(pdf)) if pages_spec else None
        desc_parts = []
        if page_nums:
            desc_parts.append(f"pages {page_nums}")
        if rotate:
            desc_parts.append(f"rotated {rotate}deg")
        print(f"Preprocessing {pdf.name}: {', '.join(desc_parts)}...")
        src      = preprocess_pdf(pdf, page_nums, rotate)
        tmp_file = src

    print(f"Converting {pdf.name} (marker)...")
    try:
        config_parser = ConfigParser({"output_format": "markdown"})
        converter = PdfConverter(
            config          = config_parser.generate_config_dict(),
            artifact_dict   = create_model_dict(),
            processor_list  = config_parser.get_processors(),
            renderer        = config_parser.get_renderer(),
        )
        rendered = converter(str(src))
        markdown, _, _ = text_from_rendered(rendered)
    finally:
        if tmp_file and tmp_file.exists():
            tmp_file.unlink()

    _write_output(markdown, output_path)


# ---------------------------------------------------------------------------
# Shared output helper
# ---------------------------------------------------------------------------

def _write_output(markdown: str, output_path: str) -> None:
    out = Path(output_path)
    out.write_text(markdown, encoding="utf-8")
    print(f"Done. Output → {out}\n  Characters : {len(markdown):,}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a PDF to Markdown + LaTeX. "
            "Choose --backend docling (default, general-purpose) or "
            "--backend marker (better LaTeX for math-heavy events)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output",
        help="Output .md path (default: input filename with .md extension)",
    )
    parser.add_argument(
        "--backend",
        choices=["docling", "marker"],
        default="docling",
        help="Conversion backend (default: docling). Use marker for math-heavy PDFs.",
    )
    parser.add_argument(
        "--pages",
        metavar="RANGE",
        help="Pages to process, e.g. '1-5' or '1,3,7-10' (default: all)",
    )
    parser.add_argument(
        "--no-ocr",
        action="store_true",
        help=(
            "[docling only] Skip OCR. Use for digitally-created PDFs where text "
            "is already selectable. Much faster, but won't work on scanned pages."
        ),
    )
    parser.add_argument(
        "--rotate",
        type=int,
        choices=[90, 180, 270],
        default=0,
        metavar="DEG",
        help="Rotate every page before processing: 90, 180, or 270 degrees clockwise.",
    )
    parser.add_argument(
        "--rasterize",
        action="store_true",
        help=(
            "[docling only] Render each page to a PNG first, then OCR the image. "
            "Useful when the embedded PDF content is too poor quality to read directly."
        ),
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        metavar="N",
        help="[docling only] Resolution for --rasterize (default: 300).",
    )
    parser.add_argument(
        "--no-verify-ssl",
        action="store_true",
        help=(
            "Disable SSL certificate verification. Use on networks with a "
            "corporate proxy that intercepts TLS (e.g. district-managed machines)."
        ),
    )

    args = parser.parse_args()

    # Must happen before any network-touching imports (docling, marker, HF Hub).
    if args.no_verify_ssl:
        disable_ssl_verification()

    output = args.output or str(Path(args.input_pdf).with_suffix(".md"))

    if args.backend == "marker":
        if args.no_ocr:
            print("Note: --no-ocr is a docling flag and is ignored with --backend marker.")
        if args.rasterize:
            print("Note: --rasterize is a docling flag and is ignored with --backend marker.")
        run_marker(
            pdf_path    = args.input_pdf,
            output_path = output,
            pages_spec  = args.pages,
            rotate      = args.rotate,
        )
    else:
        run_docling(
            pdf_path    = args.input_pdf,
            output_path = output,
            pages_spec  = args.pages,
            no_ocr      = args.no_ocr,
            rotate      = args.rotate,
            rasterize   = args.rasterize,
            dpi         = args.dpi,
        )


if __name__ == "__main__":
    main()
