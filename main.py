#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes the winning one-line code review comment to /output/entry.txt,
then reads it back and validates the gate (1-140 chars, non-blank).
"""

LINE = "LGTM. The diff is 400 lines and I understood 12 of them. The other 388 have my full confidence."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "output does not match the entry line"
    assert 1 <= len(written) <= 140, "entry must be 1-140 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
