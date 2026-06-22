import json

import pytest

from backend.alis.source_registry import SourceRegistry, SourceRegistryEntry


def _required_refs():
    return {
        "admission_decision_ref": "aegis:decision:001",
        "admission_request_ref": "arya:request:001",
        "canonical_endpoint_ref": "thoth:endpoint:001",
        "provenance_record_id": "thoth:provenance:001",
        "lineage_root_id": "thoth:lineage:001",
        "schema_ref": "thoth:schema:source-registry-entry:v1",
        "contract_ref": "alis:contract:thoth-registry:v1",
        "checksum_policy_ref": "thoth:checksum-policy:001",
        "mutation_record_ref": "thoth:mutation:001",
    }


def _entry(**overrides):
    entry = {
        "registry_entry_id": "thoth:source:ons",
        "registry_entry_version": "1",
        "source_key": "ons",
        "source_name": "Office for National Statistics",
        "source_owner": "ONS",
        "source_type": "official-statistics-provider",
        "source_status": "active",
        "access_type": "public",
        "groups": ["G7"],
        "indicator_categories": ["Economy & Trade"],
        "publication_types": ["CSV"],
        "geography": "UK",
    }
    entry.update(_required_refs())
    entry.update(overrides)
    return entry


def test_source_registry_entry_construction():
    entry = SourceRegistryEntry(
        registry_entry_id="thoth:source:ons",
        registry_entry_version="1",
        source_key="ons",
        source_name="Office for National Statistics",
        source_owner="ONS",
        source_type="official-statistics-provider",
        source_status="active",
        metadata={"short_name": "ONS"},
        **_required_refs(),
    )

    assert entry.registry_entry_id == "thoth:source:ons"
    assert entry.source_key == "ons"
    assert entry.owning_engine == "Thoth"


def test_source_registry_entry_to_dict_serializes_required_fields():
    entry = SourceRegistryEntry(
        registry_entry_id="thoth:source:ons",
        registry_entry_version="1",
        source_key="ons",
        source_name="Office for National Statistics",
        source_owner="ONS",
        source_type="official-statistics-provider",
        source_status="active",
        metadata={"short_name": "ONS"},
        **_required_refs(),
    )

    serialized = entry.to_dict()

    assert serialized["registry_entry_id"] == "thoth:source:ons"
    assert serialized["source_key"] == "ons"
    assert serialized["short_name"] == "ONS"
    assert serialized["contract_ref"] == "alis:contract:thoth-registry:v1"


def test_source_registry_initializes_from_in_memory_entries():
    registry = SourceRegistry(entries=[_entry()])

    assert registry.list_sources() == ["thoth:source:ons"]
    assert registry.get_source_by_id("thoth:source:ons")["source_owner"] == "ONS"


def test_rejects_non_thoth_source_ids():
    with pytest.raises(ValueError, match="Thoth-owned"):
        SourceRegistry(entries=[_entry(registry_entry_id="external:source:ons")])


def test_accepts_thoth_source_and_prototype_source_id_prefixes():
    registry = SourceRegistry(
        entries=[
            _entry(registry_entry_id="thoth:source:ons"),
            {
                "registry_entry_id": "thoth:prototype-source:world-bank",
                "source_key": "world-bank",
                "source_name": "World Bank",
                "source_owner": "World Bank",
                "source_type": "prototype",
                "source_status": "prototype",
            },
        ]
    )

    assert registry.list_sources() == [
        "thoth:source:ons",
        "thoth:prototype-source:world-bank",
    ]


def test_production_entries_fail_closed_without_required_references():
    incomplete = _entry()
    incomplete.pop("provenance_record_id")

    with pytest.raises(ValueError, match="provenance_record_id"):
        SourceRegistry(entries=[incomplete])


@pytest.mark.parametrize("status", ["active", "admitted"])
def test_validate_source_access_true_only_for_active_or_admitted_public_entries(
    status,
):
    registry = SourceRegistry(entries=[_entry(source_status=status)])

    assert registry.validate_source_access("thoth:source:ons") is True
    assert registry.validate_source_access("ons") is True


@pytest.mark.parametrize(
    "entry",
    [
        _entry(source_status="deprecated"),
        _entry(access_type="private"),
        {
            "registry_entry_id": "thoth:prototype-source:ons",
            "source_key": "ons",
            "source_name": "Office for National Statistics",
            "source_owner": "ONS",
            "source_type": "prototype",
            "source_status": "prototype",
            "access_type": "public",
        },
    ],
)
def test_validate_source_access_false_for_inactive_non_public_or_incomplete_entries(
    entry,
):
    registry = SourceRegistry(entries=[entry])

    assert registry.validate_source_access("ons") is False


def test_validate_source_access_false_for_missing_entry():
    registry = SourceRegistry(entries=[_entry()])

    assert registry.validate_source_access("missing") is False


def test_loads_prototype_json_from_temporary_test_data(tmp_path):
    registry_file = tmp_path / "source_registry.json"
    registry_file.write_text(
        json.dumps(
            {
                "sources": [
                    {
                        "short_name": "ONS",
                        "organisation": "Office for National Statistics",
                        "access_type": "public",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    registry = SourceRegistry(str(registry_file))

    assert registry.list_sources() == ["thoth:prototype-source:ons"]
    assert registry.validate_source_access("ONS") is False


def test_helper_exposes_no_network_database_or_mutation_operations():
    registry = SourceRegistry(entries=[_entry()])

    for forbidden_name in (
        "fetch",
        "retrieve",
        "connect",
        "admit_source",
        "mutate",
        "save",
    ):
        assert not hasattr(registry, forbidden_name)
