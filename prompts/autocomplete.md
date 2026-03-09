---
title: Autocomplete
difficulty: Hard
---

Build an autocomplete system using a **trie** (prefix tree) data structure.

A trie stores words by their characters, where each node represents a single character and paths from root to a terminal node spell out a word.

Implement a `Trie` class with the following methods:

- `insert(word)` — add a word to the trie
- `search(word)` — return `True` if the exact word exists
- `starts_with(prefix)` — return `True` if any word in the trie starts with the given prefix
- `autocomplete(prefix)` — return a list of all words in the trie that start with the given prefix

```python
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("apply")
trie.insert("banana")

trie.search("app")           →  True
trie.starts_with("appl")     →  True
trie.autocomplete("app")     →  ["app", "apple", "application", "apply"]
trie.autocomplete("ban")     →  ["banana"]
trie.autocomplete("xyz")     →  []
```
