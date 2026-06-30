from scholarly import ProxyGenerator, scholarly
import json
import os
import sys
import time
from copy import deepcopy
from datetime import datetime

import requests
from bs4 import BeautifulSoup

RETRY_DELAYS_SECONDS = (10, 20, 30, 45, 60, 90)
SNAPSHOT_PATH = "results/gs_data.json"
SHIELDIO_PATH = "results/gs_data_shieldsio.json"
SCHOLAR_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}


def load_snapshot() -> dict | None:
    if not os.path.exists(SNAPSHOT_PATH):
        return None
    with open(SNAPSHOT_PATH, encoding="utf-8") as handle:
        return json.load(handle)


def normalize_publications(author: dict) -> dict:
    publications = author.get("publications", {})
    if isinstance(publications, list):
        author["publications"] = {
            item["author_pub_id"]: item for item in publications if item.get("author_pub_id")
        }
    return author


def fetch_via_scholarly(scholar_id: str) -> dict:
    last_error = None

    for attempt, delay in enumerate(RETRY_DELAYS_SECONDS, start=1):
        try:
            if attempt >= 4:
                pg = ProxyGenerator()
                if pg.FreeProxies():
                    scholarly.use_proxy(pg)
                    print("Using free proxy.", file=sys.stderr)

            print(f"Scholarly attempt {attempt}/{len(RETRY_DELAYS_SECONDS)}...", file=sys.stderr)
            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(
                author,
                sections=["basics", "indices", "counts", "publications"],
            )

            if not author.get("name") or author.get("citedby") is None:
                raise ValueError("Incomplete Scholar profile (likely blocked by anti-bot page).")

            return normalize_publications(author)
        except Exception as exc:
            last_error = exc
            print(f"Scholarly attempt {attempt} failed: {exc}", file=sys.stderr)
            if attempt < len(RETRY_DELAYS_SECONDS):
                time.sleep(delay)

    raise RuntimeError(
        f"Scholarly fetch failed after {len(RETRY_DELAYS_SECONDS)} attempts: {last_error}"
    )


def fetch_via_http(scholar_id: str, existing: dict | None = None) -> dict | None:
    url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en&oi=ao"
    print(f"Trying HTTP fallback: {url}", file=sys.stderr)

    try:
        response = requests.get(url, headers=SCHOLAR_HEADERS, timeout=60)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"HTTP fallback request failed: {exc}", file=sys.stderr)
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    name_el = soup.find("div", id="gsc_prf_in")
    stats = soup.select("td.gsc_rsb_std")

    if not name_el or len(stats) < 3:
        print("HTTP fallback could not parse Scholar profile page.", file=sys.stderr)
        return None

    author = deepcopy(existing) if existing else {}
    author.update(
        {
            "scholar_id": scholar_id,
            "name": name_el.get_text(strip=True),
            "citedby": int(stats[0].get_text(strip=True).replace(",", "")),
            "hindex": int(stats[1].get_text(strip=True).replace(",", "")),
            "i10index": int(stats[2].get_text(strip=True).replace(",", "")),
            "publications": author.get("publications", {}),
        }
    )
    return author


def write_outputs(author: dict) -> None:
    os.makedirs("results", exist_ok=True)

    with open(SNAPSHOT_PATH, "w", encoding="utf-8") as handle:
        json.dump(author, handle, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open(SHIELDIO_PATH, "w", encoding="utf-8") as handle:
        json.dump(shieldio_data, handle, ensure_ascii=False)


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise EnvironmentError("GOOGLE_SCHOLAR_ID is not set.")

    existing = load_snapshot()
    author = None
    crawl_status = "failed"

    try:
        author = fetch_via_scholarly(scholar_id)
        crawl_status = "scholarly"
    except Exception as exc:
        print(f"Scholarly crawl failed: {exc}", file=sys.stderr)
        author = fetch_via_http(scholar_id, existing)
        if author:
            crawl_status = "http_fallback"

    if author is None and existing:
        author = existing
        crawl_status = "cached"

    if author is None:
        raise RuntimeError("No Scholar data available from crawl, HTTP fallback, or cache.")

    author["updated"] = str(datetime.now())
    author["crawl_status"] = crawl_status
    author = normalize_publications(author)

    print(json.dumps(author, indent=2))
    write_outputs(author)

    if crawl_status != "scholarly":
        print(
            f"Warning: used {crawl_status} data instead of a full Scholarly crawl.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
