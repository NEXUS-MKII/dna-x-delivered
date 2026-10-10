#!/usr/bin/env python3
"""DNA-X landing page: build from the Marketing NOW v1.4 sections.

The source sections (source_marketing_now_v1.4/) stay untouched. This script
rebrands them as DNA-X on every run, so fixes go here or into the source,
never into the output.

  * NOW is removed: class/variable prefix now- → dnax-, the JS namespace
    NOW → DNAX, and the NOW copy, links and schema.
  * DNA-X palette: the original navy + orange, token prefix dnax-. See DNAX_BRAND.md.
  * Prices come from the build scripts (NEXUS MKII/nexus_wow_ext.py PRODUCTS):
    Build F $1,997; bundles re-priced to match the scripts.
  * Checkout links point at GHL placeholders until the products exist.

Outputs:
  dist/index.html                                   the assembled page
  psikiq-workbench/prototypes/dnax-landing/...      the same page, for review

    python3 build_page.py
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
SRC = HERE / "source_marketing_now_v1.4"
DIST = HERE / "dist"
WORKBENCH = HERE.parents[1] / "psikiq-workbench" / "prototypes" / "dnax-landing"

# Display order (04.5 sits after the bundles, per the v1.4 README)
ORDER = ["00_foundation", "01_hero", "02_system", "03_tier1_carousel", "04_dnax_carousel",
         "05_bundles_carousel", "04.5_funnel", "06_proof_faq", "07_close_footer"]

# ── DNA-X palette ──────────────────────────────────────────────────────────────
# The DNA-X palette is the original navy + orange (Chris, 2026-10-10); only the
# token prefix changes. See DNAX_BRAND.md.
ROOT = """:root {
  --dnax-navy: #1A1A2E;          /* primary brand: hero bg, headings, body text */
  --dnax-deep-navy: #080808;     /* deepest tone: footer, high-contrast panels */
  --dnax-orange: #E84C1E;        /* accent: CTAs, links, eyebrows, the X in DNAx */
  --dnax-orange-dk: #B83B17;     /* hover on orange buttons / links */
  --dnax-orange-light: #FF6B3D;  /* reserved: gradients, glows, hover accents */
  --dnax-white: #FFFFFF;
  --dnax-light-bg: #F8F8F8;
  --dnax-light-gray: #E8E8E8;
  --dnax-mid-gray: #666666;
  --dnax-text: #1A1A2E;
  --dnax-text-muted: #555555;
  --dnax-text-light: rgba(255, 255, 255, 0.95);
  --dnax-text-light-dim: rgba(255, 255, 255, 0.78);
  --dnax-warn-bg: #FFF7ED;
  --dnax-warn-border: #F59E0B;
  --dnax-warn-text: #92400E;
}"""

# Visible copy: (old, new). Order matters for overlapping phrases.
COPY = [
    ("MARKETING NOW", "DNA-X"),
    ("Marketing NOW", "DNA-X"),
    ("NOW underneath, your DNA on top", "Our engine underneath, your DNA on top"),
    ("NOW AESTHETIC", "DNA-X AESTHETIC"),
    ("NOW aesthetic", "DNA-X aesthetic"),
    ("Kajabi custom code block AND GitHub repo", "GHL custom code block AND GitHub repo"),
    ("Kajabi block + GitHub repo", "GHL block + GitHub repo"),
    ("Kajabi or GitHub", "GHL or GitHub"),
    ("We deliver Kajabi-ready and GitHub-ready by default", "We deliver GHL-ready and GitHub-ready by default"),
    ("Kajabi-ready and GitHub-ready by default", "GHL-ready and GitHub-ready by default"),
    ("anything that takes HTML and CSS — Kajabi, WordPress", "anything that takes HTML and CSS — GoHighLevel, WordPress"),
    ("If you cancel your Kajabi, your relationship with us", "If you change platforms, end your relationship with us"),
    ("At Kajabi checkout.", "At checkout."),
    ("Kajabi offer URLs are not yet configured", "GHL product links are not yet configured"),
    ("Kajabi URL not yet configured", "GHL product link not yet configured"),
    ("Kajabi offer URLs not configured", "GHL product links not configured"),
    ("Calendly URL not yet configured", "Booking link not yet configured"),
    ("[Marketing NOW]", "[DNA-X]"),
    ("#REPLACE_KAJABI_OFFER_URL_*", "#REPLACE_GHL_PRODUCT_URL_*"),
    # footer
    ('<a href="https://www.nowgroup.co.nz/">Home</a>', '<a href="https://dnaxmarketing.com/">Home</a>'),
    ('<a href="https://www.nowgroup.co.nz/about">About NOW</a>', '<a href="https://psikiq.io/">PsikiQ</a>'),
    ('<a href="https://www.nowgroup.co.nz/netsync">NET_SYNC</a>\n', ""),
    ('<a href="https://www.nowgroup.co.nz/blog">Blog</a>\n', ""),
    ("https://www.nowgroup.co.nz/privacy", "https://dnaxmarketing.com/privacy"),
    ("https://www.nowgroup.co.nz/terms", "https://dnaxmarketing.com/terms"),
    ("mailto:chris@nowgroup.co.nz\">chris@nowgroup.co.nz", "mailto:chris@psikiq.io\">chris@psikiq.io"),
    ("© 2026 NOW Group. All rights reserved.", "© 2026 DNA-X · PsikiQ Solutions. All rights reserved."),
    # diagnostic CTA: NET_SYNC brandkit is NOW infrastructure. DNA-X diagnostic URL TBC
    ("https://netsync.nowgroup.co.nz/brandkit/", "#dnax-diagnostic"),
    # schema
    ('"name": "NOW Group",\n  "alternateName": "DNA-X"', '"name": "DNA-X",\n  "parentOrganization": {"@type": "Organization", "name": "PsikiQ Solutions", "url": "https://psikiq.io"}'),
    ('"url": "https://www.nowgroup.co.nz"', '"url": "https://dnaxmarketing.com"'),
    ('"email": "chris@nowgroup.co.nz"', '"email": "chris@psikiq.io"'),
    ('"addressLocality": "Auckland",\n    ', ""),
    ("member", "partner"), ("Member", "Partner"),
]

# Prices + product changes, scoped per file: (file, old, new).
# Source of truth: NEXUS MKII/nexus_wow_ext.py PRODUCTS (updated 2026-10-10):
#   D Quiz Endpoint $3,497 (incl. main quiz landing page) · E GEO + SEO $2,597 (24 citations
#   standard) · F BizCard $1,997 · Content Pack Pro = 4 x 600-word pillar articles, fortnightly.
# Bundles: doubles save $497, the triple saves $494 (rule carried from the scripts).
#   D+E $6,094 → $5,597 · D+F $5,494 → $4,997 · E+F $4,594 → $4,097 · D+E+F $8,091 → $7,597
PRICES = [
    # Content Pack Pro
    ("03_tier1_carousel", "<li>2 pillar articles, 1,200–1,800 words each</li>",
                          "<li>4 pillar articles, 600 words each, released fortnightly</li>"),
    # Build D: Quiz Endpoint, $3,497, main quiz landing page
    ("02_system", '<div class="dnax-spine-mod">Quiz Funnel</div>', '<div class="dnax-spine-mod">Quiz Endpoint</div>'),
    ("04_dnax_carousel", "<h3>Build D — Quiz Funnel</h3>", "<h3>Build D — Quiz Endpoint</h3>"),
    ("04_dnax_carousel", "Custom-scored. Three result tiers,", "A main quiz landing page, custom scoring, three result tiers,"),
    ("04_dnax_carousel", "<li>3 result pages, 3 lead magnets, 8-email sequence</li>",
                         "<li>Main quiz landing page + 3 result pages</li>\n              <li>3 lead magnets + 8-email sequence</li>"),
    ("04_dnax_carousel", '<div class="dnax-card-price">$2,497</div>', '<div class="dnax-card-price">$3,497</div>'),
    ("04_dnax_carousel", "Start Build D — $2,497", "Start Build D — $3,497"),
    ("04_dnax_carousel", "quiz universe + scoring + landing + 3 result pages", "quiz universe + scoring + main quiz landing page + 3 result pages"),
    # Build E: 24 citations standard, $2,597
    ("04_dnax_carousel", "12 articles. 3 schema layers. 12 foundation citations.", "12 articles. 3 schema layers. 24 foundation citations."),
    ("04_dnax_carousel", "12 articles, three-layer schema, 12 high-trust citations", "12 articles, three-layer schema, 24 high-trust citations"),
    ("04_dnax_carousel", "<li>12 high-trust citations — manually verified foundation</li>",
                         "<li>24 high-trust citations: 12 automated + 12 hand-placed by a VA</li>"),
    ("04_dnax_carousel", '<div class="dnax-card-price">$1,997</div>\n            <div class="dnax-card-meta">4-WEEK',
                         '<div class="dnax-card-price">$2,597</div>\n            <div class="dnax-card-meta">4-WEEK'),
    ("04_dnax_carousel", "Start Build E — $1,997", "Start Build E — $2,597"),
    ("04_dnax_carousel", "<p><strong>12-citation foundation pack</strong>", "<p><strong>24-citation foundation pack</strong>"),
    ("04_dnax_carousel", "<p><strong>Optional Depth Upgrade (+$597)</strong> — VA Manual Citations: 12 hand-placed niche citations on top of the base 12. Total: 24, still a foundation.</p>",
                         "<p><strong>VA Manual Citations (included)</strong> — 12 hand-placed niche citations on top of the base 12. Total: 24, still a foundation.</p>"),
    ("06_proof_faq", "12 articles, 3 schema layers, 12 high-trust citations. It's a starter", "12 articles, 3 schema layers, 24 high-trust citations. It's a starter"),
    ("06_proof_faq", "The VA Depth Upgrade ($597) adds 12 hand-placed citations", "Build E also includes 12 VA hand-placed citations"),
    ("06_proof_faq", "Total with upgrade: 24 citations.", "Total: 24 citations."),
    ("06_proof_faq", "Build E is a 12-citation foundation pack", "Build E is a 24-citation foundation pack"),
    # Build F
    ("04_dnax_carousel", '<div class="dnax-card-price">$1,497</div>', '<div class="dnax-card-price">$1,997</div>'),
    ("04_dnax_carousel", "Start Build F — $1,497", "Start Build F — $1,997"),
    ("07_close_footer", "From $1,497.", "From $1,997."),
    # Bundles
    ("05_bundles_carousel", '<span class="dnax-bundle-strike">$4,494</span>  →  <span class="dnax-bundle-newprice">$3,997</span>',
                            '<span class="dnax-bundle-strike">$6,094</span>  →  <span class="dnax-bundle-newprice">$5,597</span>'),
    ("05_bundles_carousel", '<div class="dnax-bundle-price-block">$3,997</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-pipeline">Start Pipeline Engine — $3,997</a>',
                            '<div class="dnax-bundle-price-block">$5,597</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-pipeline">Start Pipeline Engine — $5,597</a>'),
    ("05_bundles_carousel", '<span class="dnax-bundle-strike">$3,994</span>  →  <span class="dnax-bundle-newprice">$3,497</span>',
                            '<span class="dnax-bundle-strike">$5,494</span>  →  <span class="dnax-bundle-newprice">$4,997</span>'),
    ("05_bundles_carousel", '<div class="dnax-bundle-price-block">$3,497</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-conversion">Start Conversion Stack — $3,497</a>',
                            '<div class="dnax-bundle-price-block">$4,997</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-conversion">Start Conversion Stack — $4,997</a>'),
    ("05_bundles_carousel", '<span class="dnax-bundle-strike">$3,494</span>  →  <span class="dnax-bundle-newprice">$2,997</span>',
                            '<span class="dnax-bundle-strike">$4,594</span>  →  <span class="dnax-bundle-newprice">$4,097</span>'),
    ("05_bundles_carousel", '<div class="dnax-bundle-price-block">$2,997</div>', '<div class="dnax-bundle-price-block">$4,097</div>'),
    ("05_bundles_carousel", "Start Authority Stack — $2,997", "Start Authority Stack — $4,097"),
    ("05_bundles_carousel", '<span class="dnax-bundle-strike">$5,991</span>  →  <span class="dnax-bundle-newprice">$4,997</span>',
                            '<span class="dnax-bundle-strike">$8,091</span>  →  <span class="dnax-bundle-newprice">$7,597</span>'),
    ("05_bundles_carousel", '<div class="dnax-bundle-price-block">$4,997</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-complete-factory">',
                            '<div class="dnax-bundle-price-block">$7,597</div>\n            <a href="#" class="dnax-btn dnax-btn-block" data-offer="bundle-complete-factory">'),
    ("05_bundles_carousel", "Start Complete Factory — $4,997", "Start Complete Factory — $7,597"),
    ("05_bundles_carousel", "SAVE $994", "SAVE $494"),
    # Pack letters per the scripts: B = Email Database Rescue, C = Partner Growth
    ("03_tier1_carousel", "<li>Pack B — Partner Growth System</li>\n              <li>Pack C — Email Database Rescue</li>",
                          "<li>Pack B — Email Database Rescue</li>\n              <li>Pack C — Partner Growth System</li>"),
]


REGEX = [  # whitespace-tolerant rewrites
    (r"— a productised marketing system from NOW Group\.<br>\s*Networking Our Way\. Auckland, NZ\.",
     "— generative marketing, hand built by robots.<br>\n        A PsikiQ Solutions company. New Zealand."),
    (r"Custom Code Block on the Kajabi page", "Custom Code element on the GHL page"),
    (r"\(Essentials / DNAx / Calendly\)", "(Essentials / DNAx / book a call)"),
]


def letters(name: str, s: str) -> str:
    """B = Email Rescue (Activation), C = Partner Growth (Alliance), per the build scripts."""
    if name == "02_system":
        b = re.search(r'<div class="dnax-spine-cell">\s*<div class="dnax-spine-letter">B</div>.*?</div>\s*</div>', s, re.S)
        c = re.search(r'<div class="dnax-spine-cell">\s*<div class="dnax-spine-letter">C</div>.*?</div>\s*</div>', s, re.S)
        if not (b and c):
            raise SystemExit("02_system: spine cells B/C not found")
        nb = c.group(0).replace(">C<", ">B<"); nc = b.group(0).replace(">B<", ">C<")
        s = s[:b.start()] + nb + s[b.end():c.start()] + nc + s[c.end():]
    if name == "03_tier1_carousel":
        m = re.search(r"(        <!-- Card B — Alliance -->\n.*?)(        <!-- Card C — Activation -->\n.*?)(        <!-- WOW Bundle)", s, re.S)
        if not m:
            raise SystemExit("03_tier1_carousel: cards B/C not found")
        card_b = m.group(2).replace("Card C — Activation", "Card B — Activation")
        card_c = m.group(1).replace("Card B — Alliance", "Card C — Alliance")
        s = s[:m.start()] + card_b + card_c + m.group(3) + s[m.end():]
    return s


def drop_placeholder_proof(name: str, s: str) -> str:
    """The six proof vignettes are invented placeholders. They never ship; restore when real quotes exist."""
    if name == "06_proof_faq":
        s2 = re.sub(r"<!-- ═══ PROOF ═══ -->.*?(?=<!-- ═══ FAQ ═══ -->)", "", s, count=1, flags=re.S)
        if s2 == s:
            raise SystemExit("06_proof_faq: proof section not found")
        s = s2
    return s


def rebrand(name: str, s: str) -> str:
    s = re.sub(r"(?<![A-Za-z])now-", "dnax-", s)
    s = re.sub(r"\bNOW\.", "DNAX.", s)
    s = s.replace("window.NOW = window.NOW", "window.DNAX = window.DNAX")
    if name == "00_foundation":
        s = re.sub(r":root \{.*?\n\}", ROOT, s, count=1, flags=re.S)
        s = s.replace("'#REPLACE_KAJABI_OFFER_URL_", "'#REPLACE_GHL_PRODUCT_URL_")
        s = s.replace("'#REPLACE_CALENDLY_FIT_CALL_URL'", "'#REPLACE_GHL_BOOKING_URL'")
    for old, new in COPY:
        s = s.replace(old, new)
    for pat, new in REGEX:
        s = re.sub(pat, new, s)
    s = letters(name, s)
    s = drop_placeholder_proof(name, s)
    for f, old, new in PRICES:
        if f == name:
            if old not in s:
                raise SystemExit(f"{name}: price anchor not found: {old[:70]}")
            s = s.replace(old, new)
    return s


SECTION_NAMES = {"00_foundation": "foundation (styles + scripts, MUST be first)", "01_hero": "hero",
                 "02_system": "system + six A's", "03_tier1_carousel": "Tier 1 carousel",
                 "04_dnax_carousel": "DNAx builds carousel", "05_bundles_carousel": "bundles carousel",
                 "04.5_funnel": "how the funnel works", "06_proof_faq": "FAQ",
                 "07_close_footer": "close + footer"}


def main() -> None:
    parts = [(n, rebrand(n, (SRC / f"{n}.html").read_text())) for n in ORDER]
    body = "\n".join(p for _, p in parts)
    sec = DIST / "sections"
    sec.mkdir(parents=True, exist_ok=True)
    for old in sec.glob("*.html"):
        old.unlink()
    for i, (n, p) in enumerate(parts, 1):
        slug = n.split("_", 1)[1].replace("_", "-").replace("proof-faq", "faq")
        (sec / f"{i:02d}_{slug}.html").write_text(p)
    leftovers = sorted(set(re.findall(r"[^\n]{0,30}(?:(?<!DONE )\bNOW\b|nowgroup|Kajabi|Calendly|NET_SYNC)[^\n]{0,30}", body)))
    page = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "<title>DNA-X · Generative marketing</title>\n</head>\n<body style=\"margin:0\">\n"
            + body + "\n</body>\n</html>\n")
    DIST.mkdir(exist_ok=True)
    (DIST / "index.html").write_text(page)
    (WORKBENCH / "screens").mkdir(parents=True, exist_ok=True)
    (WORKBENCH / "screens" / "home.html").write_text(page)
    (WORKBENCH / "manifest.json").write_text(json.dumps({
        "name": "DNA-X · Landing (v0.1 from Marketing NOW v1.4)",
        "description": "DNA-X's own landing page, rebranded from the Kajabi Marketing NOW build. Prices per the build scripts.",
        "device": "desktop", "start": "home",
        "screens": [{"id": "home", "title": "Home", "file": "screens/home.html"}]}, indent=2) + "\n")
    # GHL: the whole page as ONE Custom Code element in a full-width section
    ghl = ("<!-- DNA-X home: ONE Custom Code element, full-width section. -->\n"
           "<!-- GENERATED by build_page.py; edit the source sections or the build, not this file. -->\n"
           "<style>\n"
           "  /* GHL caps every section's inner row at 1170px, even full-width ones. Lift it, and the\n"
           "     row/column padding, only on the section holding this page. */\n"
           "  .c-section:has(.dnax-hero-section) > .inner{max-width:none!important;width:100%!important;}\n"
           "  .c-section:has(.dnax-hero-section),\n"
           "  .c-section:has(.dnax-hero-section) .c-row,\n"
           "  .c-section:has(.dnax-hero-section) .c-column{padding:0!important;margin:0!important;}\n"
           "</style>\n" + body + "\n")
    (DIST / "dnax-home-ghl.html").write_text(ghl)
    print(f"✓ dist/dnax-home-ghl.html  ({len(ghl)//1024} KB)  for the GHL Custom Code element")
    # Public site repo (one repo per domain): generated output only, never the build or the sources
    site = HERE.parents[1] / "dnax-marketing"
    if site.is_dir():
        (site / "sections").mkdir(exist_ok=True)
        for old in (site / "sections").glob("*.html"):
            old.unlink()
        for f in sec.glob("*.html"):
            (site / "sections" / f.name).write_text(f.read_text())
        (site / "ghl").mkdir(exist_ok=True)
        (site / "ghl" / "dnax-home-ghl.html").write_text(ghl)
        # temporary landing page on GitHub Pages: kept out of search until the domain is live
        (site / "index.html").write_text(page.replace("<head>\n", "<head>\n<meta name=\"robots\" content=\"noindex, nofollow\">\n", 1))
        print(f"✓ synced to {site.name}/ (index.html, sections/, ghl/)")
    print(f"✓ dist/index.html  ({len(page)//1024} KB)  + workbench prototype dnax-landing")
    if leftovers:
        print("⚠ NOW/Kajabi residue still in the page:")
        for l in leftovers:
            print("   ", l.strip())


if __name__ == "__main__":
    main()
