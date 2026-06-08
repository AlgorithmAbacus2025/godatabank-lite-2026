"""Abacus v0.1 deterministic classifier.

Scope:
- consume validated metadata records only
- classify by fixed taxonomy rules
- store classification output under data/classified/
- no AI summarisation, opinion, prediction, search, publishing, subscriptions, or extra institutions
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from . import taxonomy
except ImportError:  # Allows direct execution: python backend/abacus/classifier.py
    import taxonomy  # type: ignore


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VALIDATED_PATH = PROJECT_ROOT / "data" / "validated" / "approved_world_bank_metadata_40107522.json"
CLASSIFIED_DIR = PROJECT_ROOT / "data" / "classified"


class ClassificationError(RuntimeError):
    """Raised when a record cannot be classified inside Abacus v0.1 rules."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_output_dir() -> None:
    CLASSIFIED_DIR.mkdir(parents=True, exist_ok=True)


def load_validated_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        record = json.load(file)

    if not isinstance(record, dict):
        raise ClassificationError("validated record must be a JSON object")
    if record.get("validation_status") != "APPROVED":
        raise ClassificationError("Abacus v0.1 accepts approved Validator records only")
    metadata = record.get("metadata")
    if not isinstance(metadata, dict):
        raise ClassificationError("validated record must contain a metadata object")
    return record


def normalise_text(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower())).strip()


def metadata_text(metadata: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("title", "source_url", "document_id", "world_bank_record_key"):
        value = metadata.get(key)
        if isinstance(value, str):
            parts.append(value)

    raw_record = metadata.get("raw_record")
    if isinstance(raw_record, dict):
        for key in ("display_title", "docdt", "url", "pdfurl"):
            value = raw_record.get(key)
            if isinstance(value, str):
                parts.append(value)

    return normalise_text(" ".join(parts))


def keyword_matches(text: str, keywords: tuple[str, ...]) -> list[str]:
    matches: list[str] = []
    padded_text = f" {text} "
    for keyword in keywords:
        normalised_keyword = normalise_text(keyword)
        if f" {normalised_keyword} " in padded_text:
            matches.append(keyword)
    return matches


def choose_category(text: str, rules: tuple[tuple[str, tuple[str, ...]], ...], fallback: str) -> tuple[str, list[str]]:
    best_category = fallback
    best_matches: list[str] = []

    for category, keywords in rules:
        matches = keyword_matches(text, keywords)
        if len(matches) > len(best_matches):
            best_category = category
            best_matches = matches

    return best_category, best_matches


def derive_keywords(title: str, matched_terms: list[str]) -> list[str]:
    keywords: list[str] = []

    for term in matched_terms:
        normalised = normalise_text(term)
        if normalised and normalised not in keywords:
            keywords.append(normalised)

    for token in normalise_text(title).split():
        if len(token) < 3:
            continue
        if token in taxonomy.STOPWORDS:
            continue
        if token not in keywords:
            keywords.append(token)

    return keywords[:16]


def slug(value: str) -> str:
    return normalise_text(value).replace(" ", "-")


def build_tags(institution: str, region: str, sector: str, topic: str, document_id: str) -> list[str]:
    return [
        slug(institution),
        slug(region),
        slug(sector),
        slug(topic),
        f"document-{slug(document_id)}",
        "validated-metadata",
    ]


def classify_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    institution = metadata.get("institution")
    title = metadata.get("title")
    document_id = metadata.get("document_id")

    if not isinstance(institution, str) or not institution.strip():
        raise ClassificationError("metadata.institution is required")
    if not isinstance(title, str) or not title.strip():
        raise ClassificationError("metadata.title is required")
    if not isinstance(document_id, str) or not document_id.strip():
        raise ClassificationError("metadata.document_id is required")
    if institution != "World Bank":
        raise ClassificationError("Abacus v0.1 does not classify additional institutions")

    text = metadata_text(metadata)
    region, region_terms = choose_category(text, taxonomy.REGION_RULES, "Global")
    sector, sector_terms = choose_category(text, taxonomy.SECTOR_RULES, "Governance")
    topic, topic_terms = choose_category(text, taxonomy.TOPIC_RULES, sector)

    matched_terms = region_terms + sector_terms + topic_terms
    keywords = derive_keywords(title, matched_terms)

    return {
        "institution": institution,
        "region": region,
        "sector": sector,
        "topic": topic,
        "keywords": keywords,
        "tags": build_tags(institution, region, sector, topic, document_id),
    }


def classified_output_path(metadata: dict[str, Any]) -> Path:
    document_id = str(metadata["document_id"]).strip().replace("/", "_")
    return CLASSIFIED_DIR / f"classified_world_bank_metadata_{document_id}.json"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def classify_file(input_path: Path = DEFAULT_VALIDATED_PATH) -> tuple[Path, dict[str, Any]]:
    ensure_output_dir()
    validated_record = load_validated_record(input_path)
    metadata = validated_record["metadata"]
    classification = classify_metadata(metadata)
    output_path = classified_output_path(metadata)

    output = {
        **classification,
        "classification_status": "CLASSIFIED",
        "classified_at_utc": utc_now(),
        "schema_version": "abacus.v0.1",
        "source_validated_path": str(input_path),
        "title": metadata["title"],
        "publication_date": metadata.get("publication_date"),
        "document_id": metadata["document_id"],
        "source_document_id": metadata["document_id"],
        "source_title": metadata["title"],
        "source_url": metadata.get("source_url"),
    }
    write_json(output_path, output)
    return output_path, output


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    input_path = Path(args[0]).resolve() if args else DEFAULT_VALIDATED_PATH

    try:
        output_path, _ = classify_file(input_path)
    except Exception as exc:
        print(json.dumps({"status": "FAILED", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1

    print(json.dumps({"status": "CLASSIFIED", "output_path": str(output_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
