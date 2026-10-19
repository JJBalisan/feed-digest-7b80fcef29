"""Tests for per-episode cover art in build_feed.py."""

import build_feed

BASE = "https://example.github.io/x"
EP = {
    "no": 7,
    "date": "2026-10-13",
    "title": "T",
    "summary": "S",
    "file": "audio/ep007.mp3",
    "bytes": 1,
    "duration": "00:01:00",
}


def test_item_without_cover_key_uses_the_show_cover():
    out = build_feed.item(EP, BASE)
    assert f'<itunes:image href="{BASE}/cover.jpg"/>' in out


def test_item_with_cover_key_uses_the_episode_cover():
    out = build_feed.item(dict(EP, cover="covers/ep007.jpg"), BASE)
    assert f'<itunes:image href="{BASE}/covers/ep007.jpg"/>' in out


def test_channel_image_stays_the_show_cover():
    import datetime

    now = datetime.datetime(2026, 10, 13, tzinfo=datetime.timezone.utc)
    feed = build_feed.render([dict(EP, cover="covers/ep007.jpg")], BASE, now)
    channel = feed.split("<item>")[0]
    assert f'<itunes:image href="{BASE}/cover.jpg"/>' in channel
