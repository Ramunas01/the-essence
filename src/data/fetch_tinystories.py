"""Fetch a deduplicated 200-story sample from roneneldan/TinyStories (train split)."""

import hashlib
import json
import sys
from pathlib import Path

OUTPUT = Path(__file__).parent.parent.parent / "data" / "tinystories" / "sample-200.jsonl"
TARGET = 200
SOURCE = "roneneldan/TinyStories"
SPLIT = "train"


def text_hash(text: str) -> str:
    return hashlib.sha256(text.strip().encode()).hexdigest()


def fetch_sample():
    try:
        from datasets import load_dataset
    except ImportError:
        print("Install the 'datasets' package: pip install datasets", file=sys.stderr)
        sys.exit(1)

    ds = load_dataset(SOURCE, split=SPLIT, streaming=True, trust_remote_code=False)

    seen: set[str] = set()
    stories: list[dict] = []
    total_fetched = 0
    duplicates_dropped = 0

    for row in ds:
        if len(stories) >= TARGET:
            break
        total_fetched += 1
        raw = row.get("text", "")
        h = text_hash(raw)
        if h in seen:
            duplicates_dropped += 1
            continue
        seen.add(h)
        stories.append(raw)

    if len(stories) < TARGET:
        print(f"ERROR: only found {len(stories)} unique stories; wanted {TARGET}", file=sys.stderr)
        sys.exit(1)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        for i, text in enumerate(stories):
            record = {
                "id": i,
                "text": text,
                "n_chars": len(text),
                "source": SOURCE,
                "split": SPLIT,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Total fetched     : {total_fetched}")
    print(f"Duplicates dropped: {duplicates_dropped}")
    print(f"Final count       : {len(stories)}")
    print(f"Output            : {OUTPUT}")


if __name__ == "__main__":
    fetch_sample()
