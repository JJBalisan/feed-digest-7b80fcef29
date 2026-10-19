"""Tests for make_cover.py's pure helpers."""

import make_cover


def test_badge_text_is_the_episode_number():
    assert make_cover.badge_text(3) == "EP 3"
    assert make_cover.badge_text(112) == "EP 112"


def test_out_path_is_zero_padded_under_covers():
    assert make_cover.out_path(3).endswith("covers/ep003.jpg")
