"""
convert_events.py — Batch-convert UIL event PDFs to Markdown.

Converts all configured events, routing math-heavy ones through the
marker backend and the rest through the default docling backend.
Output .md files land in an md/ subfolder inside each event folder.

Excluded events (no conversion):
    Accounting, Computer Applications, Literary Criticism,
    Current Issues & Events

    Mathematics is excluded here because it has its own convert_all.py.

Usage:
    python convert_events.py
    python convert_events.py --dry-run
    python convert_events.py --no-verify-ssl
    python convert_events.py --event "Number Sense"   # single event
"""

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent   # UIL/
OCR  = HERE / "pdf_ocr.py"

# Only convert PDFs inside these year subfolders.
# Modify as needed, e.g. YEARS = {2024, 2025} or YEARS = None to convert all years.
YEARS = {2023, 2024, 2025, 2026}

# Events that need the marker backend (math-heavy)
MARKER_EVENTS = {
    "Calculator Applications",
    "Computer Science Written",
    "Number Sense",
    "Science",
}

# Events to convert with the default (docling) backend
DOCLING_EVENTS = {
    "Computer Science",
    "Copy Editing",
    "Editorial Writing",
    "Feature Writing",
    "Headline Writing",
    "News Writing",
    "Ready Writing",
    "Social Studies",
    "Spelling & Vocabulary",
}

# First content page for events that have cover pages to skip.
# Value is passed as "--pages N-999" (999 is effectively "to end of document").
# Events not listed here are converted in full (no --pages flag).
START_PAGE = {
    "Calculator Applications":  2,
    "Computer Science Written": 4,
    "Copy Editing":             3,
    "Science":                  2,
    "Social Studies":           2,
    "Spelling & Vocabulary":    2,
}

ALL_EVENTS = MARKER_EVENTS | DOCLING_EVENTS


def convert_event(event: str, dry_run: bool, no_verify_ssl: bool) -> tuple[int, int, int]:
    """Convert all PDFs for a single event. Returns (ok, skipped, failed)."""
    event_dir = HERE / event
    out_dir   = event_dir / "md"

    if not event_dir.is_dir():
        print(f"  [WARN] Directory not found, skipping: {event_dir}")
        return 0, 0, 0

    out_dir.mkdir(exist_ok=True)

    use_marker = event in MARKER_EVENTS
    backend_label = "marker" if use_marker else "docling"

    all_pdfs = sorted(event_dir.rglob("*.pdf"))

    # Filter by YEARS if set (match against the immediate parent folder name)
    if YEARS is not None:
        pdfs = [p for p in all_pdfs if p.parent.name.isdigit() and int(p.parent.name) in YEARS]
    else:
        pdfs = all_pdfs

    if not pdfs:
        print(f"  [WARN] No PDFs found under {event_dir} for years {YEARS}")
        return 0, 0, 0

    total = len(pdfs)
    year_label = f"years={sorted(YEARS)}" if YEARS else "all years"
    print(f"\n{'='*60}")
    print(f"  {event}  ({total} PDF(s), backend={backend_label}, {year_label})")
    print(f"  Output → {out_dir}")
    print(f"{'='*60}")

    ok = skip = fail = 0
    for i, pdf in enumerate(pdfs, 1):
        out = out_dir / pdf.with_suffix(".md").name

        if out.exists():
            print(f"  [{i:3}/{total}] -- {pdf.name}  (already exists, skipping)")
            skip += 1
            continue

        cmd = [sys.executable, str(OCR), str(pdf), "-o", str(out)]
        if use_marker:
            cmd += ["--backend", "marker"]
        if event in START_PAGE:
            cmd += ["--pages", f"{START_PAGE[event]}-999"]
        if no_verify_ssl:
            cmd.append("--no-verify-ssl")

        print(f"  [{i:3}/{total}] >> {pdf.name}")
        if dry_run:
            print(f"           {' '.join(cmd)}\n")
            ok += 1
            continue

        result = subprocess.run(cmd)
        if result.returncode == 0:
            print(f"           -> {out.name}\n")
            ok += 1
        else:
            print(f"           FAILED (exit {result.returncode})\n")
            fail += 1

    return ok, skip, fail


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print commands without running them")
    parser.add_argument("--no-verify-ssl", action="store_true",
                        help="Pass --no-verify-ssl to pdf_ocr.py")
    parser.add_argument("--event", metavar="NAME",
                        help="Convert only this event (exact folder name)")
    args = parser.parse_args()

    if not OCR.exists():
        sys.exit(f"pdf_ocr.py not found at {OCR}")

    if args.event:
        if args.event not in ALL_EVENTS:
            sys.exit(
                f"Unknown event: '{args.event}'\n"
                f"Valid events: {sorted(ALL_EVENTS)}"
            )
        events = [args.event]
    else:
        events = sorted(ALL_EVENTS)

    print(f"UIL Event Converter")
    print(f"Dry run: {args.dry_run}")
    print(f"Events : {len(events)}")

    total_ok = total_skip = total_fail = 0
    for event in events:
        ok, skip, fail = convert_event(event, args.dry_run, args.no_verify_ssl)
        total_ok   += ok
        total_skip += skip
        total_fail += fail

    print(f"\n{'='*60}")
    print(f"  All done.")
    print(f"  Converted : {total_ok}")
    print(f"  Skipped   : {total_skip}  (already existed)")
    print(f"  Failed    : {total_fail}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
