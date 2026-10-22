# Marked Read (unlisted)

Daily spoken digest, narrated by the `daily-feed-podcast` scheduled task.
The repo is public only because free GitHub Pages needs that; the name is
random and the page carries noindex. Treat the feed URL as a secret.

This repo holds data only: `show.json` (the show's feed settings),
`episodes.json`, `feed.xml`, covers and audio. The task publishes with the
shared kit (`podcast-kit`):
`~/.local/share/threshold-and-bar/bin/publish_episode.py` adds an episode, and
`python3 ~/.local/share/threshold-and-bar/bin/build_feed.py .` rebuilds `feed.xml` by hand.
