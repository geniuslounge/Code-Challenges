---
title: Maze Solver
difficulty: Hard
---

Given a 2D grid representing a maze, find the shortest path from the start to the exit.

- `0` = open path
- `1` = wall
- `S` = start
- `E` = exit

```python
maze = [
    ["S", 0, 1, 0, 0],
    [1,   0, 1, 0, 1],
    [1,   0, 0, 0, 1],
    [1,   1, 1, 0, 1],
    [0,   0, 0, 0, "E"],
]
```

Your function should return the shortest path as a list of `(row, col)` coordinates, or `None` if no path exists.

- You may only move up, down, left, or right (no diagonals).

**Part 2** — Allow diagonal movement. Does the shortest path change?
