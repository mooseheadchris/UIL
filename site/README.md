# AcDec Study Site

A study website for an Academic Decathlon team. Runs entirely inside Google
Workspace: an Apps Script web app backed by one Google Sheet, embedded in a
Google Site. No external services required.

**Features**

- Salted SHA-256 student logins (roster uploaded as CSV by the coach)
- Anki-style flashcards with a simplified SM-2 spaced-repetition algorithm
- Multiple-choice quizzes, scored server-side
- Leaderboard (all-time and last 7 days)
- Teacher dashboard: roster management, password resets, content upload,
  participation reports

## Architecture overview

```
Google Site (iframe)
    └── Apps Script Web App (/exec)
           ├── HtmlService SPA  (vanilla JS, no frameworks)
           └── google.script.run ─▶ Server .gs modules
                                       └── SpreadsheetApp + CacheService + LockService
                                                    │
                                                    ▼
                                           One Google Sheet (tabs = tables)
```

Sessions are signed HMAC tokens kept in the browser's `localStorage`. The web
app runs **as the owner** so students don't need access to the sheet itself.

## Repository layout

```
├── appsscript.json              # Apps Script manifest
├── .clasp.json.example          # Template — copy to .clasp.json and set scriptId
└── src/
    ├── Constants.gs             # subject enum, sheet names, points, SRS defaults
    ├── SheetDB.gs               # sheet I/O + caching + LockService
    ├── Auth.gs                  # hashing, HMAC session tokens, guards
    ├── Users.gs                 # roster import, user lookup
    ├── Study.gs                 # SM-2 algorithm + session composition
    ├── Quiz.gs                  # quiz lifecycle + server-side scoring
    ├── Leaderboard.gs           # aggregation + cache
    ├── Teacher.gs               # role-gated admin endpoints
    ├── Code.gs                  # doGet, include helper, setupSpreadsheet
    └── html/
        ├── index.html           # SPA shell
        ├── styles.html          # CSS
        ├── client.html          # router + RPC wrapper
        ├── view_login.html
        ├── view_dashboard.html
        ├── view_study.html
        ├── view_quiz.html
        ├── view_leaderboard.html
        ├── view_teacher.html
        └── katex.html            # self-hosted KaTeX (JS + CSS with
                                  # base64-embedded woff2 fonts)
```

## Setup

All of this can be done entirely in a web browser — no software to install on
your school computer.

### 1. Create the Google Sheet + bound Apps Script project

1. In Google Drive, create a new **Google Sheet** named e.g. "AcDec Study DB".
2. In that sheet, open **Extensions → Apps Script**.
3. The editor opens a new bound project. This is where the code lives.

### 2. Add the code — browser-only path (recommended for school computers)

In the Apps Script editor:

1. **Manifest.** Click the gear icon (**Project Settings**) and check
   _"Show appsscript.json manifest file in editor"_. Then in the Files panel,
   open `appsscript.json` and replace its contents with the manifest from this
   repo (`appsscript.json`).

2. **Server files (`.gs`).** Delete the default `Code.gs`. For each file under
   `src/` in this repo (there are 9), click the **+** next to Files → **Script**,
   type the name without extension (e.g. `Constants`, `SheetDB`, `Auth`, …),
   then paste the contents of the matching `src/NAME.gs` file from this repo.

3. **HTML files.** For each file under `src/html/` (there are 10 — including
   `html/katex`, which is large), click **+** → **HTML**, enter the name
   **including the `html/` prefix** (e.g. `html/index`, `html/styles`,
   `html/client`, `html/view_login`, …), then paste contents. The slash in
   the name is valid — it's how Apps Script namespaces the partials that
   `include('html/...')` looks up.

   Note: `html/katex` is ~630 KB (KaTeX JS + CSS with all math fonts embedded
   as base64) so everything works even when CDNs are blocked. Paste it like
   any other HTML file — the Apps Script editor handles it fine.

That's it — you now have all 20 files in the project.

### 2b. Optional: `clasp` (only if you can install npm)

If you have a personal computer where `npm` works, `clasp` lets you `git pull`
and `clasp push` instead of pasting files. Steps:

```bash
npm install -g @google/clasp
clasp login
cp .clasp.json.example .clasp.json   # paste the scriptId into it
clasp push -f
```

`.clasp.json` is gitignored so you don't leak your script ID. Skip this whole
section if you can't install npm.

### 3. Run the one-time setup

In the Apps Script editor, select the function `setupSpreadsheet` and click
**Run**. You'll be prompted to authorize the script's scopes. After it
completes:

- All sheet tabs are created with correct headers.
- A seed **teacher** account is created using your own Google email.
- The temporary password is written to the execution log **and** to
  `Project Settings → Script Properties → SEED_TEACHER_PASSWORD`.

**Change that password from the teacher UI immediately**, then delete the
`SEED_TEACHER_PASSWORD` property.

### 4. Deploy as a web app

In the editor: **Deploy → New deployment → Web app**.

- Execute as: **Me** (owner)
- Who has access: **Anyone** (required so students who aren't signed into a
  Google account can still log in; Apps Script still runs as you)

Copy the web app URL (`.../exec`).

### 5. Embed in Google Sites

1. Open your (new) Google Site, pick a page, click **Insert → Embed → By URL**.
2. Paste the web app `/exec` URL and insert.
3. Resize the embed block to roughly fill the page.
4. Publish the site.

Done. Students visit the Google Site page and use the app inline.

## Roster import format

Paste CSV into the teacher dashboard. Header row is optional.

```csv
email,firstName,lastName,initialPassword,role
student1@school.edu,Jordan,Lee,Temp1234,student
student2@school.edu,Kai,Morris,Temp5678,student
coach@school.edu,Coach,Smith,Coach9999,teacher
```

**Security notes**

- Passwords are salted SHA-256. Do not reuse a student's school-login password
  — this site's passwords should be site-specific.
- Students cannot self-register or self-reset; teachers issue temp passwords.
- Session tokens expire after 12 hours.

**Teacher backup password (emergency access)**

If you lock yourself out, set a Script Property to grant any teacher account
emergency login without touching the sheet:

1. Apps Script editor → **Project Settings → Script Properties → Add property**
2. Name: `BACKUP_TEACHER_PASSWORD`
3. Value: any string you'll remember (e.g. `OpenSesame123`)
4. Save. Now any user with `role=teacher` can log in using that password.
5. Delete the property when you're back in to re-lock it.

Only teacher-role accounts are eligible — student logins always go through the
normal salted-hash check. Script Properties are only visible to project
editors, so this is as private as the script itself.

## Flashcards CSV

Header row required. `section` column is optional — omit it, or leave blank
on individual rows.

```csv
subject,section,front,back
Mathematics,Section 1,What is the derivative of x^2?,2x
Mathematics,Section 2,Solve for x: 3x + 5 = 14,3
Science,,Formula for the ideal gas law?,PV = nRT
```

## Questions CSV

Header row required. `section` and `explanation` columns are optional.

```csv
subject,section,prompt,choiceA,choiceB,choiceC,choiceD,correctChoice,explanation
Science,Section 1,Water boils at sea level at?,50°C,75°C,100°C,212°C,C,100°C = 212°F.
```

Subject must match one of:

`Art`, `Economics`, `Language & Literature`, `Mathematics`, `Music`, `Science`, `Social Science`, `Essay`, `Interview`, `Speech`

Sections are free-form text — use whatever the team's study guide calls them
("Section 1", "Chapter 3", "Impressionism"…). Rows with a blank section are
only reachable when students choose "All sections" — so naming your sections
consistently matters. If you get typos ("Section  1" vs "Section 1"), fix
them in the Edit content panel described below.

## Math equations (LaTeX)

KaTeX is bundled into `src/html/katex.html` with all fonts inlined as base64,
so math rendering works fully offline — nothing loads from a CDN. Use LaTeX
delimiters anywhere students see text (flashcard front/back, quiz prompts,
choices, explanations):

| Delimiter | Use | Example |
|---|---|---|
| `$...$` | Inline math | `The formula $E = mc^2$ shows…` |
| `$$...$$` | Display (centered, larger) | `$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$` |
| `\(...\)` | Inline (alternate) | same as `$...$` |
| `\[...\]` | Display (alternate) | same as `$$...$$` |

CSV example with math:

```csv
subject,section,front,back
Mathematics,Calculus,What is $\frac{d}{dx} x^2$?,$2x$
Mathematics,Calculus,Solve $$\int_0^1 x^2 \, dx$$,$$\frac{1}{3}$$
Science,Physics,Newton's second law?,$F = ma$
```

If LaTeX fails to parse (typo in the source), KaTeX shows the raw source as
plain text instead of crashing — so bad math never breaks the card.

### Regenerating `html/katex.html` (only if you want to update KaTeX)

The bundled file is KaTeX 0.16.11. To rebuild it against a newer version, on
any machine with `npm`:

```bash
cd /tmp && npm pack katex@<version>
tar -xzf katex-<version>.tgz
node /path/to/this/repo/scripts/build-katex.js   # reads ./package/dist, writes src/html/katex.html
```

(The build script is `scripts/build-katex.js` in this repo — copy it if you
plan to upgrade. Most users will never need to touch this.)

## Editing uploaded content

The teacher dashboard includes an **Edit content** panel. Switch between the
Flashcards and Questions tabs, filter by subject + section, type in the search
box to find a specific card, and click **Edit** on any row. Each row expands
into a full form — subject, section, front/back (or prompt/choices/correct
choice/explanation), **Save** / **Cancel** / **Delete**. Pagination shows 25
rows at a time.

Deleting a flashcard also removes all student SRS progress for that card.
Deleting a question leaves historical quiz attempts intact (scores still
reflect the original answers).

## Verification checklist

After deployment, walk through these in order:

1. **Setup** — sheet has tabs `Users, Flashcards, Questions, StudyProgress, QuizAttempts, QuizAnswers` with headers.
2. **Auth** — log in as seed teacher directly at the `/exec` URL. Wrong password is rejected.
3. **Content upload** — paste a few flashcards and questions. Confirm rows appear in the sheet with generated IDs.
4. **Student flow** — create a test student account via roster import. Log in (incognito window). Study → rate cards → confirm `StudyProgress` rows appear and `nextDue` advances. Take a quiz → confirm score + attempt row.
5. **Leaderboard** — 2+ students accumulate points; order is correct; updates within 5 minutes.
6. **Embed** — open the Google Site page in a fresh browser not signed into a Google account — login + full flow still works inside the iframe.
7. **Role enforcement** — from the browser devtools as a student, try `google.script.run.teacher_listUsers('<student-token>')` → returns "Not authorized."

## Known limits

- **Write serialization**: every write goes through `LockService.getScriptLock()` to avoid interleaving. Latency penalty ~200 ms.
- **Scale**: ~30 students × ~2000 cards = tens of thousands of rows. Well within Sheets' 10M-cell cap and the 6-minute script execution limit, since hot reads are cached.
- **Password policy**: no self-service reset. Coach issues a new temp password via the teacher UI.

## License

MIT.
