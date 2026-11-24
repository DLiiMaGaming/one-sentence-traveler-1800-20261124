#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (max 200 characters) explaining the modern
internet to a time traveler from 1800, using only things a person from
that year already knows: a road, a post office, a library, a market,
a letter, ink.

Output: /output/entry.txt
"""

import os

SENTENCE = (
    "Picture one road joining every library, post office, and market "
    "on earth, where a letter reaches the far side of the world before "
    "its ink dries, and all mankind walks it together, day and night."
)


# Guards enforce the kit's rules before anything is written: the entry
# must be a single sentence of at most 200 characters. The file is
# only created once every check has passed.
def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1, "must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
