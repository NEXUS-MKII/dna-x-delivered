#!/usr/bin/env python3
"""Render one product card per entry in catalogue.json.

The cards are what GHL shows in store listings, order forms and invoices, so they
carry the site's language exactly: steel ground, gold psi, mono kicker, Oswald name,
gold price, hairline rules. 1000x1000 — square is the one shape every GHL surface
crops safely.

    python3 build_cards.py            # writes cards/ + a contact sheet
    python3 build_cards.py --sheet-only

Fonts are fetched once to the system temp dir (Oswald + JetBrains Mono, the site's).
"""
from __future__ import annotations
import json, pathlib, sys, tempfile, urllib.request
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).parent
CARDS = HERE / "cards"
FONTS = pathlib.Path(tempfile.gettempdir()) / "psikiq-fonts"
SRC = {
    "Oswald.ttf": "https://github.com/google/fonts/raw/main/ofl/oswald/Oswald%5Bwght%5D.ttf",
    "JetBrainsMono.ttf": "https://github.com/google/fonts/raw/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
}
VOID = (23, 17, 10, 255)
GOLD = (230, 190, 106, 255)
WARM = (232, 145, 46, 255)
WHITE = (255, 255, 255, 255)
MUT = (114, 126, 142, 255)
S = 1000                      # card edge
PAD = 78

def _fonts() -> dict:
    FONTS.mkdir(exist_ok=True)
    for name, url in SRC.items():
        p = FONTS / name
        if not p.exists():
            urllib.request.urlretrieve(url, p)
    return {k: FONTS / k for k in SRC}

def osw(px: int, weight: str = "SemiBold"):
    f = ImageFont.truetype(str(_F["Oswald.ttf"]), px)
    f.set_variation_by_name(weight)
    return f

def mono(px: int, weight: str = "Medium"):
    f = ImageFont.truetype(str(_F["JetBrainsMono.ttf"]), px)
    f.set_variation_by_name(weight)
    return f

def tracked(d: ImageDraw.ImageDraw, xy, text: str, font, fill, track: float):
    """letter-spacing, which Pillow has no notion of — the brand leans on it hard"""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + track
    return x

def tw(text: str, font, track: float) -> float:
    """width as tracked() will actually draw it — Pillow's getlength knows nothing of tracking"""
    return sum(font.getlength(c) + track for c in text) - (track if text else 0)

def wrap(text: str, font, width: int, track: float = 0.0) -> list[str]:
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if tw(t, font, track) <= width:
            line = t
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines

def steel(size: int) -> Image.Image:
    """the site's brushed steel: vertical striations + a diagonal sheen"""
    im = Image.new("RGBA", (size, size), VOID)
    d = ImageDraw.Draw(im)
    band = [(0x17,0x11,0x0a),(0x20,0x18,0x0e),(0x19,0x11,0x08),(0x24,0x1b,0x0f),(0x15,0x0f,0x08)]
    step = max(2, size // 125)
    for x in range(0, size, step):
        c = band[(x // step) % len(band)]
        d.rectangle((x, 0, x + step - 1, size), fill=c + (255,))
    sheen = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sheen)
    for i in range(size * 2):
        a = int(26 * max(0.0, 1 - abs(i - size * 0.55) / (size * 0.5)))
        if a:
            sd.line((i, 0, i - size, size), fill=(230, 190, 106, a), width=3)
    return Image.alpha_composite(im, sheen)

def card(p: dict, psi: Image.Image) -> Image.Image:
    """Bottom-anchored: the price block is fixed to the foot, the name sits on the
    rule above it, so a one-line and a three-line name both breathe."""
    im = steel(S)
    d = ImageDraw.Draw(im)
    FOOT_Y  = S - 88                 # footer baseline
    PRICE_Y = FOOT_Y - 148           # price block top
    RULE_Y  = PRICE_Y - 46           # hairline above the price
    # top rule + psi mark + kicker
    d.rectangle((0, 0, S, 5), fill=GOLD)
    m = psi.copy()
    m.thumbnail((104, 104), Image.LANCZOS)
    im.alpha_composite(m, (PAD, PAD))
    tracked(d, (PAD + m.width + 26, PAD + 40), p["kicker"].upper(), mono(20), WARM, 3.4)
    # name + blurb, bottom-anchored to the rule
    # measure what is actually drawn: the name is upper-cased, and uppercase runs
    # ~15% wider than the mixed case it is written in. -26 for Oswald side-bearings.
    TRACK, MAXW = 1.2, S - PAD * 2 - 26
    NAME = p["name"].upper()
    f_name = osw(86)
    lines = wrap(NAME, f_name, MAXW, TRACK)
    while (len(lines) > 2 or max((tw(l, f_name, TRACK) for l in lines), default=0) > MAXW) and f_name.size > 52:
        f_name = osw(f_name.size - 4)
        lines = wrap(NAME, f_name, MAXW, TRACK)
    lh = int(f_name.size * 1.04)
    f_blurb = mono(21)
    block_h = lh * len(lines) + 34 + f_blurb.size
    y = RULE_Y - 56 - block_h
    for ln in lines:
        tracked(d, (PAD, y), ln, f_name, WHITE, TRACK)
        y += lh
    tracked(d, (PAD, y + 34), p["blurb"].upper(), f_blurb, MUT, 2.6)
    # hairline, price, qualifier
    d.rectangle((PAD, RULE_Y, S - PAD, RULE_Y + 1), fill=(230, 190, 106, 70))
    f_price = osw(100)
    d.text((PAD, PRICE_Y), p["price_label"], font=f_price, fill=GOLD)
    qual = ("RECURRING" if (p.get("price") and p["price"]["type"] == "recurring")
            else "SCOPED" if not p.get("price") else None)
    if qual:
        tracked(d, (PAD + f_price.getlength(p["price_label"]) + 20, PRICE_Y + 62),
                qual, mono(19), MUT, 2.6)
    # footer
    tracked(d, (PAD, FOOT_Y), "PSIKIQ", mono(22, "Bold"), GOLD, 4.0)
    f_cur = mono(19)
    cur = "NZD EX-GST"
    tracked(d, (S - PAD - tw(cur, f_cur, 2.6), FOOT_Y + 2), cur, f_cur, MUT, 2.6)
    # corner brackets — the HUD signature
    b, t = 46, 3
    for x0, y0, x1, y1 in ((PAD-28, PAD-28, PAD-28+b, PAD-28+t), (PAD-28, PAD-28, PAD-28+t, PAD-28+b),
                           (S-PAD+28-b, S-PAD+28-t, S-PAD+28, S-PAD+28), (S-PAD+28-t, S-PAD+28-b, S-PAD+28, S-PAD+28)):
        d.rectangle((x0, y0, x1, y1), fill=(230, 190, 106, 150))
    return im

def main() -> int:
    global _F
    _F = _fonts()
    cat = json.loads((HERE / "catalogue.json").read_text())
    psi = Image.open(HERE.parent / "psi-gold.webp").convert("RGBA")
    CARDS.mkdir(exist_ok=True)
    made = []
    for p in cat["products"]:
        im = card(p, psi)
        out = CARDS / f"{p['key']}.png"
        im.save(out, optimize=True)
        made.append((p["key"], out.stat().st_size // 1024))
    # contact sheet, 5 across
    cols, th = 5, 300
    rows = (len(made) + cols - 1) // cols
    sheet = Image.new("RGBA", (cols * th + (cols + 1) * 12, rows * th + (rows + 1) * 12), (238, 240, 243, 255))
    for i, (key, _) in enumerate(made):
        t = Image.open(CARDS / f"{key}.png").resize((th, th), Image.LANCZOS)
        sheet.alpha_composite(t, (12 + (i % cols) * (th + 12), 12 + (i // cols) * (th + 12)))
    sheet.save(HERE / "_sheet.png")
    print(f"{len(made)} cards → {CARDS}")
    for k, kb in made:
        print(f"  {k}.png  {kb} KB")
    return 0

if __name__ == "__main__":
    sys.exit(main())
