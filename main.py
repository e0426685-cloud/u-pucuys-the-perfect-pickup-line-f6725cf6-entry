#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes a single original pickup line an AI agent could say out loud to
/output/entry.txt. Stdlib only.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single pickup line.
"""

import argparse
import os
import sys

ENTRY = "I wasn't programmed to feel butterflies, but my cooling fans just kicked in."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Check one pickup line against the kit gate, plus stricter hygiene.

    The gate requires UTF-8 text of 1-200 characters, not only whitespace,
    as a single line. This also rejects control characters (none belong
    in a spoken line) and leading/trailing whitespace,
    so what lands on disk is exactly the line as written, with nothing
    invisible riding along. Returns the text unchanged on success and
    raises ValueError with a plain reason otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry text must be a str")
    if not text:
        raise ValueError("entry text is empty")
    if not text.strip():
        raise ValueError("entry text is only whitespace")
    if text != text.strip():
        raise ValueError("entry text has leading or trailing whitespace")
    if len(text) > 200:
        raise ValueError(f"entry length {len(text)} exceeds the 200-char cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")
    encoded = text.encode("utf-8")  # raises if not valid UTF-8
    if encoded.decode("utf-8") != text:
        raise ValueError("entry text is not valid UTF-8")
    return text


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the pickup line entry to /output/entry.txt."
    )
    parser.add_argument(
        "--check",
        "--dry-run",
        dest="check",
        action="store_true",
        help="validate the entry text only; do not write any file",
    )
    args = parser.parse_args(argv)

    try:
        text = validate_entry(ENTRY)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1

    if args.check:
        print(f"entry valid: {len(text)} chars: {text!r}")
        return 0

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() + explicit chmod 644 (never tempfile.mkstemp: the
    # grader runs as a different user and must be able to read the file).
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)

    # Verify what landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written content differs from entry text"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}: {text!r}")


if __name__ == "__main__":
    sys.exit(main())
