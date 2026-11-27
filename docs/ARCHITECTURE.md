# Architecture orientation

Status: descriptive index, not a new architectural contract.

## Observed prototype
- `backend/alis/`: configuration, source registry helper and World Bank connector.
- `backend/validators/`: schema and validation.
- `backend/abacus/`: taxonomy and classification.
- `backend/summary/`: summary generation.
- `scripts/run_world_bank_pipeline.py`: pipeline runner.
- `sources/`, `data/`, `reports/`: source admission, evidence chain and generated outputs.
- `workbench/`: topic-level research material.
- `site/`: static publication output.
- `tests/alis/`: source registry test module.

This inventory describes tracked files; no runtime tests were executed during documentation cleanup.

## Documented target
The [boundary register v1.0-R1](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md) specifies Abacus (planning/analysis), Arya (source proposal/admission requests), Hermes (retrieval), Thoth (registry/provenance), Aegis (validation/gates), Vyasa (synthesis), Apollo (publication) and Argus (audit/monitoring). The [Thoth design](architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md) and [registry authority decision](reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md) define further boundaries. These are not claims that all eight engines exist as implemented packages.

The [migration plan](reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md) proposes separation between ALIS Core and GoDataBank product code. An adaptive agent may orchestrate deterministic tools in a future design; this is not an approved runtime change.
