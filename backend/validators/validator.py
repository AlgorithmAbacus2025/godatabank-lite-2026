"""Validator v0.1 for ALIS metadata records.

Scope:
- validate one ALIS metadata JSON record
- approve or reject the record
- write approved records to data/validated/
- log validation results
- no Abacus, summarisation, search, publishing, subscriptions, or extra institutions
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    from . import schema
except ImportError:  # Allows direct execution: python backend/validators/validator.py
    import schema  # type: ignore


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ALIS_METADATA_PATH = PROJECT_ROOT / "data" / "raw" / "world_bank" / "latest_metadata.json"
VALIDATED_DIR = PROJECT_ROOT / "data" / "validated"
VALIDATION_LOG_PATH = VALIDATED_DIR / "validator.log"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_output_dir() -> None:
    VALIDATED_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("metadata record must be a JSON object")
    return data


def extract_document_id(metadata: dict[str, Any]) -> Any:
    for field in schema.ALIS_DOCUMENT_ID_FIELDS:
        value = metadata.get(field)
        if value is not None:
            return value
    return None


def canonicalise(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        "institution": metadata.get("institution"),
        "title": metadata.get("title"),
        "publication_date": metadata.get("publication_date"),
        "source_url": metadata.get("source_url"),
        "document_id": extract_document_id(metadata),
        "language": metadata.get("language"),
        "source_api_url": metadata.get("source_api_url"),
        "retrieved_at_utc": metadata.get("retrieved_at_utc"),
        "world_bank_record_key": metadata.get("world_bank_record_key"),
        "raw_record": metadata.get("raw_record"),
    }


def check_required_fields(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in schema.REQUIRED_FIELDS:
        value = record.get(field)
        if value is None:
            errors.append(f"missing required field: {field}")
        elif isinstance(value, str) and not value.strip():
            errors.append(f"empty required field: {field}")
    return errors


def check_schema_types(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field, expected_type in schema.FIELD_TYPES.items():
        value = record.get(field)
        if value is not None and not isinstance(value, expected_type):
            errors.append(f"field {field} must be {expected_type.__name__}")
    return errors


def check_publication_date(record: dict[str, Any]) -> list[str]:
    value = record.get("publication_date")
    if not isinstance(value, str) or not value.strip():
        return ["publication_date is required for date validation"]

    try:
        datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return ["publication_date must be a valid ISO date or datetime"]

    return []


def check_source_url(record: dict[str, Any]) -> list[str]:
    value = record.get("source_url")
    if not isinstance(value, str) or not value.strip():
        return ["source_url is required for URL validation"]

    parsed = urlparse(value.strip())
    if parsed.scheme not in {"http", "https"}:
        return ["source_url must use http or https"]
    if not parsed.netloc:
        return ["source_url must include a domain"]

    return []


def check_institution(record: dict[str, Any]) -> list[str]:
    value = record.get("institution")
    if not isinstance(value, str) or not value.strip():
        return ["institution is required for approval validation"]

    if value not in schema.APPROVED_INSTITUTIONS:
        return [f"institution is not approved: {value}"]

    return []


def check_world_bank_domain(record: dict[str, Any]) -> list[str]:
    institution = record.get("institution")
    source_url = record.get("source_url")

    if institution != "World Bank":
        return []
    if not isinstance(source_url, str):
        return ["World Bank source_url must be a string"]

    parsed = urlparse(source_url)
    hostname = parsed.hostname or ""
    approved_domains = schema.APPROVED_INSTITUTIONS["World Bank"]["domains"]
    if not any(hostname == domain or hostname.endswith(f".{domain}") for domain in approved_domains):
        return ["World Bank source_url must resolve to a worldbank.org domain"]

    return []


def validate_record(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_fields(record))
    errors.extend(check_schema_types(record))
    errors.extend(check_publication_date(record))
    errors.extend(check_source_url(record))
    errors.extend(check_institution(record))
    errors.extend(check_world_bank_domain(record))
    return errors


def approved_output_path(record: dict[str, Any]) -> Path:
    document_id = str(record["document_id"]).strip().replace("/", "_")
    return VALIDATED_DIR / f"approved_world_bank_metadata_{document_id}.json"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def log_validation(
    *,
    status: str,
    input_path: Path,
    output_path: Path | None,
    errors: list[str],
) -> None:
    ensure_output_dir()
    log_entry = {
        "timestamp": utc_now(),
        "status": status,
        "input_path": str(input_path),
        "output_path": str(output_path) if output_path else None,
        "errors": errors,
    }
    with VALIDATION_LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry, sort_keys=True) + "\n")


def validate_file(input_path: Path = DEFAULT_ALIS_METADATA_PATH) -> tuple[str, list[str], Path | None]:
    ensure_output_dir()
    metadata = load_json(input_path)
    record = canonicalise(metadata)
    errors = validate_record(record)

    if errors:
        log_validation(status=schema.REJECTED_STATUS, input_path=input_path, output_path=None, errors=errors)
        return schema.REJECTED_STATUS, errors, None

    output_path = approved_output_path(record)
    approved_record = {
        "validation_status": schema.APPROVED_STATUS,
        "validated_at_utc": utc_now(),
        "schema_version": "validator.v0.1",
        "metadata": record,
    }
    write_json(output_path, approved_record)
    log_validation(status=schema.APPROVED_STATUS, input_path=input_path, output_path=output_path, errors=[])
    return schema.APPROVED_STATUS, [], output_path


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    input_path = Path(args[0]).resolve() if args else DEFAULT_ALIS_METADATA_PATH

    try:
        status, errors, _ = validate_file(input_path)
    except Exception as exc:
        ensure_output_dir()
        log_validation(status=schema.REJECTED_STATUS, input_path=input_path, output_path=None, errors=[str(exc)])
        print(schema.REJECTED_STATUS)
        return 1

    print(status)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
