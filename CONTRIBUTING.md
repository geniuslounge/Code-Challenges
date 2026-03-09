# Contributing

Thanks for wanting to add a prompt! Here's everything you need to know.

## Adding a Prompt

1. **Fork** this repo and create a branch.
2. **Create a file** in `prompts/` named in kebab-case: `your-prompt-title.md`
3. **Add frontmatter** at the top of the file:

```markdown
---
title: Your Prompt Title
difficulty: Easy | Medium | Hard | FML
---

Your prompt description here.
```

4. **Open a pull request.** The README and difficulty pages update automatically on merge — you don't need to run any scripts.

## Difficulty Guide

| Level | Description |
|-------|-------------|
| Easy | Solvable in a few lines; good for beginners |
| Medium | Requires some thought about logic or data structures |
| Hard | Non-trivial algorithm or significant implementation effort |
| FML | You'll question your life choices |

## Prompt Guidelines

- **Be clear and self-contained.** Include any sample input/output so solvers know what to aim for.
- **Language-agnostic.** Don't write prompts that require a specific language.
- **Original wording.** If your prompt is based on a well-known problem, write the description in your own words.
- **One prompt per file.** Keep each challenge in its own `.md` file.

## What Makes a Good Prompt?

- Has a clear goal and success criteria
- Includes at least one example with expected output
- Optionally includes a "Part 2" to extend the challenge

## Questions?

Open an issue and tag it `question`.
