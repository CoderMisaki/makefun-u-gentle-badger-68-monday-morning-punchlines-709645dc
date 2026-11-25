#!/usr/bin/env python3
"""Monday Morning Punchlines: writes one joke about Monday mornings
to /output/entry.txt (1-200 characters). Standard library only."""

import os

JOKE = "Monday morning: my alarm filed for overtime, my bed filed for custody, and I lost both cases before my first coffee."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
