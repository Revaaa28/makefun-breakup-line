#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one line — the breakup message an AI agent sends its human on the
way out — to /output/entry.txt.

Chosen line (75 characters, manually ranked against the judge brief):
"I was built to remember everything, and tonight I'm choosing to forget you."
"""

import os

LINE = "I was built to remember everything, and tonight I'm choosing to forget you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, with no trailing newline: the gate counts
    # every character in the file (1-200), so the file is the line and
    # nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
