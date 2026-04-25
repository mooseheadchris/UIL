"""
pdf_ocr.py — PDF → Markdown + LaTeX using IBM Docling

Extracts text and mathematical equations from PDFs, outputting clean Markdown
with equations in LaTeX notation. Uses Docling's layout-aware pipeline which
handles columns, tables, figures, and formula regions correctly.

Usage:
    python pdf_ocr.py input.pdf
    python pdf_ocr.py input.pdf -o output.md
    python pdf_ocr.py input.pdf --pages 1-5
    python pdf_ocr.py input.pdf --pages 1,3,7-10
    python pdf_ocr.py input.pdf --no-ocr         # text-based PDFs, skips OCR
    python pdf_ocr.py input.pdf --rotate 90       # rotate pages before OCR
    python pdf_ocr.py input.pdf --rasterize       # render to PNG first, then OCR
    python pdf_ocr.py input.pdf --rasterize --dpi 400  # higher DPI for poor scans

Requirements:
    pip install docling pypdf pymupdf

Apple Silicon note:
    Docling's PyTorch models use MPS automatically on M-series Macs.
    No extra configuration needed — it is detected at runtime.
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
    Aggressively suppress SSL certificate checks across every HTTP layer
    Python uses.  Required on networks where a corporate proxy re-signs
    TLS traffic with an internal CA that Python does not trust.
    """
    import os, ssl, warnings

    # --- Environment variables (picked up by new sessions) ------------------
    os.environ["REQUESTS_CA_BUNDLE"]              = ""
    os.environ["CURL_CA_BUNDLE"]                  = ""
    os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"
    os.environ["PYTHONHTTPSVERIFY"]               = "0"

    # --- stdlib ssl / urllib ------------------------------------------------
    ssl._create_default_https_context = ssl._create_unverified_context

    # --- urllib3 ------------------------------------------------------------
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except ImportError:
        pass

    # --- requests: patch Session so verify=False is forced on every call ----
    try:
        import requests
        _orig_request = requests.Session.request
        def _patched_request(self, method, url, **kwargs):
            kwargs["verify"] = False
            return _orig_request(self, method, url, **kwargs)
        requests.Session.request = _patched_request
    except ImportError:
        pass

    # --- httpx (used by some Docling / HF Hub versions) ---------------------
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

    # Suppress the resulting InsecureRequestWarning noise
    warnings.filterwarnings("ignore", message="Unverified HTTPS request")


# ---------------------------------------------------------------------------
# Page selection helpers
# ---------------------------------------------------------------------------

def parse_page_range(spec: str, total_pages: int) -> list:
    """
    Convert a page-range string to a sorted list of 1-based page numbers.

    Examples:
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
        sys.exit(
            f"No valid pages in '{spec}' for a {total_pages}-page document."
        )
    return valid


def preprocess_pdf(src: Path, page_numbers: list | None, rotate: int) -> Path:
    """
    Write a pre-processed copy of the PDF to a temp file, applying optional
    page selection and/or rotation.  Returns the temp Path — caller must unlink.
    """
    try:
        import pypdf
    except ImportError:
        sys.exit(
            "pypdf is required for page selection / rotation.\n"
            "Install with: pip install pypdf"
        )

    writer = pypdf.PdfWriter()
    with open(str(src), "rb") as fh:
        reader   = pypdf.PdfReader(fh)
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
# Rasterization (PDF → PNG via PyMuPDF)
# ---------------------------------------------------------------------------

def rasterize_to_images(src: Path, page_nums: list | None, rotate: int, dpi: int) -> list:
    """
    Render each selected page of src to a temp PNG at the given DPI.
    Rotation is applied in the render matrix (no separate pypdf step needed).
    Returns a list of temp PNG Paths — caller must unlink them all.
    """
    try:
        import fitz  # pymupdf
    except ImportError:
        sys.exit(
            "pymupdf is required for rasterization.\n"
            "Install with: pip install pymupdf"
        )

    doc       = fitz.open(str(src))
    scale     = dpi / 72
    mat       = fitz.Matrix(scale, scale)
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
# Core conversion
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
        sys.exit(
            f"Missing dependency: {exc}\n"
            "Install with: pip install docling"
        )

    pdf = Path(pdf_path)
    if not pdf.exists():
        sys.exit(f"File not found: {pdf_path}")

    # --- Configure pipeline -------------------------------------------------
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr             = not no_ocr
    pipeline_options.do_table_structure = True

    # Formula enrichment converts detected equation regions to LaTeX.
    # Supported in Docling >= 2.x; silently ignored if not available.
    if hasattr(pipeline_options, "do_formula_enrichment"):
        pipeline_options.do_formula_enrichment = True

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    # --- Resolve page list if needed ----------------------------------------
    page_nums = None
    if pages_spec:
        try:
            import pypdf
            with open(str(pdf), "rb") as fh:
                total = len(pypdf.PdfReader(fh).pages)
        except ImportError:
            sys.exit(
                "pypdf is required for page selection.\n"
                "Install with: pip install pypdf"
            )
        page_nums = parse_page_range(pages_spec, total)

    # --- Rasterize path: PDF → PNG → Docling --------------------------------
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

    # --- Standard path: PDF → Docling (with optional page select/rotate) ----
    else:
        src      = pdf
        tmp_file = None

        if pages_spec or rotate:
            desc_parts = []
            if page_nums:
                desc_parts.append(f"pages {page_nums}")
            if rotate:
                desc_parts.append(f"rotated {rotate}°")
            print(f"Preprocessing {pdf.name}: {', '.join(desc_parts)}...")
            src      = preprocess_pdf(pdf, page_nums, rotate)
            tmp_file = src

        print(f"Converting {pdf.name}...")
        try:
            result = converter.convert(str(src))
        finally:
            if tmp_file and tmp_file.exists():
                tmp_file.unlink()

        if result is None or result.document is None:
            sys.exit("Conversion failed — Docling returned no output.")

        markdown = result.document.export_to_markdown()

    out = Path(output_path)
    out.write_text(markdown, encoding="utf-8")
    print(
        f"Done. Output → {out}\n"
        f"  Characters : {len(markdown):,}"
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert a PDF to Markdown + LaTeX using IBM Docling. "
            "Handles mixed text, tables, and mathematical equations."
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
        "--pages",
        metavar="RANGE",
        help="Pages to process, e.g. '1-5' or '1,3,7-10' (default: all)",
    )
    parser.add_argument(
        "--no-ocr",
        action="store_true",
        help=(
            "Skip the OCR step. Use for digitally-created PDFs where text is "
            "already selectable. Much faster, but won't work on scanned pages."
        ),
    )
    parser.add_argument(
        "--rotate",
        type=int,
        choices=[90, 180, 270],
        default=0,
        metavar="DEG",
        help="Rotate every page before OCR: 90, 180, or 270 degrees clockwise.",
    )
    parser.add_argument(
        "--rasterize",
        action="store_true",
        help=(
            "Render each page to a PNG first, then OCR the image. "
            "Useful when the embedded PDF content is too poor quality to read directly."
        ),
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        metavar="N",
        help="Resolution for --rasterize (default: 300). Try 400-600 for very poor scans.",
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

    # Must happen before docling / huggingface_hub are imported
    if args.no_verify_ssl:
        disable_ssl_verification()

    output = args.output or str(Path(args.input_pdf).with_suffix(".md"))

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
