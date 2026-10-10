#!/usr/bin/env python3
"""DNS as code for one domain on Cloudflare.

Each domain's repo carries its own copy of this script plus dns/records.json.
records.json is the source of truth for the records it lists; the script only
touches those (it never deletes anything unless you pass --prune).

    python3 cf_dns.py export        # snapshot live records into records.json (first run)
    python3 cf_dns.py plan          # show what apply would change (default, read-only)
    python3 cf_dns.py apply         # make Cloudflare match records.json
    python3 cf_dns.py apply --prune # ...and delete live records not in records.json
    python3 cf_dns.py create-zone   # add the domain to Cloudflare; prints the nameservers
                                    # to set at the registrar

The API token is read from the AUBIT vault by the key named in records.json
("token_key") and is never written anywhere. Records GHL needs must be
"proxied": false (grey cloud) or GHL cannot issue the SSL certificate.
"""
from __future__ import annotations
import argparse, json, pathlib, subprocess, sys, urllib.error, urllib.request

HERE = pathlib.Path(__file__).parent
RECORDS = HERE / "records.json"
VAULT = pathlib.Path("/Users/christopherwhite/Applications/Claude Projects/NEXUS MKII/aubit-now")
API = "https://api.cloudflare.com/client/v4"
KEY_FIELDS = ("type", "name", "content", "proxied", "ttl", "priority")


def token(key: str) -> str:
    out = subprocess.run([sys.executable, "aubit_now_env_vault.py", "get", key, "--reveal"],
                         cwd=VAULT, capture_output=True, text=True, check=True).stdout.strip()
    tok = out.splitlines()[-1].split("=", 1)[-1].strip().strip('"')
    if not tok:
        raise SystemExit(f"vault key {key} is empty")
    return tok


def cf(tok: str, method: str, path: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json",
                 "User-Agent": "psikiq-cf-dns/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            got = json.loads(r.read())
    except urllib.error.HTTPError as e:
        got = json.loads(e.read() or b"{}")
    if not got.get("success"):
        raise SystemExit(f"{method} {path} failed: {got.get('errors')}")
    return got


def zone_id(tok: str, name: str) -> str:
    res = cf(tok, "GET", f"/zones?name={name}")["result"]
    if not res:
        raise SystemExit(f"{name} is not in Cloudflare yet: run create-zone first")
    return res[0]["id"]


def live_records(tok: str, zid: str) -> list[dict]:
    out, page = [], 1
    while True:
        got = cf(tok, "GET", f"/zones/{zid}/dns_records?per_page=100&page={page}")
        out += got["result"]
        if page >= got["result_info"]["total_pages"]:
            return out
        page += 1


def norm(r: dict) -> dict:
    d = {k: r[k] for k in KEY_FIELDS if k in r and r[k] is not None}
    if d.get("type") not in ("MX", "SRV", "URI"):
        d.pop("priority", None)
    return d


def ident(r: dict) -> tuple:
    # TXT/MX can legitimately repeat a name, so identity includes content for those
    return (r["type"], r["name"], r["content"] if r["type"] in ("TXT", "MX", "NS", "CAA") else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", default="plan", choices=["plan", "apply", "export", "create-zone"])
    ap.add_argument("--prune", action="store_true", help="with apply: delete live records not in records.json")
    a = ap.parse_args()

    cfg = json.loads(RECORDS.read_text())
    tok = token(cfg["token_key"])
    zone = cfg["zone"]

    if a.cmd == "create-zone":
        if not cfg.get("account_id"):
            raise SystemExit("set account_id in records.json (Cloudflare dashboard → account home URL)")
        z = cf(tok, "POST", "/zones", {"name": zone, "account": {"id": cfg["account_id"]}, "type": "full"})["result"]
        print(f"✓ {zone} added (status: {z['status']}). Set these nameservers at the registrar:")
        for ns in z["name_servers"]:
            print(f"    {ns}")
        return 0

    zid = zone_id(tok, zone)
    live = live_records(tok, zid)

    if a.cmd == "export":
        cfg["records"] = sorted((norm(r) for r in live), key=lambda r: (r["name"], r["type"], r["content"]))
        RECORDS.write_text(json.dumps(cfg, indent=2) + "\n")
        print(f"✓ exported {len(live)} live records for {zone} into {RECORDS.name}")
        return 0

    want = {ident(r): norm(r) for r in cfg["records"]}
    have = {ident(r): r for r in live}
    creates = [r for k, r in want.items() if k not in have]
    updates = [(have[k], r) for k, r in want.items() if k in have and norm(have[k]) != {**norm(have[k]), **r}]
    deletes = [r for k, r in have.items() if k not in want] if a.prune else []

    for r in creates:
        print(f"+ create  {r['type']:5} {r['name']} → {r['content']}  proxied={r.get('proxied')}")
    for old, r in updates:
        print(f"~ update  {r['type']:5} {r['name']}  {norm(old)} → {r}")
    for r in deletes:
        print(f"- delete  {r['type']:5} {r['name']} → {r['content']}")
    if not (creates or updates or deletes):
        print(f"✓ {zone}: live DNS matches records.json ({len(want)} records)")
        return 0
    if a.cmd == "plan":
        print("(plan only: run `apply` to make these changes)")
        return 0

    for r in creates:
        cf(tok, "POST", f"/zones/{zid}/dns_records", r)
    for old, r in updates:
        cf(tok, "PATCH", f"/zones/{zid}/dns_records/{old['id']}", r)
    for r in deletes:
        cf(tok, "DELETE", f"/zones/{zid}/dns_records/{r['id']}")
    print(f"✓ applied: {len(creates)} created, {len(updates)} updated, {len(deletes)} deleted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
