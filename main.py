#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one joke (at most 200 characters, single line, UTF-8) to
/output/entry.txt. Deterministic: the line below is the winner of the
local pairwise tournament in tournament.py (see tournament.jsonl and
tournament-run.log). No network, no randomness, no input files.

Tournament result (2026-11-25, 17 games, house scoring, both orders,
Caffeine router judge, 34/34 calls OK):
  winner c14 — 3 game wins, total game score 2.65; beat runner-up c02
  head-to-head in the final (both orders, margins 3 and 3).
  Caffeine router judge: c14 won 3/4 games, mean game score 0.663.
  Runner-up c02 also won 3/4 games but scored lower (2.35, mean 0.588).
  The v1 provisional line (c07) won 0/2 games and was eliminated in
  round 1, so this file was revised to the tournament winner in v2.
  Verboo was not used as a judge: its trial balance was exhausted on
  2026-11-24 and every call fails with HTTP 422; see tournament.py.
"""

import os

ENTRY = (
    "By the end, the only person who knew what the meeting was about "
    "was the person who declined it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
