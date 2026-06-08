"""Fetch, validate, store, and archive one World Bank publication metadata record.

ALIS v0.1 scope:
- official World Bank API only
- publication metadata only
- JSON file storage only
- no databases, AI summarisation, publishing, search, or subscriber systems
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from . import config
except ImportError:  # Allows direct execution: python backend/alis/world_bank_connector.py
    import config  # type: ignore


REQUIRED_FIELDS = ("title", "institution", "source_url", "publication_date")


class WorldBankConnectorError(RuntimeError):
    """Raised when ALIS cannot fetch, normalise, or validate metadata."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today_utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def ensure_directories() -> None:
    config.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    config.ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)


def build_request_url() -> str:
    params = {
        "format": "json",
        "rows": "1",
        "os": "0",
        "lang_exact": config.WORLD_BANK_LANGUAGE,
        "enddate": today_utc_date(),
        "fl": ",".join(config.WORLD_BANK_API_FIELDS),
    }
    return f"{config.WORLD_BANK_API_BASE_URL}?{urlencode(params)}"


def fetch_metadata_response(request_url: str) -> dict[str, Any]:
    request = Request(
        request_url,
        headers={
            "Accept": "application/json",
            "User-Agent": config.USER_AGENT,
        },
        method="GET",
    )
    with urlopen(request, timeout=config.DEFAULT_TIMEOUT_SECONDS) as response:
        if response.status != 200:
            raise WorldBankConnectorError(f"World Bank API returned HTTP {response.status}")
        return json.load(response)


def first_document(response_data: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    documents = response_data.get("documents")
    if not isinstance(documents, dict):
        raise WorldBankConnectorError("World Bank API response did not contain a documents object")

    for record_key, document in documents.items():
        if record_key == "facets":
            continue
        if isinstance(document, dict):
            return record_key, document

    raise WorldBankConnectorError("World Bank API response did not contain a publication record")


def first_doc_name(document: dict[str, Any]) -> str | None:
    docna = document.get("docna")
    if not isinstance(docna, dict):
        return None

    for value in docna.values():
        if isinstance(value, dict) and isinstance(value.get("docna"), str):
            return value["docna"].strip()

    return None


def canonical_source_url(document: dict[str, Any]) -> str | None:
    source_url = document.get("url") or document.get("pdfurl")
    if not isinstance(source_url, str) or not source_url.strip():
        return None

    source_url = source_url.strip()
    if source_url.startswith("http://documents.worldbank.org/"):
        return source_url.replace("http://", "https://", 1)
    return source_url


def normalise_metadata(
    record_key: str,
    document: dict[str, Any],
    request_url: str,
    response_data: dict[str, Any],
    retrieved_at_utc: str,
) -> dict[str, Any]:
    title = document.get("display_title") or first_doc_name(document)

    return {
        "title": title.strip() if isinstance(title, str) else None,
        "institution": config.WORLD_BANK_INSTITUTION,
        "source_url": canonical_source_url(document),
        "publication_date": document.get("docdt"),
        "document_id": document.get("id"),
        "language": document.get("lang"),
        "world_bank_record_key": record_key,
        "world_bank_document_id": document.get("id"),
        "source_api_url": request_url,
        "retrieved_at_utc": retrieved_at_utc,
        "api_response_context": {
            "rows": response_data.get("rows"),
            "os": response_data.get("os"),
            "page": response_data.get("page"),
            "total": response_data.get("total"),
        },
        "raw_record": document,
    }


def validate_publication_date(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def validate_metadata(metadata: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing or empty required field: {field}")

    if metadata.get("institution") != config.WORLD_BANK_INSTITUTION:
        errors.append("institution must be World Bank")

    source_url = metadata.get("source_url")
    if isinstance(source_url, str):
        if not source_url.startswith(("https://", "http://")):
            errors.append("source_url must be an HTTP URL")
        if "worldbank.org" not in source_url:
            errors.append("source_url must point to a worldbank.org domain")

    if not validate_publication_date(metadata.get("publication_date")):
        errors.append("publication_date must be a parseable ISO date or datetime")

    if metadata.get("language") != config.WORLD_BANK_LANGUAGE:
        errors.append("language must be English")

    return errors


def archive_path_for(metadata: dict[str, Any]) -> Path:
    timestamp = metadata["retrieved_at_utc"].replace("-", "").replace(":", "").replace("Z", "Z")
    record_key = str(metadata.get("world_bank_record_key") or "record").replace("/", "_")
    return config.ARCHIVE_DIR / f"world_bank_metadata_{record_key}_{timestamp}.json"


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def log_event(
    status: str,
    message: str,
    *,
    request_url: str | None = None,
    metadata_path: Path | None = None,
    archive_path: Path | None = None,
    validation_errors: list[str] | None = None,
) -> None:
    ensure_directories()
    entry = {
        "timestamp": utc_now(),
        "status": status,
        "message": message,
        "request_url": request_url,
        "metadata_path": str(metadata_path) if metadata_path else None,
        "archive_path": str(archive_path) if archive_path else None,
        "validation_errors": validation_errors or [],
    }
    with config.LOG_FILE_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(entry, sort_keys=True) + "\n")


def run() -> dict[str, Any]:
    ensure_directories()
    request_url = build_request_url()
    retrieved_at_utc = utc_now()

    response_data = fetch_metadata_response(request_url)
    record_key, document = first_document(response_data)
    metadata = normalise_metadata(record_key, document, request_url, response_data, retrieved_at_utc)

    validation_errors = validate_metadata(metadata)
    if validation_errors:
        log_event("failure", "metadata validation failed", request_url=request_url, validation_errors=validation_errors)
        raise WorldBankConnectorError("; ".join(validation_errors))

    archive_path = archive_path_for(metadata)
    write_json(config.LATEST_METADATA_PATH, metadata)
    write_json(archive_path, metadata)

    log_event(
        "success",
        "metadata fetched, validated, stored, and archived",
        request_url=request_url,
        metadata_path=config.LATEST_METADATA_PATH,
        archive_path=archive_path,
    )

    return {
        "status": "success",
        "metadata_path": str(config.LATEST_METADATA_PATH),
        "archive_path": str(archive_path),
        "log_path": str(config.LOG_FILE_PATH),
        "title": metadata["title"],
        "institution": metadata["institution"],
        "source_url": metadata["source_url"],
        "publication_date": metadata["publication_date"],
    }


def main() -> int:
    try:
        result = run()
    except Exception as exc:
        log_event("failure", str(exc))
        print(json.dumps({"status": "failure", "error": str(exc)}, indent=2), file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
