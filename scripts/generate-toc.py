#!/usr/bin/env python3
"""Regenerates the Prompts table in README.md from prompts/*.md frontmatter."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
README = REPO_ROOT / "README.md"

MARKER_START = "<!-- PROMPTS_START -->"
MARKER_END = "<!-- PROMPTS_END -->"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

DIFFICULTY_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2, "FML": 3}


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip('"')
    return data


def build_table(prompts):
    rows = ["| Title | Difficulty |", "|-------|------------|"]
    for p in prompts:
        link = f"[{p['title']}](prompts/{p['file']})"
        rows.append(f"| {link} | {p['difficulty']} |")
    return "\n".join(rows)


def main():
    prompts = []
    for path in PROMPTS_DIR.glob("*.md"):
        fm = parse_frontmatter(path.read_text())
        if not fm.get("title"):
            continue
        prompts.append({
            "title": fm["title"],
            "difficulty": fm.get("difficulty", ""),
            "file": path.name,
        })

    prompts.sort(key=lambda p: (
        DIFFICULTY_ORDER.get(p["difficulty"], 99),
        p["title"].lower(),
    ))

    table = build_table(prompts)

    readme = README.read_text()
    new_section = f"{MARKER_START}\n{table}\n{MARKER_END}"

    if MARKER_START in readme and MARKER_END in readme:
        updated = re.sub(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            new_section,
            readme,
            flags=re.DOTALL,
        )
    else:
        print("ERROR: markers not found in README.md", file=sys.stderr)
        sys.exit(1)

    if updated != readme:
        README.write_text(updated)
        print(f"README.md updated with {len(prompts)} prompts.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
