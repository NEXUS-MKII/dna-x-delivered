#!/usr/bin/env python3
"""Upload the site's images into the PsikiQSolutions GHL Media Library.

GHL-hosted media replaces GitHub Pages as the image host, so the site and the
product cards no longer depend on a public repo. Each file is uploaded once;
the GHL URL is recorded in media_map.json (relative path → URL), which
build_ghl.py and products/sync_products.py read. Re-running skips anything
already mapped; --force re-uploads.

    python3 push_media.py            # upload new files
    python3 push_media.py --dry-run  # list what would upload
"""
import argparse, json, mimetypes, pathlib, sys, urllib.error, urllib.request, uuid

sys.path.insert(0, str(pathlib.Path(__file__).parent / "products"))
from sync_products import BASE, LOCATION, VERSION, token  # noqa: E402

HERE = pathlib.Path(__file__).parent
MAP = HERE / "media_map.json"
FILES = (["psi-gold.webp", "psi-split.webp", "psi-split-250.webp", "logo/psikiq-og-1200x630.png"]
         + sorted(f"icons/{p.name}" for p in (HERE / "icons").iterdir() if p.suffix in (".png", ".ico"))
         + sorted(f"products/cards/{p.name}" for p in (HERE / "products/cards").glob("*.png")))


def upload(tok: str, rel: str) -> str:
    path = HERE / rel
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    name = "psikiq-" + rel.replace("/", "-")
    parts = [
        (f'--{boundary}\r\nContent-Disposition: form-data; name="hosted"\r\n\r\nfalse\r\n').encode(),
        (f'--{boundary}\r\nContent-Disposition: form-data; name="name"\r\n\r\n{name}\r\n').encode(),
        (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\n'
         f'Content-Type: {ctype}\r\n\r\n').encode() + path.read_bytes() + b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ]
    req = urllib.request.Request(
        f"{BASE}/medias/upload-file?altId={LOCATION}&altType=location", method="POST",
        data=b"".join(parts),
        headers={"Authorization": f"Bearer {tok}", "Version": VERSION, "Accept": "application/json",
                 "Content-Type": f"multipart/form-data; boundary={boundary}",
                 "User-Agent": "psikiq-media-push/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            got = json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"upload {rel} → {e.code}: {e.read().decode()[:400]}")
    url = got.get("url")
    if not url:
        raise SystemExit(f"upload {rel}: no url in response {got}")
    return url


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", help="upload just this relative path")
    a = ap.parse_args()
    mapping = json.loads(MAP.read_text()) if MAP.exists() else {}
    todo = [f for f in FILES if (a.force or f not in mapping) and (not a.only or f == a.only)]
    if a.dry_run:
        print("\n".join(todo) or "nothing to upload")
        return 0
    tok = token()
    for rel in todo:
        mapping[rel] = upload(tok, rel)
        MAP.write_text(json.dumps(mapping, indent=2) + "\n")
        print(f"✓ {rel}  →  {mapping[rel]}")
    print(f"{len(mapping)} files mapped in {MAP.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
