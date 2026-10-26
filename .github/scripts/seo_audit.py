#!/usr/bin/env python3
"""Read-only SEO audit for a static HTML/GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from collections import defaultdict
import json

ROOT = Path(".")
IGNORE = {".git", ".github", "node_modules", "vendor", "dist", "build"}
BASE_URL = "https://fashiondesign4all786-tech.github.io/Tools/"

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.description = ""
        self.canonical = ""
        self.h1 = 0
        self.images_missing_alt = 0
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title": self.in_title = True
        elif tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "").strip()
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonical = a.get("href", "").strip()
        elif tag == "h1": self.h1 += 1
        elif tag == "img" and "alt" not in a: self.images_missing_alt += 1
        elif tag == "a" and a.get("href"): self.links.append(a["href"])
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
    def handle_data(self, data):
        if self.in_title: self.title += data.strip()

def html_files():
    for p in ROOT.rglob("*.html"):
        if not any(part in IGNORE for part in p.parts):
            yield p

pages, issues = [], []
for path in sorted(html_files()):
    parser = PageParser()
    try:
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    except OSError as exc:
        issues.append((str(path), "ERROR", f"Could not read file: {exc}"))
        continue
    item = {"path": str(path), "title": parser.title.strip(),
            "description": parser.description, "canonical": parser.canonical,
            "h1_count": parser.h1, "images_missing_alt": parser.images_missing_alt,
            "links": parser.links}
    pages.append(item)
    if not item["title"]: issues.append((str(path), "HIGH", "Missing <title>"))
    elif len(item["title"]) > 60: issues.append((str(path), "LOW", f"Title is long ({len(item['title'])} characters)"))
    if not item["description"]: issues.append((str(path), "HIGH", "Missing meta description"))
    elif len(item["description"]) < 70 or len(item["description"]) > 160:
        issues.append((str(path), "LOW", f"Meta description length is {len(item['description'])} characters; review target 70–160"))
    if not item["canonical"]: issues.append((str(path), "MEDIUM", "Missing canonical URL; confirm intended URL before adding"))
    if item["h1_count"] == 0: issues.append((str(path), "MEDIUM", "No H1 heading detected"))
    elif item["h1_count"] > 1: issues.append((str(path), "LOW", f"{item['h1_count']} H1 headings detected; review page structure"))
    if item["images_missing_alt"]: issues.append((str(path), "MEDIUM", f"{item['images_missing_alt']} image(s) missing alt attribute"))

for field, label in (("title", "Duplicate title"), ("description", "Duplicate meta description")):
    grouped = defaultdict(list)
    for p in pages:
        value = p[field].strip().casefold()
        if value: grouped[value].append(p["path"])
    for value, paths in grouped.items():
        if len(paths) > 1:
            for path in paths:
                issues.append((path, "MEDIUM", f"{label}: also used by {', '.join(x for x in paths if x != path)}"))

lines = ["# SEO Audit Report", "", f"- Site: {BASE_URL}", f"- HTML pages scanned: {len(pages)}",
         f"- Findings: {len(issues)}", "", "## Findings", ""]
if issues:
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "ERROR": 3}
    for path, severity, detail in sorted(issues, key=lambda x: (order.get(x[1], 9), x[0], x[2])):
        lines.append(f"- **{severity}** — `{path}`: {detail}")
else:
    lines.append("No basic metadata findings detected.")
lines += ["", "## Page inventory", "", "| Page | Title | Description chars | Canonical | H1 count | Missing image alt |",
          "|---|---|---:|---|---:|---:|"]
for p in pages:
    lines.append(f"| `{p['path']}` | {p['title'].replace('|', '\\|') or '—'} | {len(p['description'])} | {'yes' if p['canonical'] else 'no'} | {p['h1_count']} | {p['images_missing_alt']} |")
lines += ["", "## Safety notes", "",
          "- This audit is read-only and does not edit or publish site files.",
          "- Findings are heuristics, not Google ranking guarantees.",
          "- Canonical URLs, generated alt text, redirects, robots rules, and page copy require human review before changes.",
          "- This report checks HTML metadata and structure; it does not measure Core Web Vitals, backlinks, search rankings, or Search Console indexing."]
Path("seo-audit-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
Path("seo-audit-report.json").write_text(json.dumps({"site": BASE_URL, "pages_scanned": len(pages),
    "finding_count": len(issues), "findings": [{"path": p, "severity": s, "detail": d} for p,s,d in issues]}, indent=2), encoding="utf-8")
print(f"Scanned {len(pages)} HTML pages; recorded {len(issues)} findings.")
