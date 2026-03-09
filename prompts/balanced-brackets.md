---
title: Balanced Brackets
difficulty: Medium
---

Write a function that takes a string and returns `True` if all brackets are properly opened and closed, `False` otherwise.

The bracket types to handle: `()`, `[]`, `{}`

```
is_balanced("([]{})")        →  True
is_balanced("{[()]}")        →  True
is_balanced("([)]")          →  False
is_balanced("{[}")           →  False
is_balanced("")              →  True
```

- Brackets must close in the correct order — the most recently opened bracket must be closed first.
- Non-bracket characters in the string should be ignored.
