# ENGINE v0.1 Review

## 1. Executive Summary

ENGINE v0.1 is the first complete GoDataBank evidence engine. Its purpose is to retrieve official metadata, verify required evidence fields, organise the record into a deterministic taxonomy, and generate a controlled citation-backed summary without inventing facts.

The current engine demonstrates the core GoDataBank principle:

```text
Truth is retrieved, not generated.
```

ENGINE v0.1 is intentionally narrow. It uses one official institution, the World Bank, and one official metadata path. It proves the evidence chain from official source retrieval through validation, classification, contract preservation, and template-based summary generation.

## 2. Architecture Overview

The current evidence path is:

```text
World Bank
|
v
ALIS
|
v
Validator
|
v
Abacus
|
v
Summary Engine
```

Stage responsibilities:

- World Bank provides the official source metadata.
- ALIS fetches, normalises, stores, archives, and logs metadata.
- Validator verifies mandatory evidence fields and approves or rejects the record.
- Abacus classifies approved metadata into institution, region, sector, topic, keywords, and tags.
- Summary Engine creates a structured citation-backed summary from classified metadata.

The Pipeline Contract v0.1 requires these metadata fields to survive every stage:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

## 3. Components Review

### ALIS v0.1

Purpose:

ALIS v0.1 retrieves one official World Bank publication metadata record, normalises it into GoDataBank metadata fields, stores the latest JSON record, archives a timestamped copy, and logs success or failure.

Inputs:

- Official World Bank Documents & Reports API.

Outputs:

- `data/raw/world_bank/latest_metadata.json`
- `data/raw/world_bank/archive/*.json`
- `data/raw/world_bank/logs/world_bank_connector.log`

Status:

- Operational.
- Frozen for ENGINE v0.1.

Dependencies:

- Python standard library.
- Official World Bank API endpoint.
- `backend/alis/config.py`

### Validator v0.1

Purpose:

Validator v0.1 verifies the ALIS metadata record before it can enter classification. It checks required fields, date validity, URL validity, approved institution status, World Bank domain validity, and schema structure.

Inputs:

- `data/raw/world_bank/latest_metadata.json`

Outputs:

- `APPROVED` or `REJECTED`
- `data/validated/approved_world_bank_metadata_40107522.json`
- `data/validated/validator.log`

Status:

- Operational.
- Frozen for ENGINE v0.1.

Dependencies:

- `backend/validators/schema.py`
- ALIS output.

### Abacus v0.1

Purpose:

Abacus v0.1 classifies approved Validator records using deterministic taxonomy rules. It organises the record by institution, region, sector, topic, keywords, and tags.

Inputs:

- Approved Validator records from `data/validated/`.

Outputs:

- `data/classified/classified_world_bank_metadata_40107522.json`

Status:

- Operational.
- Frozen for ENGINE v0.1.

Dependencies:

- `backend/abacus/taxonomy.py`
- Validator-approved metadata.

### Pipeline Runner v0.1

Purpose:

Pipeline Runner v0.1 orchestrates the existing World Bank path through ALIS, Validator, and Abacus using one command. It stops if validation fails.

Inputs:

- Existing ALIS, Validator, and Abacus modules.
- Official World Bank API access through ALIS.

Outputs:

- Concise execution summary:

```text
FETCHED
VALIDATED
CLASSIFIED
COMPLETE
```

- Updated raw, validated, and classified data artifacts.

Status:

- Operational.
- Frozen for ENGINE v0.1.
- It does not currently execute the Summary Engine; summary generation remains a separate controlled layer.

Dependencies:

- `backend.alis.world_bank_connector`
- `backend.validators.validator`
- `backend.abacus.classifier`

### Summary Engine v0.1

Purpose:

Summary Engine v0.1 creates one structured citation-backed summary JSON from classified metadata using fixed templates only.

Inputs:

- Classified records from `data/classified/`.

Outputs:

- `data/summaries/summary_world_bank_metadata_40107522.json`

Status:

- Operational.
- Frozen for ENGINE v0.1.

Dependencies:

- Abacus classified output.
- Pipeline Contract v0.1 preserved metadata fields.

### Pipeline Contract v0.1

Purpose:

Pipeline Contract v0.1 formally defines the mandatory metadata fields that must survive every stage. It prevents citation loss and protects evidence integrity across the engine.

Inputs:

- Existing ALIS, Validator, Abacus, and Summary Engine records.

Outputs:

- `docs/PIPELINE_CONTRACT_V0_1.md`
- Contract verification result showing required fields preserved across all stages.

Status:

- Operational as a governance document and verified contract.
- Frozen for ENGINE v0.1.

Dependencies:

- ALIS canonical metadata.
- Validator canonical schema.
- Abacus preservation of mandatory fields.
- Summary Engine preservation of mandatory fields.

## 4. What Works

ENGINE v0.1 successfully demonstrates:

- Official World Bank metadata retrieval.
- JSON storage of raw source metadata.
- Timestamped archive creation.
- Structured fetch logging.
- Validation of required metadata fields.
- Institution approval checks.
- World Bank domain checks.
- Approved metadata output.
- Structured validation logging.
- Deterministic classification.
- Region classification: `Asia-Pacific`.
- Sector classification: `Finance`.
- Topic classification: `Banking`.
- Keyword and tag generation.
- Template-based summary generation.
- Citation-backed summary JSON.
- Metadata contract preservation across ALIS, Validator, Abacus, and Summary Engine.
- A pipeline runner for ALIS through Abacus.
- Clear scope limits excluding AI, publishing, search, subscribers, databases, and additional institutions.

## 5. Known Limitations

ENGINE v0.1 is deliberately limited:

- Single institution only.
- World Bank only.
- One metadata record demonstrated.
- One official metadata endpoint implemented.
- Template summaries only.
- No AI summarisation.
- No publishing layer.
- No search.
- No subscribers.
- No databases.
- No frontend.
- No additional source connectors.
- Pipeline Runner v0.1 stops at classification and does not yet orchestrate Summary Engine.
- Classification rules are deterministic and narrow.
- Summary output is structured JSON only.

## 6. Lessons Learned

Metadata preservation is critical. The engine needs stable mandatory fields across all stages so evidence remains traceable.

Validation should occur before classification. Classification becomes safer and simpler when it only accepts approved metadata.

Classified data is more useful than raw data for downstream systems. Region, sector, topic, keywords, and tags make the record easier to organise without changing the evidence.

Pipeline contracts prevent citation loss. The contract milestone revealed that required metadata can be accidentally dropped or renamed even when each individual stage works.

Template summaries are controllable. They provide a useful summary layer without introducing AI, opinion, or unsupported claims.

Narrow scope made the system verifiable. Limiting ENGINE v0.1 to one institution and one record made it possible to inspect the full evidence path end to end.

Logging and archives make review possible. The raw archive, validation log, classified output, and summary output provide a traceable audit path.

## 7. Freeze Recommendation

ENGINE v0.1 should be frozen.

Reasoning:

- The engine retrieves official World Bank metadata.
- The record is validated before classification.
- Classification is deterministic.
- Summary generation is template-based and citation-backed.
- Mandatory metadata fields are preserved through all stages.
- Scope limits are clear and respected.
- Existing milestones are operational and reviewed.

Freeze status:

```text
ENGINE v0.1: READY TO FREEZE
```

## 8. Roadmap Recommendation

The next milestone should be:

```text
Publishing Layer v0.1
```

No further future milestone design is included in this review.
