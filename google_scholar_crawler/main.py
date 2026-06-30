from scholarly import ProxyGenerator, scholarly
import json
import os
import sys
import time
from datetime import datetime

RETRY_DELAYS_SECONDS = (10, 20, 30, 45, 60, 90)


def setup_proxy(use_proxy: bool) -> None:
    if not use_proxy:
        scholarly.use_proxy(ProxyGenerator())
        return

    pg = ProxyGenerator()
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("Using free proxy.", file=sys.stderr)
    else:
        print("Free proxy unavailable; retrying without proxy.", file=sys.stderr)
        scholarly.use_proxy(ProxyGenerator())


def fetch_author(scholar_id: str) -> dict:
    last_error = None

    for attempt, delay in enumerate(RETRY_DELAYS_SECONDS, start=1):
        try:
            setup_proxy(use_proxy=attempt >= 3)
            print(f"Attempt {attempt}/{len(RETRY_DELAYS_SECONDS)}...", file=sys.stderr)

            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(
                author,
                sections=["basics", "indices", "counts", "publications"],
            )

            if not author.get("name") or author.get("citedby") is None:
                raise ValueError("Incomplete Scholar profile (likely blocked by anti-bot page).")

            return author
        except Exception as exc:
            last_error = exc
            print(f"Attempt {attempt} failed: {exc}", file=sys.stderr)
            if attempt < len(RETRY_DELAYS_SECONDS):
                time.sleep(delay)

    raise RuntimeError(
        f"Failed to fetch Google Scholar data after {len(RETRY_DELAYS_SECONDS)} attempts: {last_error}"
    )


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise EnvironmentError("GOOGLE_SCHOLAR_ID is not set.")

    author = fetch_author(scholar_id)
    author["updated"] = str(datetime.now())
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author["publications"]
    }

    print(json.dumps(author, indent=2))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
