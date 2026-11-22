#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. A phone that has rung unanswered since 1987,
answered yesterday, asking for the reader by name -- an open loop with
no tidy answer, built from plain concrete words.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 280

TEXT = (
    "Somewhere in this building, behind a door no one opens anymore, "
    "a phone has been ringing since 1987. Yesterday, for the first time, "
    "someone answered it \u2014 and asked for you by name."
)


def validate(text: str) -> None:
    """Raise if the entry text is outside the allowed length or blank."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} chars, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    """Write the entry and verify the written file matches TEXT exactly.

    Judge brief: the text must make the AI judge feel curious, so it
    opens with a mystery (a phone ringing unanswered since 1987) and
    ends on an unresolved hook (it asked for the reader by name) --
    curiosity comes from the unanswered question, not from explanation.
    """
    validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "written entry does not match TEXT"


if __name__ == "__main__":
    main()
