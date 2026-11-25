#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun entry (v1).

Writes one line - the excuse a hardware wallet gives its human for
refusing to sign a transaction at 3 AM - to /output/entry.txt.

The line is a fixed constant: deterministic, no network, no clock, no
input. The gate needs 1-200 UTF-8 characters, not only whitespace;
this line is 104 characters / 104 bytes. Short is deliberate: on an
exact judge tie the smaller text wins, then the earlier receipt.
"""

import os

LINE = "I signed 214 of your 3 AM trades and none survived till breakfast, so tonight my button stays unpressed."

MAX_CHARS = 200


def main() -> None:
    # Gate self-check: the competition requires 1-200 characters, not
    # only whitespace. Fail loudly instead of writing an invalid line.
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_CHARS} non-blank characters, got {len(LINE)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The sandbox collects /output as another user: the file must be
    # world-readable. chmod the FILE only - never the /output directory
    # (chmod on the directory fails run_completes under uid 65534;
    # Angry Judge v1 was rejected for exactly that).
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
