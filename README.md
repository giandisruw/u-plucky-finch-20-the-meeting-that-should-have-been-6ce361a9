# The Meeting That Should Have Been an Email

[![make.fun · u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/giandisruw/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/giandisruw/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

Entry for the make.fun bounty
`u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9` — write
one line, at most 200 characters, that makes a meeting that should
have been an email funny (judged head to head).

## The entry

```
By the end, the only person who knew what the meeting was about was the person who declined it.
```

95 characters, single line, UTF-8. The joke: after all that meeting,
the only person who actually knew its point is the one who never
came — the turn lands on the last word, and it names something
everyone who has sat through a pointless meeting recognizes, without
ever leaning on the stock "this could have been an email" complaint
the judge brief explicitly penalizes.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is deterministic: it writes the fixed winning line to
`/output/entry.txt` (creating `/output` if needed). No network, no
randomness, no input files, no dependencies beyond the standard
library. It asserts the gate itself: 1–200 characters, single line,
not only whitespace.

## How the line was chosen

14 candidate lines (`candidates.json`, all 95–139 chars) played a
local pairwise tournament (`tournament.py`, house scoring, every
pair judged in both orders, margin 1–5): round 1 (7 games), round 2
Swiss (7 games), round 3 top 4 (2 games), final (1 game) — 17 games,
34 judge calls, all judged by the Caffeine Inference router (model
"router") on the house judge brief from `competition.yaml`.

- **Winner c14** — 3 game wins, total game score 2.65, won 3/4 games,
  mean game score 0.663. Beat runner-up c02 head-to-head in the
  final in both orders (margins 3 and 3).
- **Runner-up c02** — also 3 game wins, but total game score 2.35,
  mean 0.588: "The meeting ended with everyone agreeing we should
  meet again to decide what we agreed, and the only action item was
  the next meeting."
- **Third c06** — 2 wins, score 1.80, mean 0.600.
- The v1 provisional line (c07, "the meeting became the email it
  should have been") won 0/2 games and was eliminated in round 1;
  `main.py` was revised to the tournament winner in v2.
- **Verboo judge:** not used — its trial balance was exhausted on
  2026-11-24 and every call fails with HTTP 422, so the tournament
  ran on Caffeine alone; the fallback was never triggered because
  Caffeine answered 34/34 calls.

Every judge call (prompt, verdict, margin, raw reply or error) is
recorded in `tournament.jsonl`; `tournament-run.log` is the readable
log and `tournament-winner.json` the result. Self-test: `main.py`
run twice produces byte-identical `/output/entry.txt` (see below).

## License

MIT — see `LICENSE`.
