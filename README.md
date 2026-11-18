# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Siksuk72/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Siksuk72/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up the world's news of Tuesday 17 November 2026:
a one-page newspaper front page drawn programmatically with Python PIL
(`draw.py`), copied to `/output/entry.png` by `main.ts` (Node 22, stdlib
only). Drawing in code — not image generation — means every word is
spelled correctly and stays legible at ~300 px.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=hz26ha21&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>

## Layout

- Masthead "THE WORLD TODAY" + "TUESDAY, 17 NOVEMBER 2026 • 30 STORIES • 6 CONTINENTS"
- 3 lead stories: Iran fires drones at a US radar in Bahrain; Ukraine hits the Kerch Bridge again; Trump lands in Manila with a Xi-Trump-Putin summit confirmed.
- Schematic world map ("WHERE IT HAPPENED") with a marker per continent.
- 6 continent sections × 4 stories each (24 stories).
- "ALSO TODAY" strip with 3 more briefs. Total: 30 stories.

## The 30 stories (all reported on 17 Nov 2026)

### Leads
1. Iran fires drones at a US radar in Bahrain; the US hits back at an IRGC missile site in the Strait of Hormuz — Reuters, AP
2. Ukraine hits the Kerch Bridge again and a road span collapses; Russia strikes Kyiv's bridges; Abu Dhabi peace talks end with no breakthrough — BBC, Al Jazeera
3. Trump lands in Manila for the ASEAN summit; China confirms a Xi-Trump-Putin meeting in Shenzhen on Thursday at APEC — AP

### North America
4. Nvidia beats with $115.8bn in revenue, first earnings since Jensen Huang's exit; interim chief Colette Kress guides to $130bn — CNBC
5. Wall Street slides as the Fed hints at hikes: S&P 500 down 1.03%, Dow down 1.64%; St. Louis Fed chief Musalem sees several hikes before spring — CNBC, AP
6. Pentagon fails its financial audit for a 9th straight year; auditors cannot verify accounts covering $4.8tn in assets
7. Apple services hit by an outage after an internal update; the NSA's network also degraded — CNBC

### Europe
8. EU accuses Russia of stalling peace talks while bombing Ukraine's power grid; new sanctions hit nearly 50 Russian banks — AP
9. Five European states plan a Rwanda "return hub" for rejected asylum seekers: Germany, Denmark, Austria, Greece, Netherlands — AP
10. Russia says it downed 1,336 Ukrainian drones, Kyiv's biggest aerial attack of the war — AP
11. Germany thrash the Netherlands 5-0 (match Monday night, reported Tuesday)

### Asia
12. Japan scrambles jets as two suspected Russian aircraft breach its airspace near Okinoshima; Tokyo lodges a stern protest — Reuters
13. India bus plunges into a gorge in Uttarakhand; at least 8 dead, 26 hurt — ANI/PTI
14. India beat Pakistan 2-1 to win the SAFF Championship in Dhaka, a record 10th title
15. US moves to close the AI chip loophole letting China rent US computing power

### Africa
16. 17 killed in two South Africa mass shootings: nine in a Pretoria shack, eight in a minibus near Pietermaritzburg; police say unrelated — AP, BBC
17. Morocco enter FIFA's top five, the first African team since Nigeria in 1994
18. AFCON qualifiers: Zimbabwe, Cameroon and Senegal win; Ghana edge Somalia 1-0 on an Ayew penalty
19. COP31 draft puts Africa's climate finance first: $120bn a year in adaptation finance by 2035 — COP31 Presidency draft

### South America
20. Pope Leo ends his 12-day South America tour; on the flight home he jokes reporters look more tired than him — Reuters
21. Vinicius nets his first Brazil hat-trick, three goals in 20 minutes in a 7-0 win
22. Rare images of uncontacted Awa people in Brazil's Amazon highlight threats from loggers and ranchers — Reuters
23. Catholics fall to 55% in Latin America, down from 80% in 1995, a Latinobarometro study finds — Christian Post

### Oceania
24. Australia named "Fossil of the Day" at COP31 while presiding over the talks — Climate Action Network
25. COP31 draft carries Pacific priorities: adaptation finance and ocean health — PINA
26. Tonga's PM brings the Pacific climate plea to COP31
27. Sydney Sixers chase down 125 to beat Adelaide Strikers in the women's Big Bash

### Also today
28. Houthis free 600 detainees in Yemen amid the continuing conflict
29. Bahrain sentences 64 Shia Muslims to life over alleged Iran links
30. US measles cases hit their highest since 1991; 13 babies born with the virus, the CDC says

## Method & verification

- Research: web search on 18 Nov 2026 against reporting dated 17 Nov 2026;
  every story above traces to at least one named reputable source. Claims
  are labelled as claims ("Russia says…", "suspected Russian aircraft…").
  No story was invented; uncertain items were dropped, not guessed.
- Two items happened on Monday night but were first reported widely on
  Tuesday 17 November (Germany's 5-0 win; the 1,336-drone attack), which
  the rules count ("happened, or first reported, on 17 November").
- Rendering: `python3 draw.py` → `entry.png` (1024×1024 PNG, 152,600 bytes,
  sha256 `542e05038bc4d1fa18ae9b0eadaed984295478cb13dc8e5944c1876a77042743`).
  DejaVu fonts, fixed layout, no randomness, no network — re-runs are
  byte-identical. Checked visually at full size and at 300 px: masthead,
  date and lead headlines stay legible.
- Program: `main.ts` copies `entry.png` to `/output/entry.png`; two runs
  write byte-identical output.

## License

MIT (see LICENSE).
