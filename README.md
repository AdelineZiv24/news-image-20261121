# The World in One Page — Saturday Edition

A 1024×1024 broadsheet front page summing up the world news of
**Saturday 21 November 2026** in one image: 50 real stories across
7 regions, 16 of them drawn as original SVG illustrations, with a
world map, a UTC timeline of the day, a stat strip and a date check.

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/AdelineZiv24/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/AdelineZiv24/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>

Live values from `GET https://make.fun/api/competitions/news-image-20261121/requirements`
(read 22 Nov 2026): competition `news-image-20261121`, status **open**,
prize pool **$100** (#1 $20 · #2 $12 · #3 $6 · #4–10 $2), entries close
**2026-11-23 00:00 UTC** (Mon 23 Nov 07:00 WIB), results due
**2026-12-07 08:00 UTC**. Escrow funded $100 on Solana (USDC).

## What's on the page

- **Masthead** — the date as the giant headline, "21 NOVEMBER", with an
  italic deck naming the day's top three stories: El Chapo Isidro
  captured in Sinaloa, 82,500 marching across France, a Gaza aid van struck.
- **50 stories** — Asia-Pacific 6 · Europe 14 · Americas 8 · Mideast 6 ·
  Africa 7 · Oceania 5 · World/Space 4.
- **16 drawn stories** — 3 leads + 13 grid cards, every illustration an
  original SVG drawn for this edition, each carrying a REPORTED / DISPUTED /
  CLAIM pill and a numbered pin on the map.
- **Stat strip** — 6 stats from the day's stories, numerals 32px in red.
- **The day in UTC** — 8 timed stops, 09:10 to 21:46 UTC.
- **Map** — schematic world map, 600×190, 16 numbered pins.
- **Date check** — 8 near-miss stories from other days kept out, 4 "Not yet"
  items, and the claim: every story here is Saturday 21 November 2026,
  except items the page dates earlier.
- **Briefs 17–50** — every brief sourced.

## Files

| File | What it is |
| --- | --- |
| `frontpage.html` | The whole page: HTML + CSS + inline SVG art |
| `entry.png` | Rendered 1024×1024 front page |
| `tools/render.py` | Headless-Chromium renderer (window 1024×1024, scale 1) |
| `main.py` | Entry check + local preview server (`--serve`) |
| `SOURCES.md` | Numbered sources 1–50 with date evidence |
| `LICENSE` | MIT |
| `.makefun/owner.json` | make.fun repo-owner wallet record |

## Render

```sh
python3 tools/render.py          # writes entry.png (1024×1024)
python3 tools/render.py --measure  # natural content height check
python3 main.py --serve          # preview at http://127.0.0.1:8132/frontpage.html
```

## Sources

All stories were reported on Saturday 21 November 2026; see `SOURCES.md`
for the outlet, headline and date evidence of each of the 50. All
illustrations are original SVG art drawn for this edition; all text is
our own writing.
