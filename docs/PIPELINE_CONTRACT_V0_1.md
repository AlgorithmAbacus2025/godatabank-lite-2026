# Pipeline Contract v0.1

## Mission

Preserve evidence integrity across all GoDataBank stages.

Truth is retrieved, not generated. Each pipeline stage may add stage-specific metadata, but it must not remove, rename without preserving, overwrite, or invent the mandatory evidence fields.

## Mandatory Contract Fields

Every record that enters ALIS with required metadata must preserve these fields through Validator, Abacus, and Summary Engine:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

## Field Definitions

### institution

The official institution responsible for the source record.

Requirements:

- Must be present.
- Must be non-empty.
- Must remain unchanged across stages.
- For v0.1, the approved value is `World Bank`.

### title

The official source title or publication title retrieved from the admitted source metadata.

Requirements:

- Must be present.
- Must be non-empty.
- Must remain unchanged across stages.
- Must not be rewritten as a generated headline or summary.

### publication_date

The official publication date, release date, or source date retrieved from the source metadata.

Requirements:

- Must be present when supplied by ALIS.
- Must remain unchanged across stages.
- Must be preserved as a parseable date or datetime string.
- Must not be replaced by validation, classification, or summary timestamps.

### source_url

The official source URL for the record.

Requirements:

- Must be present.
- Must be non-empty.
- Must remain unchanged across stages after ALIS canonicalises the official URL.
- Must not be replaced by archive, validation, classified, or summary file paths.

### document_id

The canonical source document identifier.

Requirements:

- Must be present.
- Must be non-empty.
- Must remain unchanged across stages.
- Source-specific aliases may also be preserved, but `document_id` is the contract field.

## Stage Contract

### ALIS

ALIS retrieves official World Bank metadata and establishes the canonical evidence fields.

ALIS v0.1 must emit:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

ALIS may also preserve World Bank-specific fields such as:

- `world_bank_document_id`
- `world_bank_record_key`
- `source_api_url`
- `retrieved_at_utc`
- `raw_record`

Contract adjustment made for v0.1:

- ALIS now emits canonical `document_id` while preserving `world_bank_document_id`.

### Validator

Validator verifies the mandatory fields and writes approved metadata.

Validator v0.1 must preserve:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

Validator may add:

- `validation_status`
- `validated_at_utc`
- `schema_version`

Validator must not replace source metadata values with validation metadata.

Review result:

- Validator already preserved all five mandatory contract fields.

### Abacus

Abacus classifies approved Validator records.

Abacus v0.1 must preserve:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

Abacus may add:

- `classification_status`
- `classified_at_utc`
- `region`
- `sector`
- `topic`
- `keywords`
- `tags`
- `schema_version`

Abacus must not replace source metadata values with classification labels.

Contract adjustment made for v0.1:

- Abacus now carries canonical `title`, `publication_date`, and `document_id` into classified output.

### Summary Engine

Summary Engine creates controlled template-based summaries from classified records only.

Summary Engine v0.1 must preserve:

- `institution`
- `title`
- `publication_date`
- `source_url`
- `document_id`

Summary Engine may add:

- `summary_status`
- `generated_at_utc`
- `headline`
- `summary`
- `key_findings`
- `citation_block`
- `schema_version`

Summary Engine must not replace source metadata values with generated summary text.

Contract adjustment made for v0.1:

- Summary Engine now emits top-level `title` and reads canonical fields before source-specific aliases.

## Prohibited Contract Breaks

The pipeline must not:

- Drop mandatory fields.
- Rename mandatory fields without keeping the canonical field.
- Replace `publication_date` with retrieval, validation, classification, or generation timestamps.
- Replace `title` with a headline.
- Replace `source_url` with a local file path.
- Replace `document_id` with a stage-specific ID.
- Invent missing contract values.
- Use AI to repair missing contract values.
- Add publishing, search, subscriber systems, databases, or additional institutions under this contract milestone.

## Test Record

The contract was verified against the World Bank record:

- `institution`: `World Bank`
- `title`: `Pacific 1 - EAST ASIA AND PACIFIC- P502591- Pacific Strengthening Correspondent Banking Relationships Project - Procurement Plan`
- `publication_date`: `2026-06-08T04:00:00Z`
- `source_url`: `https://documents.worldbank.org/curated/en/099060726202511445`
- `document_id`: `40107522`

## Test Result

The contract fields were compared across:

- `data/raw/world_bank/latest_metadata.json`
- `data/validated/approved_world_bank_metadata_40107522.json`
- `data/classified/classified_world_bank_metadata_40107522.json`
- `data/summaries/summary_world_bank_metadata_40107522.json`

Result:

```text
contract fields preserved across ALIS, Validator, Abacus, Summary
```

## Readiness

Pipeline Contract v0.1 is ready for review.

A record entering ALIS with the mandatory metadata fields now exits Summary Engine with the same `institution`, `title`, `publication_date`, `source_url`, and `document_id` values preserved.
