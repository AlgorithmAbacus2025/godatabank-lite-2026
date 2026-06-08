"""Template-based Summary Engine v0.1.

Scope:
- consume classified records only from data/classified/
- create one structured citation-backed summary JSON
- no AI, opinion, prediction, publishing, search, frontend, subscribers, databases, or extra institutions
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CLASSIFIED_DIR = PROJECT_ROOT / "data" / "classified"
SUMMARIES_DIR = PROJECT_ROOT / "data" / "summaries"
DEFAULT_CLASSIFIED_PATH = CLASSIFIED_DIR / "classified_world_bank_metadata_40107522.json"


class SummaryGenerationError(RuntimeError):
    """Raised when a classified record cannot produce a controlled summary."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_output_dir() -> None:
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)


def load_classified_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        record = json.load(file)

    if not isinstance(record, dict):
        raise SummaryGenerationError("classified record must be a JSON object")
    if record.get("classification_status") != "CLASSIFIED":
        raise SummaryGenerationError("Summary Engine v0.1 accepts classified records only")
    return record


def required_string(record: dict[str, Any], field: str) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise SummaryGenerationError(f"classified record missing required field: {field}")
    return value.strip()


def optional_string(record: dict[str, Any], *fields: str) -> str | None:
    for field in fields:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def output_path_for(document_id: str) -> Path:
    safe_document_id = document_id.strip().replace("/", "_")
    return SUMMARIES_DIR / f"summary_world_bank_metadata_{safe_document_id}.json"


def build_summary(record: dict[str, Any]) -> dict[str, Any]:
    institution = required_string(record, "institution")
    region = required_string(record, "region")
    sector = required_string(record, "sector")
    topic = required_string(record, "topic")
    source_url = required_string(record, "source_url")
    document_id = optional_string(record, "document_id", "source_document_id")
    title = optional_string(record, "title", "source_title")
    publication_date = optional_string(record, "publication_date", "source_publication_date")

    if document_id is None:
        raise SummaryGenerationError("classified record missing required field: document_id")
    if title is None:
        raise SummaryGenerationError("classified record missing required field: title")

    headline = f"{institution} metadata classified under {topic}"
    summary = (
        f"This classified metadata record is organised as {topic} within the {sector} sector "
        f"for the {region} region. The source title is: {title}"
    )

    key_findings = [
        f"Institution: {institution}",
        f"Region: {region}",
        f"Sector: {sector}",
        f"Topic: {topic}",
        f"Document ID: {document_id}",
    ]
    if publication_date is None:
        key_findings.append("Publication date: not present in the classified record")
    else:
        key_findings.append(f"Publication date: {publication_date}")

    citation_block = {
        "institution": institution,
        "title": title,
        "source_url": source_url,
        "publication_date": publication_date,
        "document_id": document_id,
        "classification_status": record.get("classification_status"),
        "classified_at_utc": record.get("classified_at_utc"),
    }

    return {
        "summary_status": "GENERATED",
        "schema_version": "summary.v0.1",
        "generated_at_utc": utc_now(),
        "headline": headline,
        "title": title,
        "summary": summary,
        "key_findings": key_findings,
        "institution": institution,
        "region": region,
        "sector": sector,
        "topic": topic,
        "source_url": source_url,
        "publication_date": publication_date,
        "document_id": document_id,
        "citation_block": citation_block,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generate_summary(input_path: Path = DEFAULT_CLASSIFIED_PATH) -> tuple[Path, dict[str, Any]]:
    ensure_output_dir()
    record = load_classified_record(input_path)
    summary = build_summary(record)
    output_path = output_path_for(summary["document_id"])
    write_json(output_path, summary)
    return output_path, summary


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    input_path = Path(args[0]).resolve() if args else DEFAULT_CLASSIFIED_PATH

    try:
        output_path, _ = generate_summary(input_path)
    except Exception as exc:
        print(json.dumps({"status": "FAILED", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1

    print(json.dumps({"status": "GENERATED", "output_path": str(output_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
