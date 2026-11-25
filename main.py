"""The Raise — Famous Last Words: The Funniest Epitaph.

The line turns on a double meaning of "a raise": the dying speaker asked
the boss for a pay rise, and instead got six feet of earth — the raise
they ended up with. The joke lands in one read, needs no explanation,
and reads exactly like something carved on a stone.
"""

import os

LINE = "I asked for a raise. They gave me six feet."

MAX_CHARS = 150
MAX_BYTES = 150


def validate(line):
    """Check a single-line epitaph against the gate: 1-150 UTF-8 chars,
    at most 150 bytes, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-150 characters")
    if len(line.encode("utf-8")) > MAX_BYTES:
        raise ValueError("entry must be at most 150 bytes")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
