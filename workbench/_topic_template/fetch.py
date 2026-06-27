"""
ALIS-Lite topic fetch placeholder.

Purpose:
- Customise this file for one topic only.
- Fetch official or primary-source data after `story_scan.md` and `source_plan.md` are complete.
- Save raw evidence under `fetched/`.
- Save source/provenance records under `source_records/`.

Rules:
- Do not publish from this script.
- Do not write to `site/`.
- Do not overwrite existing evidence without deliberate review.
- Do not treat breaking news as evidence.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    print("ALIS-Lite fetch placeholder.")
    print("Customise this script for the specific topic before fetching.")
    print(f"Topic folder: {BASE_DIR}")


if __name__ == "__main__":
    main()