#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original one-line review of planet Earth, left by an alien
tourist, to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for
local testing). Python 3, standard library only. Deterministic: the
same line on every run, no randomness, no time, no network.
"""

import os

REVIEW = (
    "Visited Earth. The locals spend all day staring at glowing "
    "rectangles while the whole sky puts on a free show above them. "
    "2/5 \u2014 wasted view."
)


def main() -> None:
    # Guard the bounty gate: one line, 1-200 characters, no newline.
    assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
    assert "\n" not in REVIEW and "\r" not in REVIEW, "review must be one line"
    assert REVIEW.strip(), "review must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
