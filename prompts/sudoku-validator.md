---
title: Sudoku Validator
difficulty: Hard
---

Write a function that takes a 9×9 Sudoku board and returns `True` if it is **valid**, `False` otherwise.

A valid board satisfies all of these:
- Each row contains the digits 1–9 with no repeats.
- Each column contains the digits 1–9 with no repeats.
- Each of the nine 3×3 sub-boxes contains the digits 1–9 with no repeats.

Empty cells are represented by `0` and should be ignored during validation — you are checking whether the *filled* cells violate any rules, not whether the puzzle is solved.

```python
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

is_valid_sudoku(board)  →  True
```
