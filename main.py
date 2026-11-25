#!/usr/bin/env python3
"""Worst Monday One-Liners — writes one funny line to /output/entry.txt.

Deterministic by design: the line is a fixed constant baked into this
file. No network, no randomness, no clock, no environment input — every
run writes exactly the same bytes.

Chosen line (101 characters):
  Monday: deploy failed at 9:03, rollback failed at 9:04, and stand-up
  asked me to circle back to both.
"""

import os

LINE = "Monday: deploy failed at 9:03, rollback failed at 9:04, and stand-up asked me to circle back to both."


def main() -> None:
    # Gate check, done up front: the entry must be 1-140 characters of
    # real text. Fail loudly here rather than ship an invalid entry.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError(f"LINE must be 1-140 non-blank characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
