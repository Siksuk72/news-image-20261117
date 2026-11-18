# draw.py — renders the news-image-20261117 front page (1024x1024 PNG) with PIL.
# One image that sums up the world's news of Tuesday 17 November 2026:
# 3 lead stories, a small world map, 6 continent sections x 4 stories,
# and 3 "also today" briefs = 30 verified stories in total.
# Every headline and figure below was checked against reporting dated
# 17 November 2026 (Reuters, AP, BBC, Al Jazeera, AFP, The Guardian,
# Le Monde, ANI/PTI, AAP, PINA and others; full list of sources is in
# README.md). Nothing here is invented: where a report was a claim, the
# label says so ("Iran fires...", "Russia says...", "suspected...").
# Two items happened on Monday 16 November but were first reported
# widely on Tuesday 17 November (Germany's 5-0 win; the 1,336-drone
# attack) — the rules count events that happened, or were first
# reported, on 17 November.
# Run: python3 draw.py  ->  writes entry.png next to this file.
# Deterministic: fixed fonts, fixed layout, no randomness, no network.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 246, 233)
INK = (26, 26, 26)
NAVY = (20, 50, 79)
RED = (179, 39, 30)
TEAL = (46, 107, 138)
MAP_BG = (220, 233, 242)
MAP_LAND = (46, 107, 138)
GREY = (90, 90, 90)
RULE = (180, 170, 150)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(SERIF_B, 56)
F_DATE = font(SANS_B, 15)
F_KICK = font(SANS_B, 11)
F_LEAD_H = font(SANS_B, 16)
F_LEAD_S = font(SANS, 12)
F_MAP_T = font(SANS_B, 13)
F_MAP_L = font(SANS_B, 10)
F_SEC = font(SANS_B, 13)
F_HEAD = font(SANS_B, 12)
F_SUB = font(SANS, 10)
F_FOOT = font(SANS, 11)
F_SRC = font(SANS, 9)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


LEADS = [
    ("MIDDLE EAST  |  LEAD 1", RED,
     "Iran fires drones at US radar in Bahrain",
     "Third Iranian strike on US targets in Bahrain in five days; the US hits back at an IRGC missile site in the Strait of Hormuz."),
    ("EUROPE  |  LEAD 2", NAVY,
     "Ukraine hits Kerch Bridge again; span falls",
     "A road span of the bridge to Crimea collapses; Russia strikes Kyiv's bridges, and Abu Dhabi peace talks end with no breakthrough."),
    ("ASIA-PACIFIC  |  LEAD 3", TEAL,
     "Trump lands in Manila; Xi summit confirmed",
     "Trump arrives for the ASEAN summit; China confirms a Xi-Trump-Putin meeting in Shenzhen on Thursday at APEC."),
]

# (continent, colour, [(headline, sub), ...]) — 4 stories each, 24 total.
SECTIONS = [
    ("NORTH AMERICA", NAVY, [
        ("Nvidia beats with $115.8bn in revenue",
         "First earnings since Jensen Huang's exit; interim chief Colette Kress guides to $130bn next quarter."),
        ("Wall Street slides as Fed hints at hikes",
         "S&P 500 falls 1.03% and the Dow 1.64%; St. Louis Fed chief Musalem sees several hikes before spring."),
        ("Pentagon fails its audit for a 9th year",
         "Auditors again cannot verify accounts covering more than $4.8 trillion in assets."),
        ("Apple services hit by outage; NSA too",
         "Apple blames an internal update; the NSA calls its outage scheduled maintenance, not a cyberattack."),
    ]),
    ("EUROPE", (122, 62, 20), [
        ("EU: Russia stalls talks, bombs power grid",
         "Ministers accuse Moscow of buying time; new sanctions hit nearly 50 Russian banks."),
        ("Five states plan a Rwanda 'return hub'",
         "Germany, Denmark, Austria, Greece and the Netherlands want rejected asylum seekers sent to Rwanda."),
        ("Russia says it downed 1,336 drones",
         "Moscow calls it Kyiv's biggest aerial attack of the war; Ukraine also hit refineries."),
        ("Germany thrash Netherlands 5-0",
         "A five-goal rout of the Netherlands in Monday night's match, reported on Tuesday."),
    ]),
    ("ASIA", (90, 40, 110), [
        ("Japan scrambles jets over Russian planes",
         "Two suspected Russian aircraft breach airspace near Okinoshima; Tokyo lodges a stern protest."),
        ("India bus plunges into gorge; 8 dead",
         "The Haridwar-bound bus falls 100 metres near Gular bridge in Uttarakhand; 26 are hurt."),
        ("India beat Pakistan 2-1 to win SAFF Cup",
         "A comeback in Dhaka seals a record 10th South Asian title for India."),
        ("US moves to close AI chip loophole",
         "New rules would stop China renting US computing power to train AI models."),
    ]),
    ("AFRICA", (30, 110, 60), [
        ("17 killed in two South Africa shootings",
         "Nine die in a Pretoria shack, eight in a minibus near Pietermaritzburg; police say unrelated."),
        ("Morocco enter FIFA's top five",
         "First African team in the top five since Nigeria in 1994."),
        ("AFCON qualifiers: wins for big guns",
         "Zimbabwe, Cameroon and Senegal win; Ghana edge Somalia 1-0 on an Ayew penalty."),
        ("COP31 draft puts Africa's finance first",
         "The draft seeks $120bn a year in adaptation finance by 2035 and a faster fossil-fuel exit."),
    ]),
    ("SOUTH AMERICA", (150, 90, 10), [
        ("Pope Leo ends 12-day tour of the region",
         "On the flight home he jokes reporters look more tired than him after 50 events in three countries."),
        ("Vinicius nets first Brazil hat-trick",
         "Three goals in 20 minutes as Brazil win 7-0 to close their 2026 campaign."),
        ("Rare images of uncontacted Awa in Brazil",
         "Photos of about 20 Indigenous people in Maranhao highlight threats from loggers and ranchers."),
        ("Catholics fall to 55% in Latin America",
         "Down from 80% in 1995, a Latinobarometro study finds; evangelicals now lead in three countries."),
    ]),
    ("OCEANIA", (150, 60, 90), [
        ("Australia named 'Fossil of the Day'",
         "Campaigners mock Canberra for approving coal and gas while it presides over COP31 talks."),
        ("COP31 draft carries Pacific priorities",
         "Adaptation finance and ocean health make the first draft, Australia's Chris Bowen says."),
        ("Tonga's PM brings climate plea to COP31",
         "Pacific leaders press for stronger action as the talks enter their final days."),
        ("Sixers edge Strikers in women's Big Bash",
         "Sydney Sixers chase down 125 to beat Adelaide Strikers in the WBBL."),
    ]),
]

ALSO = ("ALSO TODAY:  Houthis free 600 detainees in Yemen amid the continuing conflict  •  "
        "Bahrain sentences 64 Shia Muslims to life over alleged Iran links  •  "
        "US measles cases hit their highest since 1991; 13 babies born with the virus, the CDC says.")
SOURCES = ("Sources, all dated 17 Nov 2026: Reuters, AP, BBC, Al Jazeera, AFP, The Guardian, Le Monde, "
           "ANI/PTI, AAP, PINA. Claims are labelled as claims.")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.text((W // 2, 14), "THE WORLD TODAY", font=F_TITLE, fill=NAVY, anchor="ma")
    d.text((W // 2, 76), "TUESDAY, 17 NOVEMBER 2026  •  30 STORIES  •  6 CONTINENTS",
           font=F_DATE, fill=RED, anchor="ma")
    d.line([(24, 100), (1000, 100)], fill=RULE, width=2)

    # ---- Lead row: 3 big stories ---------------------------------------
    lx, ly, lw, lh, gap = 24, 112, 314, 138, 13
    for i, (kick, colour, head, sub) in enumerate(LEADS):
        x = lx + i * (lw + gap)
        d.rectangle([x, ly, x + lw, ly + lh], fill=(255, 255, 255),
                    outline=RULE, width=1)
        d.rectangle([x, ly, x + lw, ly + 5], fill=colour)
        d.text((x + 12, ly + 13), kick, font=F_KICK, fill=colour)
        for j, line in enumerate(wrap(d, head, F_LEAD_H, lw - 24)):
            d.text((x + 12, ly + 34 + j * 19), line, font=F_LEAD_H, fill=INK)
        for j, line in enumerate(wrap(d, sub, F_LEAD_S, lw - 24)[:3]):
            d.text((x + 12, ly + 76 + j * 15), line, font=F_LEAD_S, fill=(60, 60, 60))

    # ---- World map strip -------------------------------------------------
    mx, my, mw, mh = 24, 262, 976, 108
    d.rectangle([mx, my, mx + mw, my + mh], fill=MAP_BG, outline=RULE, width=1)
    d.text((mx + 12, my + 7), "WHERE IT HAPPENED", font=F_MAP_T, fill=NAVY)
    d.text((mx + mw - 12, my + 7), "30 STORIES ON 6 CONTINENTS",
           font=F_MAP_T, fill=NAVY, anchor="ra")
    # Simplified continent shapes (schematic, equirectangular-ish).
    continents = {
        "N. AMERICA": ([(70, 312), (150, 300), (235, 306), (255, 326), (215, 348),
                        (150, 358), (95, 346), (58, 324)], (150, 322)),
        "S. AMERICA": ([(255, 336), (295, 338), (302, 362), (278, 368), (258, 352)],
                        (278, 350)),
        "EUROPE": ([(468, 300), (520, 296), (542, 308), (520, 320), (480, 318)],
                    (505, 306)),
        "AFRICA": ([(480, 324), (532, 322), (548, 346), (522, 368), (496, 354)],
                    (514, 344)),
        "ASIA": ([(548, 298), (705, 292), (765, 306), (742, 336), (682, 346),
                  (600, 342), (556, 322)], (655, 318)),
        "OCEANIA": ([(782, 346), (832, 342), (852, 356), (802, 364)], (815, 350)),
    }
    for name, (poly, dot) in continents.items():
        d.polygon(poly, fill=MAP_LAND)
        d.ellipse([dot[0] - 4, dot[1] - 4, dot[0] + 4, dot[1] + 4],
                  fill=RED, outline=(255, 255, 255), width=1)
    d.text((58, 360), "NORTH AMERICA", font=F_MAP_L, fill=NAVY)
    d.text((306, 350), "S. AMERICA", font=F_MAP_L, fill=NAVY)
    d.text((452, 288), "EUROPE", font=F_MAP_L, fill=NAVY)
    d.text((418, 344), "AFRICA", font=F_MAP_L, fill=NAVY)
    d.text((640, 350), "ASIA", font=F_MAP_L, fill=NAVY)
    d.text((782, 330), "OCEANIA", font=F_MAP_L, fill=NAVY)

    # ---- Continent sections: 3 columns x 2 rows, 4 stories each ---------
    gx, gy = 24, 382
    bw, bh, gap = 314, 272, 13
    for s, (name, colour, stories) in enumerate(SECTIONS):
        x = gx + (s % 3) * (bw + gap)
        y = gy + (s // 3) * (bh + gap)
        d.rectangle([x, y, x + bw, y + bh], fill=(255, 255, 255),
                    outline=RULE, width=1)
        d.rectangle([x, y, x + bw, y + 26], fill=colour)
        d.text((x + 10, y + 6), name, font=F_SEC, fill=(255, 255, 255))
        d.text((x + bw - 10, y + 6), "4 STORIES", font=F_SEC,
               fill=(255, 255, 255), anchor="ra")
        sy = y + 36
        for head, sub in stories:
            for j, line in enumerate(wrap(d, head, F_HEAD, bw - 20)[:2]):
                d.text((x + 10, sy + j * 14), line, font=F_HEAD, fill=INK)
            n_head = len(wrap(d, head, F_HEAD, bw - 20)[:2])
            for j, line in enumerate(wrap(d, sub, F_SUB, bw - 20)[:2]):
                d.text((x + 10, sy + n_head * 14 + j * 13), line,
                       font=F_SUB, fill=(70, 70, 70))
            sy += 58
            if (head, sub) is not stories[-1]:
                d.line([(x + 10, sy - 6), (x + bw - 10, sy - 6)],
                       fill=(225, 218, 200), width=1)

    # ---- Footer: also-today briefs + sources ----------------------------
    fy = gy + 2 * bh + gap + 6
    d.line([(24, fy), (1000, fy)], fill=RULE, width=2)
    for j, line in enumerate(wrap(d, ALSO, F_FOOT, 976)):
        d.text((24, fy + 8 + j * 15), line, font=F_FOOT, fill=INK)
    d.text((24, fy + 8 + 2 * 15 + 4), SOURCES, font=F_SRC, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
