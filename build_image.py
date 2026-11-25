"""Build entry.png for news-image-20261125, 1024x1024, deterministic.
V2 lesson from 21 Nov: far fewer words, much larger type.
Stories checked 25 Nov 2026, 10:30 WIB, via Reuters / AP summaries:
- Ukraine / Russian ship in Gulf of Finland, Zelenskiy confirms
- Gaza / Hamas security official killed in Israeli drone strikes
- Houthis hit Riyadh's tallest tower, 11 wounded
- Democrats win US House, 259 seats, biggest since 1990
- Nvidia rally fades, -5.9%, Asia tumbles on tariff fears
- Sarkozy + Carla Bruni ordered to trial, Libya case
- Iran whips singer Parastoo Ahmadi 74 times over YouTube concert
Markets strip: Bitcoin $59,258, Brent $90.97, Gold $3,545. Sport: Real Madrid 5-1 PSV.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def main():
    W = H = 1024
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 118], fill="black")
    d.text((36, 18), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill="white")
    d.text((36, 76), "WEDNESDAY  25  NOVEMBER  2026", font=font(BOLD, 26), fill="#ffcc00")
    # Lead story
    d.rectangle([36, 142, 46, 342], fill="#c8102e")
    lead = "UKRAINE HITS\nRUSSIAN SHIP"
    y = 142
    for line in lead.split("\n"):
        d.text((66, y), line, font=font(BOLD, 64), fill="black")
        y += 72
    d.text((66, 292), "Zelenskiy confirms drone strike in the Gulf of Finland.",
           font=font(REG, 25), fill="#333333")
    d.text((66, 324), "Norway urges caution.", font=font(REG, 25), fill="#333333")
    # Grid: 2 cols x 3 rows
    cards = [
        ("GAZA", "HAMAS OFFICIAL\nKILLED", "Israeli drones strike\nGaza City"),
        ("MIDDLE EAST", "HOUTHIS HIT\nRIYADH TOWER", "11 wounded in tallest\ntower strike"),
        ("USA", "DEMOCRATS\nWIN HOUSE", "259 seats \u2014 biggest\nsince 1990"),
        ("MARKETS", "NVIDIA RALLY\nFADES", "Shares \u22125.9%; Asia falls\non tariff fears"),
        ("FRANCE", "SARKOZY TO\nFACE TRIAL", "Ex-president and Carla\nBruni, Libya case"),
        ("IRAN", "SINGER WHIPPED\n74 TIMES", "Parastoo Ahmadi, over\na YouTube concert"),
    ]
    x0, y0 = 36, 368
    cw, ch, gap = 466, 170, 16
    for i, (tag, head, sub) in enumerate(cards):
        x = x0 + (i % 2) * (cw + gap)
        yy = y0 + (i // 2) * (ch + gap)
        d.rectangle([x, yy, x + cw, yy + ch], fill="#f2f2f2")
        d.rectangle([x, yy, x + cw, yy + 6], fill="#c8102e")
        d.text((x + 18, yy + 16), tag, font=font(BOLD, 20), fill="#c8102e")
        hy = yy + 42
        for line in head.split("\n"):
            d.text((x + 18, hy), line, font=font(BOLD, 31), fill="black")
            hy += 36
        sy = hy + 4
        for line in sub.split("\n"):
            d.text((x + 18, sy), line, font=font(REG, 20), fill="#333333")
            sy += 24
    # Bottom strip
    by = 922
    d.rectangle([0, by, W, by + 66], fill="black")
    d.text((36, by + 8), "BITCOIN $59,258  \u00b7  BRENT $90.97  \u00b7  GOLD $3,545",
           font=font(BOLD, 23), fill="white")
    d.text((36, by + 36), "SPORT: REAL MADRID 5\u20131 PSV", font=font(BOLD, 23), fill="#ffcc00")
    d.text((36, by + 72), "Sources: Reuters, AP  \u2014  25 November 2026",
           font=font(REG, 16), fill="#666666")
    img.save(OUT, "PNG", optimize=True)
    print(OUT)

if __name__ == "__main__":
    main()
