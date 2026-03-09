---
title: Binary Search
difficulty: Medium
---

Given a **sorted** list of integers and a target value, write a function that returns the index of the target using binary search. If the target is not in the list, return `-1`.

Binary search works by repeatedly halving the search space: compare the target to the middle element, then eliminate the half that can't contain the target.

```
binary_search([1, 3, 5, 7, 9, 11, 13], 7)   →  3
binary_search([1, 3, 5, 7, 9, 11, 13], 6)   →  -1
binary_search([2, 4, 6, 8, 10], 10)          →  4
```

- Do not use any built-in search functions — implement the algorithm yourself.

**Part 2** — What is the time complexity of binary search vs. a linear scan? At what list size does the difference become meaningful?
