---
title: Roman Numerals
difficulty: Medium
---

Write a function that converts an integer to its Roman numeral representation.

| Symbol | Value |
|--------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Subtraction rules apply: `IV` = 4, `IX` = 9, `XL` = 40, `XC` = 90, `CD` = 400, `CM` = 900.

```
to_roman(3)     →  "III"
to_roman(4)     →  "IV"
to_roman(1994)  →  "MCMXCIV"
to_roman(2024)  →  "MMXXIV"
```

**Part 2** — Write the reverse: convert a Roman numeral string back to an integer.
