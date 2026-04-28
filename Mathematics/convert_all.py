"""
convert_all.py — Batch-convert all Mathematics PDFs to Markdown via marker.

Finds every .pdf under this script's directory (all year subfolders),
runs pdf_ocr.py --backend marker on each one, and writes the .md files
to UIL/Mathematics/md/.

Usage:
    python convert_all.py
    python convert_all.py --dry-run
    python convert_all.py --no-verify-ssl
"""

import argparse
import subprocess
import sys
from pathlib import Path

HERE    = Path(__file__).parent          # UIL/Mathematics/
OCR     = HERE.parent / "pdf_ocr.py"    # UIL/pdf_ocr.py
OUT_DIR = HERE / "md"

SKIP = {
    "Math_Study_Material_A_2018.pdf",    # already converted
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print commands without running them")
    parser.add_argument("--no-verify-ssl", action="store_true", help="Pass --no-verify-ssl to pdf_ocr.py")
    args = parser.parse_args()

    if not OCR.exists():
        sys.exit(f"pdf_ocr.py not found at {OCR}")

    OUT_DIR.mkdir(exist_ok=True)

    pdfs = sorted(p for p in HERE.rglob("*.pdf") if p.name not in SKIP)

    if not pdfs:
        print("No PDFs found.")
        return

    total = len(pdfs)
    print(f"Found {total} PDF(s) to convert → {OUT_DIR}\n")

    ok = skip = fail = 0
    for i, pdf in enumerate(pdfs, 1):
        out = OUT_DIR / pdf.with_suffix(".md").name

        if out.exists():
            print(f"[{i:3}/{total}] -- {pdf.name}  (already exists, skipping)")
            skip += 1
            continue

        cmd = [sys.executable, str(OCR), str(pdf), "--backend", "marker", "-o", str(out)]
        if args.no_verify_ssl:
            cmd.append("--no-verify-ssl")

        print(f"[{i:3}/{total}] >> {pdf.name}")
        if args.dry_run:
            print(f"         {' '.join(cmd)}\n")
            ok += 1
            continue

        result = subprocess.run(cmd)
        if result.returncode == 0:
            print(f"         -> {out.name}\n")
            ok += 1
        else:
            print(f"         FAILED (exit {result.returncode})\n")
            fail += 1

    print(f"Done.  Converted: {ok}  Skipped: {skip}  Failed: {fail}")


if __name__ == "__main__":
    main()
