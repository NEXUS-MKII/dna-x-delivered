#!/usr/bin/env python3
"""Create / update the PsikiQ product ladder in the GHL PsikiQSolutions location.

catalogue.json is the source; this pushes it to GHL. Idempotent by product NAME:
a product whose name already exists is updated, not duplicated. Prices are a separate
endpoint; the product's single price is created if absent and corrected if it has drifted.
Amounts are WHOLE DOLLARS — this API takes major units, not cents.

    python3 sync_products.py --dry-run     # print what would happen, touch nothing
    python3 sync_products.py               # create/update
    python3 sync_products.py --list        # what is in GHL right now

The token is read from the AUBIT vault (GHL_PSIKIQ_FULL) — never stored here, never
printed. Images are served from the public host; run build_cards.py and push them
to the psikiq Pages repo before syncing, or products land without art.
"""
from __future__ import annotations
import argparse, json, pathlib, subprocess, sys, urllib.error, urllib.request

HERE = pathlib.Path(__file__).parent
VAULT = pathlib.Path("/Users/christopherwhite/Applications/Claude Projects/NEXUS MKII/aubit-now")
BASE = "https://services.leadconnectorhq.com"
LOCATION = "XmnnOgihSvpbtlApd8cN"          # PsikiQSolutions
IMG_BASE = "https://nexus-mkii.github.io/psikiq/products"
VERSION = "2021-07-28"

def token() -> str:
    out = subprocess.run(
        [sys.executable, "aubit_now_env_vault.py", "get", "GHL_PSIKIQ_FULL", "--reveal"],
        cwd=VAULT, capture_output=True, text=True, check=True).stdout.strip().splitlines()[-1]
    return out.split("=", 1)[-1].strip().strip('"')

def api(method: str, path: str, tok: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(
        f"{BASE}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {tok}", "Version": VERSION,
                 "Content-Type": "application/json", "Accept": "application/json",
                 # Cloudflare in front of the API 1010s urllib's default agent
                 "User-Agent": "psikiq-catalogue-sync/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} → {e.code}: {e.read().decode()[:400]}")

def existing(tok: str) -> dict[str, dict]:
    got = api("GET", f"/products/?locationId={LOCATION}&limit=100", tok)
    return {p["name"]: p for p in got.get("products", [])}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    tok = token()

    if a.list:
        for name, p in sorted(existing(tok).items()):
            print(f"  {p['_id']}  {name}")
        return 0

    cat = json.loads((HERE / "catalogue.json").read_text())
    have = existing(tok)
    for item in cat["products"]:
        body = {
            "locationId": LOCATION,
            "name": item["name"],
            "description": item["description"],
            "productType": "SERVICE",
            "image": f"{IMG_BASE}/{item['key']}.png",
            "availableInStore": True,
            "slug": item["key"],
            # medias[].id is required even for externally hosted art — the card's key is stable
            "medias": [{"id": item["key"], "title": item["name"],
                        "url": f"{IMG_BASE}/{item['key']}.png", "type": "image", "isFeatured": True}],
        }
        cur = have.get(item["name"])
        if a.dry_run:
            print(f"{'UPDATE' if cur else 'CREATE'}  {item['name']}")
            if item.get("price"):
                pr = item["price"]
                unit = f"${pr['amount']:,} {cat['currency']}"
                print(f"         price: {pr['type']} {unit}"
                      + (f" / {pr['interval']}" if pr["type"] == "recurring" else ""))
            else:
                print(f"         price: none — {item.get('price_note', 'quoted at point of sale')}")
            continue

        if cur:
            pid = cur["_id"]
            api("PUT", f"/products/{pid}", tok, body)
            action = "updated"
        else:
            pid = api("POST", "/products/", tok, body)["_id"]
            action = "created"

        # price — one per product, only if it has none yet
        note = ""
        if item.get("price"):
            prices = api("GET", f"/products/{pid}/price?locationId={LOCATION}&limit=20", tok).get("prices", [])
            pr = item["price"]
            pbody = {"locationId": LOCATION, "name": pr["name"], "type": pr["type"],
                     "currency": cat["currency"], "amount": pr["amount"]}
            if pr["type"] == "recurring":
                pbody["recurring"] = {"interval": pr["interval"], "intervalCount": 1}
            if not prices:
                api("POST", f"/products/{pid}/price", tok, pbody)
                note = f" + price ${pr['amount']:,}"
            elif prices[0]["amount"] != pr["amount"] or prices[0]["type"] != pr["type"]:
                api("PUT", f"/products/{pid}/price/{prices[0]['_id']}", tok, pbody)
                note = f" ~ price ${prices[0]['amount']:,} → ${pr['amount']:,}"
            else:
                note = f" (price ${pr['amount']:,} already set)"
        else:
            note = " (no price — quoted at point of sale)"
        print(f"{action:>8}  {item['name']}{note}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
