---
title: Word Frequency
difficulty: Medium
---

Given a block of text, write a function that returns the top N most frequently occurring words.

```
text = "the quick brown fox jumps over the lazy dog the fox"

top_words(text, 3)  →  [("the", 3), ("fox", 2), ("quick", 1)]
```

- Ignore punctuation and treat words case-insensitively.
- Break ties alphabetically.

**Part 2** — Exclude common "stop words" (`the`, `a`, `an`, `is`, `in`, `on`, `of`, `and`, `or`, etc.) from the results.
