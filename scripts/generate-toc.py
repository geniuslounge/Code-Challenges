#!/usr/bin/env python3
"""Generates per-difficulty pages and updates README.md links."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
README = REPO_ROOT / "README.md"

MARKER_START = "<!-- PROMPTS_START -->"
MARKER_END = "<!-- PROMPTS_END -->"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

DIFFICULTIES = ["Easy", "Medium", "Hard", "FML"]


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


def build_difficulty_page(difficulty, prompts):
    lines = [f"# {difficulty} Prompts\n"]
    if not prompts:
        lines.append("_No prompts yet. Be the first to contribute one!_\n")
    else:
        for p in sorted(prompts, key=lambda p: p["title"].lower()):
            lines.append(f"- [{p['title']}](prompts/{p['file']})")
    return "\n".join(lines) + "\n"


def build_readme_links(counts):
    lines = []
    for d in DIFFICULTIES:
        count = counts.get(d, 0)
        noun = "prompt" if count == 1 else "prompts"
        lines.append(f"- [{d}]({d}.md) — {count} {noun}")
    return "\n".join(lines)


def main():
    all_prompts = []
    for path in PROMPTS_DIR.glob("*.md"):
        fm = parse_frontmatter(path.read_text())
        if not fm.get("title"):
            continue
        all_prompts.append({
            "title": fm["title"],
            "difficulty": fm.get("difficulty", ""),
            "file": path.name,
        })

    by_difficulty = {d: [] for d in DIFFICULTIES}
    for p in all_prompts:
        if p["difficulty"] in by_difficulty:
            by_difficulty[p["difficulty"]].append(p)

    # Write per-difficulty pages
    for difficulty, prompts in by_difficulty.items():
        page_path = REPO_ROOT / f"{difficulty}.md"
        content = build_difficulty_page(difficulty, prompts)
        page_path.write_text(content)
        print(f"{difficulty}.md written ({len(prompts)} prompts).")

    # Update README
    counts = {d: len(p) for d, p in by_difficulty.items()}
    links = build_readme_links(counts)
    readme = README.read_text()
    new_section = f"{MARKER_START}\n{links}\n{MARKER_END}"

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
        print("README.md updated.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
