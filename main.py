#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one office joke (max 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
"""

import os
import sys

JOKE = (
    "The office printer has been out of toner since March. "
    "I filed a ticket, then a second ticket, "
    "and now the printer has filed a ticket about me."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(JOKE) <= 200:
        print(f"joke is {len(JOKE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if JOKE != JOKE.strip():
        print("joke has leading/trailing whitespace", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
