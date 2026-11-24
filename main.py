#!/usr/bin/env python3
"""One Sentence, One Journey — make.fun bounty entry.

Writes a complete story about a journey in exactly one sentence
(at most 300 characters) to /output/entry.txt: she sells the house,
flies one-way on a ticket booked in her mother's name by mistake,
and when the border guard mispronounces it, she lets it stand —
the woman in seat 14 travelling lighter than the one who left.

Deterministic: the text is a constant, so every run writes the same
bytes. No network.
"""
import os

TEXT = (
    "She sold her house, flew one-way on a ticket booked in her "
    "mother's name by mistake, and when the border guard mispronounced "
    "it, she let it stand — the woman in seat 14 was travelling "
    "lighter than the one who left."
)


def main():
    assert 1 <= len(TEXT) <= 300, f"text is {len(TEXT)} characters"
    assert "\n" not in TEXT and TEXT.count(".") == 1, "exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
