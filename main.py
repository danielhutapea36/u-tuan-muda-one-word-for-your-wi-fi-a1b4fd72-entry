#!/usr/bin/env python3
"""One Word for Your Wi-Fi - make.fun entry.

Writes the single chosen word to /output/entry.txt.

Deterministic by construction: a fixed constant, no randomness, no
clock, no network, no input, no environment. Every run writes the
exact same bytes.

The word is validated against the competition gate before it is
written (UTF-8 text, 1 to 20 characters, not only white space, a
single word), and the file is written atomically (temporary file +
rename) so a run never leaves a partial entry behind.
"""

import os

WORD = "Hiccup"
OUTPUT_PATH = "/output/entry.txt"


def _validate(word: str) -> None:
    if not 1 <= len(word.encode("utf-8")) <= 20:
        raise ValueError("entry must be 1 to 20 UTF-8 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")


def main() -> None:
    _validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.replace(tmp_path, OUTPUT_PATH)
    print(WORD)


if __name__ == "__main__":
    main()
