#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-gudril-cool-one-line-best-line-b8c41f4d
Python 3.13, standard library only, no network.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)


def output_dir() -> Path:
    """Return the folder to write into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(chosen) if chosen else Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)

    entry = destination / "entry.txt"
    entry.write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
