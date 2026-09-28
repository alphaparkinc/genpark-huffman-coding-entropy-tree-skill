"""Huffman Coding & Shannon Entropy Engine.
100% Python Standard Library.
"""

import math
import heapq
from collections import Counter

class HuffmanCoder:
    """Canonical Huffman tree encoder/decoder and entropy calculator."""

    @staticmethod
    def calculate_entropy(data: str) -> float:
        if not data:
            return 0.0
        counts = Counter(data)
        n = len(data)
        return -sum((c / n) * math.log2(c / n) for c in counts.values())

    @staticmethod
    def build_tree(data: str) -> dict:
        if not data:
            return {}
        counts = Counter(data)
        if len(counts) == 1:
            char = list(counts.keys())[0]
            return {char: "0"}
        heap = [[weight, [char, ""]] for char, weight in counts.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = "0" + pair[1]
            for pair in hi[1:]:
                pair[1] = "1" + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

    @classmethod
    def encode(cls, text: str) -> tuple:
        tree = cls.build_tree(text)
        bits = "".join(tree[c] for c in text)
        return bits, tree

    @classmethod
    def decode(cls, bits: str, tree: dict) -> str:
        rev_tree = {v: k for k, v in tree.items()}
        curr = ""
        out = []
        for b in bits:
            curr += b
            if curr in rev_tree:
                out.append(rev_tree[curr])
                curr = ""
        return "".join(out)
