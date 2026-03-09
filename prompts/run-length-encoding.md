---
title: Run-Length Encoding
difficulty: Medium
---

Run-length encoding (RLE) is a simple compression technique that replaces consecutive repeated characters with a count and the character.

Write two functions: one to **encode** a string and one to **decode** it.

```
encode("AAABBC")        →  "3A2B1C"
encode("AABBAABB")      →  "2A2B2A2B"
encode("ABCD")          →  "1A1B1C1D"

decode("3A2B1C")        →  "AAABBC"
decode("2A2B2A2B")      →  "AABBAABB"
```

**Part 2** — Optimize the encoder so that single characters are stored without a count prefix (e.g. `"ABCD"` → `"ABCD"` rather than `"1A1B1C1D"`). Update the decoder to handle both formats.
