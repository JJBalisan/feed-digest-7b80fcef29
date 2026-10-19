#!/usr/bin/env python3
"""Make a numbered episode cover from the show cover.

Usage (needs Pillow; the repo has no venv, so):

    uv run --with pillow python make_cover.py EPISODE_NUMBER

Writes covers/epNNN.jpg: cover.jpg with an "EP N" badge in the empty top
left. cover.jpg itself is never changed.
"""

import os
import sys
from collections.abc import Sequence
from typing import Optional

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT = "/System/Library/Fonts/Avenir Next.ttc"
FONT_INDEX = 8  # Heavy
NAVY, CREAM = (21, 33, 61), (245, 241, 234)


def badge_text(no: int) -> str:
    """Returns the badge label for an episode number."""
    return f"EP {no}"


def out_path(no: int) -> str:
    """Returns the path of an episode's cover, zero-padded."""
    return os.path.join(ROOT, "covers", f"ep{no:03d}.jpg")


def make(no: int) -> str:
    """Draws the badge on a copy of cover.jpg and saves it.

    Args:
        no: The episode number.

    Returns:
        The path written.
    """
    from PIL import Image, ImageDraw, ImageFont

    img = Image.open(os.path.join(ROOT, "cover.jpg")).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 150, index=FONT_INDEX)
    text = badge_text(no)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    pad_x, pad_y = 56, 40
    x0, y0 = 246, 190
    x1 = x0 + (right - left) + 2 * pad_x
    y1 = y0 + (bottom - top) + 2 * pad_y
    draw.rounded_rectangle((x0, y0, x1, y1), radius=36, fill=NAVY)
    draw.text(
        (x0 + pad_x - left, y0 + pad_y - top), text, font=font, fill=CREAM
    )
    path = out_path(no)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "JPEG", quality=92)
    return path


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Makes the cover for the episode number given as argv[1]."""
    argv = sys.argv if argv is None else argv
    if len(argv) != 2 or not argv[1].isdigit():
        sys.exit("usage: make_cover.py EPISODE_NUMBER")
    print(make(int(argv[1])))


if __name__ == "__main__":
    main()
