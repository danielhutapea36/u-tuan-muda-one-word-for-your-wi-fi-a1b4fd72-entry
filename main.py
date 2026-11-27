#!/usr/bin/env python3
"""One Word for Your Wi-Fi - make.fun entry.

Writes the single chosen word to /output/entry.txt.

Deterministic by construction: a fixed constant, no randomness, no
clock, no network, no input, no environment. Every run writes the
exact same bytes.
"""

import os

WORD = "Hiccup"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
