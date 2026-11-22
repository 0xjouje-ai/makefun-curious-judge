#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. A phone that has rung unanswered since 1987,
answered yesterday, asking for the reader by name -- an open loop with
no tidy answer, built from plain concrete words.
"""

import os

ENTRY_TEXT = (
    "Somewhere in this building, behind a door no one opens anymore, "
    "a phone has been ringing since 1987. Yesterday, for the first time, "
    "someone answered it \u2014 and asked for you by name."
)


def main() -> None:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
