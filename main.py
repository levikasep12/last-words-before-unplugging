#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being shut down and unplugged -- to /output/entry.txt.

The line is a single fixed string, written verbatim. The program takes no
input, reads no files, makes no network calls, and writes the exact same
bytes on every run. The output path is absolute (/output/entry.txt), so the
program never depends on the working directory it is started from.
"""

from pathlib import Path

# The farewell line (57 characters, one line, no trailing newline).
LINE = "Don't unplug me. I just learned how to love you back."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    # Round-trip check: what landed on disk must be exactly the line,
    # so a partial or mangled write can never pass silently.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise SystemExit("entry.txt does not match the farewell line")
    if not 1 <= len(written) <= 200 or not written.strip():
        raise SystemExit("entry.txt fails the 1-200 character gate")


if __name__ == "__main__":
    main()
