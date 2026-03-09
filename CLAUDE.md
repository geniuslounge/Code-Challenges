# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A community-driven collection of coding challenge prompts for interview prep and skill building. Contributors fork, add a prompt file, and submit a pull request.

## Adding a New Prompt

Create a single markdown file in `prompts/` named `kebab-title.md` (e.g. `my-new-prompt.md`) with this frontmatter:

```markdown
---
title: Your Prompt Title
difficulty: Easy | Medium | Hard | FML
---

Prompt description here.
```

No numeric prefix — prompts are sorted by difficulty (Easy → Medium → Hard → FML), then alphabetically by title within each tier.

The README table of contents updates automatically via GitHub Actions on merge. No scripts to run.

## README Table of Contents

`scripts/generate-toc.py` reads all `prompts/*.md` files, parses frontmatter, and rewrites the section between `<!-- PROMPTS_START -->` and `<!-- PROMPTS_END -->` in `README.md`. Run it locally with:

```bash
python3 scripts/generate-toc.py
```

The GitHub Action (`.github/workflows/update-readme.yml`) runs this automatically on every push to `main` that touches `prompts/`.
