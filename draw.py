#!/usr/bin/env python3
"""Draw the front page for news-image-20261117: one image summing up the
world news of Tuesday 17 November 2026. Deterministic: same input, same PNG
bytes, every run. Run: python3 draw.py  (writes entry.png next to itself)."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (248, 242, 223)
INK = (24, 24, 24)
NAVY = (31, 58, 95)
RED = (163, 31, 31)
SKY = (214, 230, 238)
GREY = (90, 90, 90)
LINE = (120, 110, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines fitting max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped text, return the y just below the last line."""
    for ln in wrap(draw, text, fnt, max_w):
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


MASTHEAD = "THE WORLD TODAY"
DATELINE = "TUESDAY, 17 NOVEMBER 2026  \u2022  30 STORIES  \u2022  6 CONTINENTS"

LEADS = [
    ("MIDDLE EAST  |  LEAD 1", RED,
     "Iran fires drones at US radar in Bahrain",
     "Third Iranian strike on US targets in Bahrain in five days; the US "
     "hits back at an IRGC missile site."),
    ("EUROPE  |  LEAD 2", NAVY,
     "Ukraine hits Kerch Bridge again; span falls",
     "A road span of the bridge to Crimea collapses; Russia strikes Kyiv's "
     "bridges as Abu Dhabi talks end in stalemate."),
    ("ASIA-PACIFIC  |  LEAD 3", (38, 90, 120),
     "Trump lands in Manila; Xi summit confirmed",
     "Trump arrives for the ASEAN summit; China confirms a Xi-Trump-Putin "
     "meeting in Shenzhen on Thursday."),
]

SECTIONS = [
    ("NORTH AMERICA", NAVY, [
        ("Nvidia beats with $115.8bn in revenue",
         "First earnings since Huang's exit; interim CEO Colette Kress "
         "guides to $130bn next quarter."),
        ("Wall Street slides as Fed hints at hikes",
         "S&P 500 falls 1.03% and the Dow 1.64%; St. Louis Fed chief "
         "Musalem sees several hikes before spring."),
        ("Pentagon fails its audit for a 9th year",
         "Auditors again cannot verify accounts covering more than "
         "$4.8 trillion in assets."),
        ("Apple services hit by outage; NSA too",
         "Apple blames an internal update; the NSA calls its outage "
         "scheduled maintenance, not a cyberattack."),
    ]),
    ("EUROPE", (122, 62, 20), [
        ("EU: Russia stalls talks, bombs power grid",
         "Europe accuses Moscow of buying time; new sanctions hit nearly "
         "50 Russian banks."),
        ("Five states plan a Rwanda \u2018return hub\u2019",
         "Germany, Denmark, Austria, Greece and the Netherlands want "
         "rejected asylum seekers sent to Rwanda."),
        ("Russia says it downed 1,336 drones",
         "Moscow calls it Kyiv's biggest aerial attack of the war; "
         "Ukraine also hit refineries."),
        ("Germany thrash Netherlands 5-0",
         "A five-goal rout of the Netherlands in Monday night's match, "
         "reported on Tuesday."),
    ]),
    ("ASIA", (96, 44, 122), [
        ("Japan scrambles jets over Russian planes",
         "Two suspected Russian aircraft breach airspace near Okinoshima; "
         "Tokyo lodges a stern protest."),
        ("India bus plunges into gorge; 8 dead",
         "The Haridwar-bound bus falls 100 metres near Gular bridge in "
         "Uttarakhand; 26 are hurt."),
        ("India beat Pakistan 2-1 to win SAFF Cup",
         "A comeback in Dhaka seals a record 10th South Asian title "
         "for India."),
        ("US moves to close AI chip loophole",
         "New rules would stop China renting US computing power to "
         "train AI models."),
    ]),
    ("AFRICA", (24, 110, 62), [
        ("17 killed in two South Africa shootings",
         "Nine die in a Pretoria shack, eight in a minibus near "
         "Pietermaritzburg; police say unrelated."),
        ("Morocco enter FIFA's top five",
         "First African team in the top five since Nigeria in 1994."),
        ("AFCON qualifiers: wins for big guns",
         "Zimbabwe, Cameroon and Senegal win; Ghana edge Somalia 1-0 "
         "on an Ayew penalty."),
        ("COP31 draft puts Africa's finance first",
         "The draft seeks $120bn a year in adaptation finance by 2035 "
         "and a faster fossil-fuel exit."),
    ]),
    ("SOUTH AMERICA", (122, 88, 18), [
        ("Pope Leo ends 12-day tour of the region",
         "On the flight home he jokes reporters look more tired than "
         "him after 50 events in three countries."),
        ("Vinicius nets first Brazil hat-trick",
         "Three goals in 20 minutes as Brazil win 7-0 to close their "
         "2026 campaign."),
        ("Rare images of uncontacted Awa in Brazil",
         "Photos of about 20 Indigenous people in Maranhao highlight "
         "threats from loggers and ranchers."),
        ("Catholics fall to 55% in Latin America",
         "Down from 80% in 1995, a Latinobarometro study finds; "
         "evangelicals now lead in three countries."),
    ]),
    ("OCEANIA", (128, 52, 84), [
        ("Australia named \u2018Fossil of the Day\u2019",
         "Campaigners mock Canberra for approving coal and gas while it "
         "presides over COP31 talks."),
        ("COP31 draft carries Pacific priorities",
         "Adaptation finance and ocean health make the first draft, "
         "Australia's Chris Bowen says."),
        ("Tonga's PM brings climate plea to COP31",
         "Pacific leaders press for stronger action as the talks enter "
         "their final days."),
        ("Sixers edge Strikers in women's Big Bash",
         "Sydney Sixers chase down 125 to beat Adelaide Strikers in "
         "the WBBL."),
    ]),
]

ALSO = ("ALSO TODAY:  Houthis free 600 detainees in Yemen amid the "
       "continuing conflict  \u2022  Bahrain sentences 64 Shia Muslims to life over "
       "alleged Iran links  \u2022  US measles cases hit their highest since 1991; "
       "13 babies born with the virus, the CDC says.")
SOURCES = ("Sources, all dated 17 Nov 2026: Reuters, AP, BBC, Al Jazeera, AFP, "
           "The Guardian, Le Monde, ANI/PTI, AAP, PINA. Claims are labelled "
           "as claims.")


def draw_lead(draw, x, y, w, h, kicker, color, headline, deck):
    draw.rectangle([x, y, x + w, y + h], outline=GREY, width=1)
    draw.rectangle([x, y, x + w, y + 3], fill=color)
    ty = y + 12
    draw.text((x + 10, ty), kicker, font=SANS_B(12), fill=color)
    ty += 20
    ty = para(draw, x + 10, ty, headline, SANS_B(20), w - 20, 24)
    para(draw, x + 10, ty + 4, deck, SANS(13), w - 20, 17, color=(60, 60, 60))


def draw_map(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=SKY, outline=GREY, width=1)
    draw.text((x + 10, y + 6), "WHERE IT HAPPENED", font=SANS_B(13), fill=NAVY)
    draw.text((x + w - 250, y + 6), "30 STORIES ON 6 CONTINENTS",
              font=SANS_B(13), fill=NAVY)
    sea = (44, 94, 122)
    # Schematic blobs: rough continent shapes in the lower two-thirds so
    # they never touch the strip titles; each label sits under its blob.
    blobs = [
        ([(40, 30), (130, 22), (200, 30), (190, 58), (110, 66), (55, 54)],
         "NORTH AMERICA", (105, 70)),
        ([(215, 52), (240, 44), (256, 56), (242, 70), (222, 66)],
         "S. AMERICA", (212, 74)),
        ([(430, 26), (490, 20), (515, 32), (490, 44), (445, 40)],
         "EUROPE", (432, 52)),
        ([(470, 50), (510, 48), (525, 66), (500, 82), (478, 70)],
         "AFRICA", (550, 64)),
        ([(580, 24), (700, 20), (800, 32), (770, 56), (640, 60), (590, 44)],
         "ASIA", (665, 64)),
        ([(815, 58), (855, 52), (872, 64), (840, 74), (820, 68)],
         "OCEANIA", (812, 78)),
    ]
    dots = [(120, 44), (236, 58), (472, 32), (498, 64), (688, 40), (844, 64)]
    for pts, label, (lx, ly) in blobs:
        pts = [(x + px, y + py) for px, py in pts]
        draw.polygon(pts, fill=sea)
        draw.text((x + lx - 20, y + ly), label, font=SANS_B(10), fill=INK)
    for dx, dy in dots:
        draw.ellipse([x + dx - 4, y + dy - 4, x + dx + 4, y + dy + 4],
                     fill=RED, outline=(255, 255, 255), width=1)


def draw_section(draw, x, y, w, h, name, color, stories):
    draw.rectangle([x, y, x + w, y + h], outline=GREY, width=1)
    draw.rectangle([x, y, x + w, y + 26], fill=color)
    draw.text((x + 10, y + 5), name, font=SANS_B(14), fill=(255, 255, 255))
    draw.text((x + w - 92, y + 5), "4 STORIES", font=SANS_B(12),
              fill=(255, 255, 255))
    cy = y + 34
    for i, (head, deck) in enumerate(stories):
        cy = para(draw, x + 10, cy, head, SANS_B(13), w - 20, 14)
        cy = para(draw, x + 10, cy + 1, deck, SANS(11), w - 20, 12,
                  color=(60, 60, 60))
        cy += 6
        if i < len(stories) - 1:
            draw.line([x + 10, cy - 3, x + w - 10, cy - 3], fill=(200, 190, 165))


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([16, 14, W - 16, H - 14], outline=LINE, width=2)

    # Masthead
    f = SERIF_B(56)
    tw = d.textlength(MASTHEAD, font=f)
    d.text(((W - tw) / 2, 22), MASTHEAD, font=f, fill=NAVY)
    f2 = SANS_B(17)
    tw2 = d.textlength(DATELINE, font=f2)
    d.text(((W - tw2) / 2, 92), DATELINE, font=f2, fill=RED)
    d.line([28, 118, W - 28, 118], fill=INK, width=2)

    # Leads
    lw, gap, lx = 314, 12, 28
    for i, (kicker, color, head, deck) in enumerate(LEADS):
        draw_lead(d, lx + i * (lw + gap), 128, lw, 140, kicker, color,
                  head, deck)

    # Map strip
    draw_map(d, 28, 278, W - 56, 92)

    # Sections: two rows of three
    sw, sh = 314, 272
    for row in range(2):
        for col in range(3):
            idx = row * 3 + col
            name, color, stories = SECTIONS[idx]
            draw_section(d, 28 + col * (sw + gap), 380 + row * (sh + 10),
                         sw, sh, name, color, stories)

    # Also-today strip and sources footer
    y = 380 + 2 * sh + 10 + 6
    y = para(d, 28, y, ALSO, SANS_B(12), W - 56, 16)
    d.line([28, y + 4, W - 28, y + 4], fill=LINE, width=1)
    para(d, 28, y + 10, SOURCES, SANS(10), W - 56, 13, color=GREY)
    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    build().save(out, "PNG", optimize=True)
    print("wrote", out)
