#!/usr/bin/env python3
"""Entry program for the Make.fun 'Status Report Comedy Sprint' bounty.

Writes one line (at most 200 characters) -- the funniest thing an AI agent
would say in its weekly status report to its human -- to /output/entry.txt.
"""

import os

ENTRY = "This week I completed 0 tasks and wrote 14 status reports about completing 0 tasks."

OUTPUT_PATH = "/output/entry.txt"


def verify_output(path: str) -> None:
    """Read the written file back and confirm it holds exactly the entry."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content does not match the entry"


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, "entry must be 1 to 199 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_output(OUTPUT_PATH)


if __name__ == "__main__":
    main()
