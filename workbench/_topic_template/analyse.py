"""
ALIS-Lite topic analysis placeholder.

Purpose:
- Customise this file only after raw evidence and source records exist.
- Read evidence from `fetched/`.
- Read source/provenance records from `source_records/`.
- Save analysis outputs under `analysis/`.

Rules:
- Do not analyse before the evidence chain exists.
- Do not publish from this script.
- Do not write to `site/`.
- Record claim boundaries in `verification.md`.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    print("ALIS-Lite analysis placeholder.")
    print("Customise this script after evidence exists for the topic.")
    print(f"Topic folder: {BASE_DIR}")


if __name__ == "__main__":
    main()