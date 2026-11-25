"""One-line joke excusing a missed deadline.

Writes the entry to /output/entry.txt (creating /output if needed).
Stdlib only, deterministic: the same line every run.
"""

import os
import sys

# The joke's turn: the excuse starts as a plausible tech glitch (a calendar
# syncing to a nonexistent timezone) and the punch reframes "late" as
# "early, on the wrong planet" — the deadline wasn't missed, it was
# relocated somewhere unreachable. One sentence, punch lands at the end.
JOKE = (
    "My calendar moved the deadline to a timezone that doesn't exist yet, "
    "so technically I'm early \u2014 just not on this planet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = JOKE.strip()
    if not line:
        print("error: joke is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(f"error: joke must be 1-200 characters, got {len(line)}",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
