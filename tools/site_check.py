#!/usr/bin/env python3
"""QA check for the BatterijWijzer static site.

Checks every site/*.html page for:
- internal links (href/src) that point to files that don't exist
- missing <title>, meta description, og:title, favicon, viewport
- sitemap.xml coverage (every indexable page listed, no dead entries)
Exit code 1 if any problem is found. Run from repo root: python3 tools/site_check.py
"""
import re
import sys
import pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent / "site"
NOINDEX = re.compile(r'<meta name="robots" content="noindex">')
problems = []

pages = sorted(SITE.glob("*.html"))
page_names = {p.name for p in pages}

for page in pages:
    html = page.read_text(encoding="utf-8")
    # internal links
    for attr, target in re.findall(r'(href|src)="([^"]+)"', html):
        if target.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        name = target.split("#")[0].split("?")[0]
        if name and not (SITE / name).exists():
            problems.append(f"{page.name}: broken internal {attr} -> {target}")
    # required head elements
    checks = {
        "<title>": "<title>" in html,
        "meta description": 'name="description"' in html or NOINDEX.search(html),
        "og:title": 'property="og:title"' in html or bool(NOINDEX.search(html)),
        "viewport": 'name="viewport"' in html,
        "favicon": 'rel="icon"' in html,
    }
    for label, ok in checks.items():
        if not ok:
            problems.append(f"{page.name}: missing {label}")

# inline JS sanity: balanced braces/parens in every non-JSON-LD script block
for page in pages:
    html = page.read_text(encoding="utf-8")
    for script in re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", html, re.S):
        for open_ch, close_ch in (("{", "}"), ("(", ")")):
            if script.count(open_ch) != script.count(close_ch):
                problems.append(f"{page.name}: unbalanced {open_ch}{close_ch} in inline script")

# sitemap coverage
sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
listed = set(re.findall(r"<loc>/?([^<]+)</loc>", sitemap))
skip = {"privacy.html", "404.html"}  # noindex / error pages stay out of the sitemap
for p in pages:
    if p.name in skip:
        continue
    if p.name not in listed:
        problems.append(f"sitemap.xml: missing {p.name}")
for entry in listed:
    if entry not in page_names:
        problems.append(f"sitemap.xml: dead entry {entry}")

# data freshness (non-fatal): warn when a page's newest Dutch "peildatum" month is stale
import datetime

MONTHS = {m: i + 1 for i, m in enumerate(
    ["januari", "februari", "maart", "april", "mei", "juni", "juli",
     "augustus", "september", "oktober", "november", "december"])}
today = datetime.date.today()
warnings = []
for page in pages:
    html = page.read_text(encoding="utf-8").lower()
    dates = [(int(y), MONTHS[m]) for m, y in re.findall(
        r"\b(" + "|".join(MONTHS) + r")\s+(20\d\d)\b", html)]
    if not dates:
        continue
    year, month = max(dates)
    age_months = (today.year - year) * 12 + (today.month - month)
    if age_months > 1:
        warnings.append(f"{page.name}: peildatum {month:02d}-{year} is {age_months} months old")

if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
if warnings:
    print(f"{len(warnings)} freshness warning(s) (non-fatal):")
    for w in warnings:
        print(" ~", w)
print(f"OK: {len(pages)} pages checked, no problems.")
