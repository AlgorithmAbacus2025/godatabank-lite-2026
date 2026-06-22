"""Thoth source registry helper for ALIS.

This helper normalises source metadata into Thoth-owned source identifiers.
JSON input is accepted only as transitional prototype data; it is not production
canonical registry state.

Deferred provenance, lineage, mutation-history, and checksum behaviour is
incomplete non-production behaviour until separately authorised.
"""

from dataclasses import dataclass, field
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional


ALLOWED_SOURCE_STATUSES = {
    "proposed",
    "admission_requested",
    "admitted",
    "active",
    "suspended",
    "deprecated",
    "retired",
    "rejected",
    "fixture_only",
    "prototype",
}

PRODUCTION_SOURCE_STATUSES = {
    "admitted",
    "active",
    "suspended",
    "deprecated",
    "retired",
    "rejected",
}

REQUIRED_PRODUCTION_REFS = (
    "admission_decision_ref",
    "admission_request_ref",
    "canonical_endpoint_ref",
    "provenance_record_id",
    "lineage_root_id",
    "schema_ref",
    "contract_ref",
    "checksum_policy_ref",
    "mutation_record_ref",
)

INCOMPLETE_NON_PRODUCTION_BEHAVIOUR = (
    "provenance, lineage, mutation-history, and checksum logic are incomplete; "
    "prototype entries are not production canonical registry state"
)


@dataclass(frozen=True)
class SourceRegistryEntry:
    """Minimum Thoth Source Registry Entry representation used by this helper."""

    registry_entry_id: str
    registry_entry_version: str
    source_key: str
    source_name: str
    source_owner: str
    source_type: str
    source_status: str
    admission_decision_ref: Optional[str] = None
    admission_request_ref: Optional[str] = None
    canonical_endpoint_ref: Optional[str] = None
    provenance_record_id: Optional[str] = None
    lineage_root_id: Optional[str] = None
    schema_ref: Optional[str] = None
    contract_ref: Optional[str] = None
    checksum_policy_ref: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_by_engine: str = "unknown"
    owning_engine: str = "Thoth"
    mutation_record_ref: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    incomplete_non_production_reason: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary form without promoting metadata to authority."""
        data = dict(self.metadata)
        data.update(
            {
                "registry_entry_id": self.registry_entry_id,
                "registry_entry_version": self.registry_entry_version,
                "source_key": self.source_key,
                "source_name": self.source_name,
                "source_owner": self.source_owner,
                "source_type": self.source_type,
                "source_status": self.source_status,
                "admission_decision_ref": self.admission_decision_ref,
                "admission_request_ref": self.admission_request_ref,
                "canonical_endpoint_ref": self.canonical_endpoint_ref,
                "provenance_record_id": self.provenance_record_id,
                "lineage_root_id": self.lineage_root_id,
                "schema_ref": self.schema_ref,
                "contract_ref": self.contract_ref,
                "checksum_policy_ref": self.checksum_policy_ref,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "created_by_engine": self.created_by_engine,
                "owning_engine": self.owning_engine,
                "mutation_record_ref": self.mutation_record_ref,
                "incomplete_non_production_reason": (
                    self.incomplete_non_production_reason
                ),
            }
        )
        data.setdefault("short_name", self.source_key)
        return data


class SourceRegistry:
    """Read-only Thoth registry metadata helper.

    This class does not retrieve network resources, decide Aegis policy gates,
    run Arya source-admission workflows, perform analytics, render output,
    publish artifacts, or emit observability/audit events.
    """

    def __init__(
        self,
        json_path: Optional[str] = None,
        entries: Optional[Iterable[Mapping[str, Any]]] = None,
    ):
        """Initialise from explicit entries or transitional prototype JSON."""
        if json_path and entries is not None:
            raise ValueError("Provide either json_path or entries, not both")

        self.json_path = Path(json_path) if json_path else None
        raw_sources = list(entries) if entries is not None else []
        if self.json_path:
            raw_sources = self._load_prototype_json(self.json_path)

        self.entries = [self._entry_from_mapping(source) for source in raw_sources]
        self.sources = [entry.to_dict() for entry in self.entries]

    def list_sources(self) -> List[str]:
        """Return Thoth-owned source identifiers."""
        return [entry.registry_entry_id for entry in self.entries]

    def get_source_by_id(self, registry_entry_id: str) -> Optional[Dict[str, Any]]:
        """Return source metadata by Thoth-owned registry entry identifier."""
        for source in self.sources:
            if source.get("registry_entry_id") == registry_entry_id:
                return source
        return None

    def get_source_by_short_name(self, short_name: str) -> Optional[Dict[str, Any]]:
        """Return metadata by legacy alias; this is not canonical authority."""
        for source in self.sources:
            aliases = source.get("aliases") or []
            if short_name in {
                source.get("short_name"),
                source.get("source_key"),
                *aliases,
            }:
                return source
        return None

    def filter_sources(
        self,
        indicator_category: Optional[str] = None,
        geography: Optional[str] = None,
        group: Optional[str] = None,
        publication_type: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Return read-only metadata matches without deciding admission policy."""
        results = self.sources
        if indicator_category:
            results = [
                source
                for source in results
                if indicator_category in source.get("indicator_categories", [])
            ]
        if geography:
            results = [
                source
                for source in results
                if geography in str(source.get("geography", ""))
            ]
        if group:
            results = [
                source for source in results if group in source.get("groups", [])
            ]
        if publication_type:
            results = [
                source
                for source in results
                if publication_type in source.get("publication_types", [])
            ]
        return results

    def validate_source_access(self, source_ref: str) -> bool:
        """Fail closed on metadata availability; this is not an Aegis gate."""
        source = self.get_source_by_id(source_ref) or self.get_source_by_short_name(
            source_ref
        )
        if not source:
            return False
        if source.get("source_status") not in {"admitted", "active"}:
            return False
        return source.get("access_type", "public") == "public"

    def get_all_groups(self) -> List[str]:
        """Return unique read-only group tags."""
        groups = set()
        for source in self.sources:
            groups.update(source.get("groups", []))
        return sorted(groups)

    def _load_prototype_json(self, json_path: Path) -> List[Mapping[str, Any]]:
        if not json_path.exists():
            raise FileNotFoundError(f"Source registry file not found: {json_path}")

        with json_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        raw_sources = data.get("sources")
        if not isinstance(raw_sources, list):
            raise ValueError("Prototype source registry JSON must contain sources list")
        return raw_sources

    def _entry_from_mapping(
        self, source: Mapping[str, Any]
    ) -> SourceRegistryEntry:
        source_key = self._required_text(
            source, "source_key", fallback_key="short_name"
        )
        source_name = self._text(
            source, "source_name", fallback_key="organisation"
        ) or source_key
        source_owner = self._text(
            source, "source_owner", fallback_key="organisation"
        ) or "unknown"
        registry_entry_id = self._text(source, "registry_entry_id")
        if not registry_entry_id:
            registry_entry_id = f"thoth:prototype-source:{self._normalise_key(source_key)}"

        source_status = self._text(source, "source_status") or "prototype"
        if source_status not in ALLOWED_SOURCE_STATUSES:
            raise ValueError(f"Unsupported Thoth source status: {source_status}")
        if not self._is_thoth_identifier(registry_entry_id):
            raise ValueError("Registry entry id must be Thoth-owned")

        values = {
            "admission_decision_ref": self._text(source, "admission_decision_ref"),
            "admission_request_ref": self._text(source, "admission_request_ref"),
            "canonical_endpoint_ref": self._text(source, "canonical_endpoint_ref"),
            "provenance_record_id": self._text(source, "provenance_record_id"),
            "lineage_root_id": self._text(source, "lineage_root_id"),
            "schema_ref": self._text(source, "schema_ref"),
            "contract_ref": self._text(source, "contract_ref"),
            "checksum_policy_ref": self._text(source, "checksum_policy_ref"),
            "mutation_record_ref": self._text(source, "mutation_record_ref"),
        }
        if source_status in PRODUCTION_SOURCE_STATUSES:
            self._validate_required_refs(values)

        reason = None
        if source_status in {"prototype", "fixture_only"}:
            reason = INCOMPLETE_NON_PRODUCTION_BEHAVIOUR

        return SourceRegistryEntry(
            registry_entry_id=registry_entry_id,
            registry_entry_version=self._text(source, "registry_entry_version")
            or "prototype-0",
            source_key=source_key,
            source_name=source_name,
            source_owner=source_owner,
            source_type=self._text(source, "source_type") or "unknown",
            source_status=source_status,
            created_at=self._text(source, "created_at"),
            updated_at=self._text(source, "updated_at"),
            created_by_engine=self._text(source, "created_by_engine") or "unknown",
            owning_engine=self._text(source, "owning_engine") or "Thoth",
            metadata=dict(source),
            incomplete_non_production_reason=reason,
            **values,
        )

    def _validate_required_refs(self, values: Mapping[str, Optional[str]]) -> None:
        missing = [
            field_name
            for field_name in REQUIRED_PRODUCTION_REFS
            if not values.get(field_name)
        ]
        if missing:
            raise ValueError(
                "Production registry entries require references: "
                + ", ".join(sorted(missing))
            )

    def _required_text(
        self,
        source: Mapping[str, Any],
        key: str,
        fallback_key: Optional[str] = None,
    ) -> str:
        value = self._text(source, key, fallback_key=fallback_key)
        if not value:
            raise ValueError(f"Source registry entry requires {key}")
        return value

    def _text(
        self,
        source: Mapping[str, Any],
        key: str,
        fallback_key: Optional[str] = None,
    ) -> Optional[str]:
        value = source.get(key)
        if value in (None, "") and fallback_key:
            value = source.get(fallback_key)
        if value in (None, ""):
            return None
        return str(value)

    def _normalise_key(self, value: str) -> str:
        key = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
        if not key:
            raise ValueError("Source key cannot produce a Thoth identifier")
        return key

    def _is_thoth_identifier(self, value: str) -> bool:
        return value.startswith(("thoth:source:", "thoth:prototype-source:"))
