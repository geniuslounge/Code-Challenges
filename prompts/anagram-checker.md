---
title: Anagram Checker
difficulty: Medium
---

Two words are anagrams if they contain the exact same letters in a different order.

Write a function that takes two strings and returns `True` if they are anagrams of each other, `False` otherwise.

```
is_anagram("listen", "silent")   →  True
is_anagram("triangle", "integral") →  True
is_anagram("hello", "world")     →  False
```

- Ignore spaces and punctuation.
- Treat uppercase and lowercase letters as the same.

**Part 2** — Given a list of words, group all anagrams together.

```
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
→  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```
