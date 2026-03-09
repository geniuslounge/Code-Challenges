---
title: Caesar Cipher
difficulty: Easy
---

One of the oldest known encryption techniques, the Caesar cipher works by shifting each letter in a message a fixed number of positions along the alphabet. A shift of 3 turns `A` into `D`, `B` into `E`, and so on. It wraps around, so `Z` with a shift of 1 becomes `A`.

Write two functions: one to **encode** a message with a given shift, and one to **decode** it.

```
encode("Hello, World!", 3)  →  "Khoor, Zruog!"
decode("Khoor, Zruog!", 3)  →  "Hello, World!"
```

- Non-letter characters (spaces, punctuation, numbers) should pass through unchanged.
- Preserve the original casing of each letter.
