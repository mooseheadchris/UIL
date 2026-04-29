# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UIL academic competition study platform with two components:
1. **`/site`** — A Google Apps Script web app (SPA + backend) backed by a single Google Sheet
2. **Root Python utilities** — PDF batch downloaders and OCR converters for study materials

## Deploying the Apps Script App

**Manual (school computers without npm):** Copy all 9 `.gs` files, 10 HTML files, and `appsscript.json` into the Apps Script editor.

**Automated via clasp:**
```bash
npm install -g @google/clasp
clasp login
cp site/.clasp.json.example site/.clasp.json  # fill in scriptId
cd site && clasp push -f
```

After first deploy, run `setupSpreadsheet()` in the editor to initialize the 6 Sheet tabs and seed the teacher account. Then deploy via **Deploy → New deployment → Web app** (execute as owner, anyone can access).

**KaTeX bundle update:**
```bash
cd /tmp && npm pack katex@0.16.11
tar -xzf katex-0.16.11.tgz
node site/scripts/build-katex.js
```

## Python Utilities

```bash
# Download UIL PDFs from uiltexas.org (2018–2026)
python download_materials.py
python download_materials.py --dry-run

# Convert PDFs to Markdown (routes math-heavy events to marker backend)
python convert_events.py
python convert_events.py --event "Number Sense"
python convert_events.py --dry-run

# Single-file OCR conversion
python pdf_ocr.py input.pdf                    # docling backend (default)
python pdf_ocr.py input.pdf --backend marker   # math-heavy PDFs
python pdf_ocr.py input.pdf -o output.md --pages 1-5
```

Python dependencies: `docling`, `pypdf`, `pymupdf`, `marker-pdf`, `requests`

## Architecture

### Backend (Google Apps Script — V8 runtime, ECMAScript 5)

All server-side logic lives in `site/src/*.gs`. Entry points are in `Code.gs` (`doGet`, `doPost`). The RPC pattern is `google.script.run.<functionName>(args)` called from the browser.

| File | Responsibility |
|---|---|
| `Code.gs` | `doGet`/`doPost` entry points, HTML serving |
| `Auth.gs` | Salted SHA-256 passwords, HMAC-SHA256 signed JWTs (12h TTL) |
| `SheetDB.gs` | All sheet I/O with 30s `CacheService` cache and `LockService` write serialization |
| `Study.gs` | SM-2 spaced repetition algorithm, card scheduling |
| `Quiz.gs` | MCQ scoring and attempt storage |
| `Users.gs` | Roster management, CSV import |
| `Teacher.gs` | Admin endpoints (password reset, content upload, participation reports) |
| `Leaderboard.gs` | Score aggregation (5-minute cache) |

### Frontend (Vanilla JS SPA, no framework)

HTML partials in `site/src/html/`. Client-side router in `client.html`. Session stored as signed JWT in `localStorage`. Math rendered by the fully self-hosted KaTeX bundle (630KB, base64-embedded fonts, no CDN).

### Data Store (Single Google Sheet, 6 tabs)

`Users` · `Flashcards` · `Questions` · `StudyProgress` · `QuizAttempts` · `QuizAnswers`

All reads go through `SheetDB.gs` cache; writes acquire a `LockService` lock (~200ms penalty each).

### PDF Pipeline

`download_materials.py` → raw PDFs per event/year → `convert_events.py` orchestrates `pdf_ocr.py`, routing math-heavy events (Mathematics, Calculator Applications, Number Sense, Science) to the `marker` backend and all others to `docling`.

## Key Constraints

- Apps Script is **ECMAScript 5** — no `let`/`const`/arrow functions/template literals in `.gs` files.
- All 6-minute execution timeout limits apply; avoid long loops in server functions.
- Google Sheets is the only database. Sheet structure is set up once by `setupSpreadsheet()` and must not be changed without updating column-index constants in `SheetDB.gs`.
- The `.clasp.json` file contains a private script ID and is gitignored — never commit it.
