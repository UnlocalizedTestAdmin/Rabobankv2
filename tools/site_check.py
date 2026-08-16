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

if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"OK: {len(pages)} pages checked, no problems.")
