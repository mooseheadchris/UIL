"""
parse_flashcards.py
Parse UIL Mathematics .md files -> flashcard CSV.
Output: Mathematics/math_flashcards.csv
Headers: Subject, Section, Front, Back

Usage:
    python parse_flashcards.py
    python parse_flashcards.py --verbose
"""

import csv, re, sys
from pathlib import Path
from collections import Counter

HERE   = Path(__file__).parent
MD_DIR = HERE / "md"
OUT    = HERE / "math_flashcards.csv"

CYRILLIC_MAP = str.maketrans("АВСЕаве", "ABCEabe")
def normalize(s): return s.translate(CYRILLIC_MAP).strip()

# ---------------------------------------------------------------------------
# Answer key parser -- handles three table formats found across the files:
#   Format 1 (2019 explicit):  | 1. | C | 21. | E | 41. | D |
#   Format 2 (2018-A/D):       | C  | 21. | B  | 41. | B  |  (row pos = prob #)
#   Format 3 (2018-B/R/S, 2019-R): | 1. | B | 21. C | 41. A |
# ---------------------------------------------------------------------------
def extract_num_letter(cell):
    cell = re.sub(r'<[^>]+>', '', cell)
    m = re.search(r'(\d+)\.?\s*([A-E])', cell)
    if m:
        return int(m.group(1)), m.group(2)
    return None

def parse_answer_key(text):
    key_start = re.search(r'Answer Key', text, re.I)
    if not key_start:
        return {}
    key_section = text[key_start.start():]
    answers = {}
    data_rows = []
    for line in key_section.split('\n'):
        if '|' not in line or '---' in line:
            continue
        cols = [normalize(c) for c in line.split('|')]
        cols = [c for c in cols if c]
        if not any(re.search(r'[A-E]', c) for c in cols):
            continue
        data_rows.append(cols)
    for row_idx, cols in enumerate(data_rows[:20]):
        n = row_idx + 1
        if len(cols) == 6:
            # Format 1
            for i in range(0, 6, 2):
                nm = re.match(r'(\d+)', cols[i])
                letter = cols[i+1] if i+1 < len(cols) else ''
                if nm and re.fullmatch(r'[A-E]', letter):
                    answers[int(nm.group(1))] = letter
        elif len(cols) == 5:
            # Format 2
            if re.fullmatch(r'[A-E]', cols[0]):
                answers[n] = cols[0]
            for num_col, ans_col in [(1, 2), (3, 4)]:
                nm = re.match(r'(\d+)', cols[num_col])
                if nm and re.fullmatch(r'[A-E]', cols[ans_col]):
                    answers[int(nm.group(1))] = cols[ans_col]
        elif len(cols) == 4:
            # Format 3
            nm = re.match(r'(\d+)', cols[0])
            letter = cols[1] if len(cols) > 1 else ''
            if nm and re.fullmatch(r'[A-E]', letter):
                answers[int(nm.group(1))] = letter
            for cell in cols[2:]:
                result = extract_num_letter(cell)
                if result:
                    answers[result[0]] = result[1]
    return answers

# ---------------------------------------------------------------------------
# Section classifier
# ---------------------------------------------------------------------------
SECTION_RULES = [
    ("Calculus", re.compile(
        r"\b(deriv|integr(?:al|at)|differenti(?:able|ate)|instantaneous rate"
        r"|rate of change|lim\b|continuous|continuity|D_x|tangent line"
        r"|area under|antiderivat|secant line|local min|local max)\b", re.I)),
    ("Statistics", re.compile(
        r"\b(probabilit|odds that|standard deviation|variance|expected value"
        r"|normal dist|regression|percentile|how many ways|arrangements?\b"
        r"|randomly|average rate of return)\b", re.I)),
    ("Pre-Calc", re.compile(
        r"\b(sin|cos|tan\b|sec\b|csc\b|cot\b|trig|bearing|amplitude|phase shift"
        r"|period\b|radian|inverse trig|polar|harmonic mean|parametric|asymptote"
        r"|focus|directrix|parabola|ellipse)\b", re.I)),
    ("Algebra 2", re.compile(
        r"\b(polynomial|logarithm|\blog\b|exponential|matrix|matric"
        r"|(?:arithmetic|geometric) sequence|series\b|fibonacci|binomial|expansion"
        r"|remainder theorem|factor theorem|quadratic formula|discriminant"
        r"|complex number|lucas number|rational root)\b", re.I)),
    ("Geometry", re.compile(
        r"\b(triangle|circle|perimeter|rhombus|inscribed|circumscribed"
        r"|similar|congruent|radius|diameter|rectangle|sphere|cylinder|cone"
        r"|quadrilateral|hexagon|pentagon|trapezoid|polygon|altitude|hypotenuse"
        r"|scalene|isosceles|equilateral|midpoint|diagonal|chord|sector"
        r"|surface area|volume|supplementary|concurrency|orthocenter"
        r"|circumcenter|centroid|incenter|nonahedron|parallelogram)\b", re.I)),
]

def classify_section(text):
    for section, pattern in SECTION_RULES:
        if pattern.search(text):
            return section
    return "Algebra 1"

# ---------------------------------------------------------------------------
# Problem splitter
# ---------------------------------------------------------------------------
PROB_START = re.compile(r'(?:^|\n)[ \t]*[-*]?[ \t]*\*{0,2}(\d{1,2})\.\s', re.M)

def split_problems(text):
    key_start = re.search(r'Answer Key', text, re.I)
    body = text[:key_start.start()] if key_start else text
    matches = [(m.start(), int(m.group(1))) for m in PROB_START.finditer(body)
               if 1 <= int(m.group(1)) <= 60]
    problems, seen = [], set()
    for i, (pos, num) in enumerate(matches):
        if num in seen:
            continue
        seen.add(num)
        end = matches[i+1][0] if i+1 < len(matches) else len(body)
        problems.append((num, body[pos:end].strip()))
    return problems

# ---------------------------------------------------------------------------
# Choice extractor
# ---------------------------------------------------------------------------
CHOICE_RE = re.compile(
    r'[-*]?\s*\*{0,2}\(([A-E])\)\*{0,2}\s*(.*?)(?=\s*[-*]?\s*\*{0,2}\([A-E]\)|$)',
    re.S)

def extract_choices(text):
    choices = {}
    for m in CHOICE_RE.finditer(text):
        letter = m.group(1)
        val = re.sub(r'\s+', ' ', m.group(2)).strip().rstrip('*').strip()
        if letter not in choices and val:
            choices[letter] = val
    return choices

def has_image(text): return bool(re.search(r'!\[\]\(', text))

def clean_front(text):
    text = re.sub(r'^[ \t]*[-*]?\s*\*{0,2}\d{1,2}\.\s*\*{0,2}', '', text.strip())
    text = re.split(r'\s*[-*]?\s*\*{0,2}\(A\)', text)[0]
    return re.sub(r'[\n ]+', ' ', text).strip()

def clean_back(letter, text):
    text = re.sub(r'[\n ]+', ' ', text).strip().rstrip('*').strip()
    return f"({letter}) {text}"

def process_file(md_path, verbose=False):
    text = md_path.read_text(encoding="utf-8", errors="replace")
    answers = parse_answer_key(text)
    problems = split_problems(text)
    if verbose:
        print(f"  Key entries: {len(answers)}, Problems found: {len(problems)}")
    rows = []
    for num, raw in problems:
        if has_image(raw):
            continue
        correct_letter = answers.get(num)
        if not correct_letter:
            if verbose: print(f"    #{num}: no key entry")
            continue
        choices = extract_choices(raw)
        correct_text = choices.get(correct_letter, '').strip()
        if not correct_text:
            if verbose: print(f"    #{num}: missing choice {correct_letter}, got {list(choices.keys())}")
            continue
        front = clean_front(raw)
        if len(front) < 15:
            continue
        back = clean_back(correct_letter, correct_text)
        rows.append({
            "Subject": "Mathematics",
            "Section": classify_section(front + " " + back),
            "Front": front,
            "Back": back,
        })
    return rows

def main():
    verbose = "--verbose" in sys.argv
    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        sys.exit(f"No .md files found in {MD_DIR}")
    all_rows = []
    for md in md_files:
        rows = process_file(md, verbose)
        print(f"  {md.name}: {len(rows)} flashcards")
        all_rows.extend(rows)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Subject", "Section", "Front", "Back"])
        writer.writeheader()
        writer.writerows(all_rows)
    counts = Counter(r["Section"] for r in all_rows)
    print(f"\nTotal: {len(all_rows)} flashcards")
    for sec, n in sorted(counts.items()):
        print(f"  {sec}: {n}")
    print(f"\nSaved -> {OUT}")

if __name__ == "__main__":
    main()
