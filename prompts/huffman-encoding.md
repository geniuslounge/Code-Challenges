---
title: Huffman Encoding
difficulty: FML
---

Huffman coding is a lossless data compression algorithm developed by David A. Huffman in 1952. It works by assigning shorter binary codes to more frequent characters and longer codes to less frequent ones — so common characters take up less space.

Implement a full Huffman encoder and decoder:

1. **Build a frequency table** from the input string.
2. **Build a Huffman tree** — a binary tree where each leaf is a character. Use a priority queue (min-heap): repeatedly merge the two lowest-frequency nodes into a new parent node until one tree remains.
3. **Generate the codebook** — traverse the tree to assign a binary code to each character (left = `0`, right = `1`).
4. **Encode** the input string using the codebook.
5. **Decode** a binary string back to the original using the tree.

```python
text = "hello huffman"

encoded, tree = huffman_encode(text)
# encoded → something like "0101100011..." (varies by implementation)

decoded = huffman_decode(encoded, tree)
# decoded → "hello huffman"

assert decoded == text
```

**Bonus** — Calculate the compression ratio: how many bits does your encoding use vs. standard 8-bit ASCII?
