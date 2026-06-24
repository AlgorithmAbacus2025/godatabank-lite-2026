"""Validator v0.1 for ALIS metadata records.

Scope:
- validate one ALIS metadata JSON record
- approve or reject the record
- write approved records to data/validated/
- log validation results
- no Abacus, summarisation, search, publishing, subscriptions, or institutions beyond approved scope
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
DEFAULT_SOURCE_ADMISSION_PATH = PROJECT_ROOT / "sources" / "world_bank_source_admission.json"
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


def repository_relative_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError as exc:
        raise ValueError(f"path must be inside project root: {path}") from exc


def extract_document_id(metadata: dict[str, Any]) -> Any:
    for field in schema.ALIS_DOCUMENT_ID_FIELDS:
        value = metadata.get(field)
        if value is not None:
            return value
    return None


def canonicalise(
    metadata: dict[str, Any],
    source_admission: dict[str, Any],
) -> dict[str, Any]:
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
        "source_id": source_admission.get("source_id"),
        "institution_type": source_admission.get("institution_type"),
        "source_admission_status": source_admission.get("admission_status"),
        "source_verification_status": source_admission.get("verification_status"),
        "source_admission_decision_date": source_admission.get("admission_decision_date"),
        "source_admission_reviewer": source_admission.get("reviewer_or_admitting_agent"),
        "citation_metadata_status": source_admission.get("citation_metadata_status"),
        "licence_or_terms_url": source_admission.get("licence_or_terms_url"),
        "licence_or_terms_note": source_admission.get("licence_or_terms_note"),
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


def check_source_admission(
    admission: dict[str, Any],
    metadata: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    for field in schema.SOURCE_ADMISSION_REQUIRED_FIELDS:
        if field not in admission:
            errors.append(f"source admission missing required field: {field}")

    for field in schema.SOURCE_ADMISSION_REQUIRED_STRING_FIELDS:
        value = admission.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"source admission missing required string field: {field}")

    if admission.get("source_id") != schema.WORLD_BANK_SOURCE_ID:
        errors.append("source admission source_id is not the approved World Bank source id")
    if admission.get("institution_name") != "World Bank":
        errors.append("source admission institution name must be World Bank")
    if metadata.get("institution") != "World Bank":
        errors.append("metadata institution must be World Bank")
    if admission.get("institution_name") != metadata.get("institution"):
        errors.append("source admission institution does not match metadata institution")
    if admission.get("admission_status") != schema.ADMITTED_SOURCE_STATUS:
        errors.append("source admission status must be admitted")
    if admission.get("verification_status") != schema.VERIFIED_SOURCE_STATUS:
        errors.append("source verification status must be verified")
    if admission.get("citation_metadata_status") != "complete":
        errors.append("source admission citation metadata status must be complete")

    decision_date = admission.get("admission_decision_date")
    if isinstance(decision_date, str):
        try:
            datetime.fromisoformat(decision_date)
        except ValueError:
            errors.append("source admission decision date must be a valid ISO date")

    evidence_retrieved_at = admission.get("admission_evidence_retrieved_at_utc")
    if evidence_retrieved_at != metadata.get("retrieved_at_utc"):
        errors.append("source admission evidence timestamp must match raw retrieval timestamp")

    official_url = admission.get("official_source_url")
    source_url = metadata.get("source_url")
    approved_domains = schema.APPROVED_INSTITUTIONS.get("World Bank", {}).get("domains", ())

    if isinstance(official_url, str):
        official_host = urlparse(official_url).hostname or ""
        if not official_host:
            errors.append("source admission official URL must include a domain")
        elif not any(official_host == domain or official_host.endswith(f".{domain}") for domain in approved_domains):
            errors.append("source admission official_source_url must resolve to a worldbank.org domain")

    if isinstance(source_url, str):
        source_host = urlparse(source_url).hostname or ""
        if not source_host:
            errors.append("metadata source URL must include a domain")
        elif not any(source_host == domain or source_host.endswith(f".{domain}") for domain in approved_domains):
            errors.append("metadata source URL must resolve to a worldbank.org domain")

    if isinstance(official_url, str) and isinstance(source_url, str):
        official_host = urlparse(official_url).hostname or ""
        source_host = urlparse(source_url).hostname or ""
        if official_host and source_host and not (
            source_host == official_host
            or source_host.endswith(f".{official_host}")
            or official_host.endswith(f".{source_host}")
        ):
            errors.append("metadata source URL does not match admitted official source domain")

    admitted_api_url = admission.get("machine_readable_access_url")
    source_api_url = metadata.get("source_api_url")

    if admitted_api_url != "https://search.worldbank.org/api/v3/wds":
        errors.append("source admission machine_readable_access_url does not match approved World Bank Documents & Reports API endpoint")

    if not isinstance(admitted_api_url, str) or not isinstance(source_api_url, str):
        errors.append("source admission and metadata API URLs must be strings")
    elif not (
        source_api_url == admitted_api_url
        or source_api_url.startswith(f"{admitted_api_url}?")
    ):
        errors.append("metadata source API URL does not match admitted API endpoint")

    # Exclusion Policy checks
    institution_type = admission.get("institution_type")
    if institution_type in ("news_organisations", "commercial_data_vendors", "think_tanks", "blogs", "social_media", "user_generated_content", "advocacy_organisations", "lobbying_organisations"):
        errors.append("source admission institution type conflicts with the exclusion policy")

    excluded_terms = ["blog", "news", "lobby", "forum", "opinion", "advocacy", "thinktank"]
    for term in excluded_terms:
        if term in (admission.get("source_id") or "").lower() or term in (admission.get("institution_name") or "").lower():
            errors.append(f"source admission conflicts with the exclusion policy: contains term '{term}'")

    return errors


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
    institution = record.get("institution")
    if institution == "World Bank":
        prefix = "world_bank"
    elif institution == "Office for National Statistics":
        prefix = "ons"
    else:
        prefix = "metadata"
    return VALIDATED_DIR / f"approved_{prefix}_metadata_{document_id}.json"


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


def validate_file(
    input_path: Path = DEFAULT_ALIS_METADATA_PATH,
    source_admission_path: Path = DEFAULT_SOURCE_ADMISSION_PATH,
) -> tuple[str, list[str], Path | None]:
    ensure_output_dir()
    if not source_admission_path.exists():
        errors = [f"source admission file is missing: {source_admission_path}"]
        log_validation(status=schema.REJECTED_STATUS, input_path=input_path, output_path=None, errors=errors)
        return schema.REJECTED_STATUS, errors, None

    metadata = load_json(input_path)
    source_admission = load_json(source_admission_path)
    record = canonicalise(metadata, source_admission)
    errors = check_source_admission(source_admission, metadata)
    errors.extend(validate_record(record))

    if errors:
        log_validation(status=schema.REJECTED_STATUS, input_path=input_path, output_path=None, errors=errors)
        return schema.REJECTED_STATUS, errors, None

    output_path = approved_output_path(record)
    approved_record = {
        "validation_status": schema.APPROVED_STATUS,
        "validated_at_utc": utc_now(),
        "schema_version": "validator.v0.1",
        "source_raw_path": repository_relative_path(input_path),
        "source_admission_path": repository_relative_path(source_admission_path),
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
