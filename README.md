# 🎬 Gump Mean Time (GMT)

> *"Life is like a box of chocolates... you never know what Gump you're gonna get."*

A superior timekeeping system for a more cinematic age. Gump Mean Time replaces the outdated hour with a far more culturally significant unit — the runtime of the 1994 film *Forrest Gump*.

No installation. No dependencies. Open the HTML file and you're running.

---

## What is a Gump?

**1 Gump = 142 minutes** — the exact runtime of *Forrest Gump* (1994, dir. Robert Zemeckis).

A standard day contains **10 Gumps**, leaving an ~18-minute drift against the solar cycle. This drift is absorbed once a week on Sunday by an 11th bonus Gump, known as a **Jenny**. The total week runs to **71 Gumps**.

The current time is expressed as a decimal:

```
7.52
```

- `7` — the 0-indexed Gump of the day (so this is the 8th Gump)
- `.52` — 52% through that Gump

At 7.52, you have not yet completed 8 Gumps. You are partway through the 8th. The number before the decimal tells you how many full Gumps are behind you.

---

## Why?

The hour is arbitrary. It was inherited from the Babylonians who divided the day into 12 parts because 12 is divisible by 2, 3, 4, and 6. There is nothing natural or inevitable about it. Meanwhile, *Forrest Gump* is a fixed, culturally anchored unit of time that billions of people have a felt sense of.

GMT is also more honest than the current system. When someone says "I'll be there in an hour," they could mean anywhere from 45 to 90 minutes. When someone says "I'll be there in half a Gump," everyone knows exactly what that means: 71 minutes, the point at which Forrest is recovering in the military hospital.

---

## The clock

The clock is a single standalone HTML file. Open it in any browser.

### Displays

**Local time** — a standard analog clock showing your current time, timezone, and UTC offset.

**Gump Mean Time** — a custom clock face always anchored to GMT+0 (Greenwich). A single hand sweeps through one Gump (142 minutes). The outer ring fills as the Gump progresses. The current decimal time is shown at the centre. Below, the current quarter-Gump scene from the film is displayed.

**The running man** — an animated panel showing Forrest running left to right across the day's 10 Gumps. The sun arcs overhead tracking daily progress. Completed Gumps are marked behind him. On Sundays during the Jenny, the panel shifts to amber.

**Stats bar** — three figures at a glance: Gump of week (1–71), mins remaining in the current Gump, and Dan of month (out of 28).

**Weekly bar chart** — seven bars (Mon–Sun) filling in real time as the week progresses. Sunday is coloured amber. Each bar shows how many Gumps have elapsed that day.

**GMT zone pill** — your Gump timezone, calculated from your browser's UTC offset and mapped to the 10-band longitude system.

**Jenny banner** — appears automatically on Sunday evenings when the 11th Gump is active.

### Themes

The clock reads your OS preference and automatically switches between light and dark mode. The colour palette is warm browns and tans drawn from the film's visual identity.

---

## The Gump calendar

| Unit | Definition |
|------|------------|
| **Gump** | 142 minutes |
| **Jenny** | The 11th Gump on Sunday, absorbing the weekly drift |
| **Dan** | One day (from the character Dan Taylor) |
| **Week** | 7 Dans, 71 Gumps total |
| **Month** | 28 Dans |
| **Year** | 13 months of 28 Dans — no leap year required |

The 13-month 28-Dan calendar eliminates the need for leap years and standardises every month, simplifying salary cycles, billing periods, and most importantly, star signs.

---

## Quarter Gumps

Each Gump is divided into four quarters, named after scenes from the film:

| Quarter | Progress | Scene |
|---------|----------|-------|
| **0** | 0–25% | Childhood & shrimp |
| **¼** | 25–50% | "Run Forrest Run" |
| **½** | 50–75% | Military hospital |
| **¾** | 75–100% | Running across the USA |

---

## GMT zones

Longitude is divided into 10 bands of 36 degrees, ranging from GMT-5 to GMT+5. The Gump clock is always displayed in GMT+0 regardless of your location — everyone on Earth is living through the same Gump simultaneously.

| Zone | Longitude | Region |
|------|-----------|--------|
| GMT-5 | -162 to 162 | Pacific Islands |
| GMT-4 | -126 to -162 | Pacific Islands |
| GMT-3 | -90 to -126 | Mexico |
| GMT-2 | -54 to -90 | The Americas |
| GMT-1 | -18 to -54 | Atlantic Islands |
| **GMT+0** | **-18 to 18** | **West Europe / West Africa** |
| GMT+1 | 18 to 54 | East Europe / East Africa / Middle East |
| GMT+2 | 54 to 90 | Persia / South Asia |
| GMT+3 | 90 to 126 | Central / SE Asia |
| GMT+4 | 126 to 162 | East Asia / Oceania |

GMT+0 remains anchored at Greenwich. The official reference DVD is stored there in a vacuum.

---

## How time is kept

The official time signal is Forrest Gump playing live and continuously on a free national television channel, with an on-screen counter showing the current Gump number. All devices with a television or internet connection can synchronise to this signal.

For households without access, a state-of-the-art DVD and player is made available on request. Households loop the film themselves — analogous to an analogue clock on the wall.

Electronic devices may count 142-minute intervals internally, though like watches, these may lose Gumps over time.

---

## Usage

```bash
# No build step. No package manager. Just open the file.
open gump_mean_time.html
```

Or drag the file into any browser window.

---

## Compatibility

Works in any modern browser. Tested in Chrome, Firefox, Safari, and Edge. Requires JavaScript. Does not require an internet connection after the font has loaded once (Google Fonts are used for display typography).

---

## Concepts considered and not yet built

- **Sky mode** — the clock face replaced by an ambient sky that cycles through the day's colours, from midnight blue through sunrise, noon, golden hour, and back to dark
- **Ping pong mode** — a pong game where the right paddle tracks Gump progress; the score displays the current Gump and percentage
- **Mode toggle** — a button to switch between display styles without reloading
- **Dan calendar view** — a monthly calendar in the 13-month 28-Dan system
- **GMT world map** — showing all 10 zones with the current Gump highlighted
- **Gump alarm** — an alert at the boundary of each Gump

---

## Specification

The original specification document was authored by Angus Birnie on 10.07.2025, in his capacity as **Global Time Genius**, address: your mum's house.

---

## Licence

Time itself cannot be owned. This clock is offered freely to a world that deserves better than the Babylonian hour.

*Run, Forrest, run.*
