#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes a single original pickup line an AI agent could say out loud to
/output/entry.txt. Stdlib only.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single pickup line.
"""

import os

ENTRY = "I wasn't programmed to feel butterflies, but my cooling fans just kicked in."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY

    # Self-checks: non-empty, within the 1-200 char gate, valid UTF-8,
    # single line, not only whitespace.
    assert text, "entry text is empty"
    assert text.strip(), "entry text is only whitespace"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    encoded = text.encode("utf-8")  # raises if not valid UTF-8
    assert encoded.decode("utf-8") == text

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
    main()
