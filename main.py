#!/usr/bin/env python3
"""One Sentence, One Journey — make.fun bounty entry.

Writes a complete story about a journey in exactly one sentence
(at most 300 characters) to /output/entry.txt: she sells the house,
books a one-way ticket under her mother's name by mistake, and by
the border — where a guard mispronounces it twice — she has stopped
correcting him, travelling lighter than she ever had.

Deterministic: the text is a constant, so every run writes the same
bytes. No network.
"""
import os

TEXT = (
    "She sold the house, booked a one-way ticket under her mother's "
    "name by mistake, and by the border — where a guard mispronounced "
    "it twice — she'd stopped correcting him, because the woman in "
    "seat 14 was travelling lighter than she ever had."
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
