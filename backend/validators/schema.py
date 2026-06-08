"""Schema constants for Validator v0.1."""

from __future__ import annotations


APPROVED_INSTITUTIONS = {
    "World Bank": {
        "domains": ("worldbank.org",),
        "source": "ALIS v0.1 World Bank metadata connector",
    }
}

REQUIRED_FIELDS = (
    "institution",
    "title",
    "publication_date",
    "source_url",
    "document_id",
)

FIELD_TYPES = {
    "institution": str,
    "title": str,
    "publication_date": str,
    "source_url": str,
    "document_id": str,
}

ALIS_DOCUMENT_ID_FIELDS = (
    "document_id",
    "world_bank_document_id",
)

APPROVED_STATUS = "APPROVED"
REJECTED_STATUS = "REJECTED"
