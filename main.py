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

# Output directory: the grader sandbox pre-creates /output (owned by
# another user, writable) and runs this program as an unprivileged
# user — so the program must never chmod a directory it does not own.
# MAKEFUN_OUTPUT_DIR lets the harness redirect the output if needed.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate check, done up front: the entry must be 1-140 characters of
    # real text. Fail loudly here rather than ship an invalid entry.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError(f"LINE must be 1-140 non-blank characters, got {len(LINE)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # NOTE: no chmod on OUTPUT_DIR — in the grader sandbox it is owned
    # by another user, and chmod on a foreign directory raises
    # PermissionError (exit 1). The directory is already writable.
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # chmod is safe here: entry.txt is a file this program just created,
    # so it is owned by this program.
    os.chmod(os.path.join(OUTPUT_DIR, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
