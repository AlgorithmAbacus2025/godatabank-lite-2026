# Summary Engine v0.1 Review

## Summary

Summary Engine v0.1 is the first controlled GoDataBank summary layer. It consumes classified metadata records from `data/classified/` only and writes one structured, citation-backed JSON summary to `data/summaries/`.

The engine uses fixed templates only. It does not use AI, invent facts, add opinion, make predictions, publish content, create frontend code, create subscriber systems, add additional institutions, or alter ALIS, Validator, Abacus, or Pipeline Runner source code.

## Files Created and Modified

Created:

- `backend/summary/README.md`
- `backend/summary/summary_generator.py`
- `docs/SUMMARY_ENGINE_V0_1_REVIEW.md`
- `data/summaries/summary_world_bank_metadata_40107522.json`

Modified:

- None.

## Input

Input directory:

```text
data/classified/
```

Test input:

```text
data/classified/classified_world_bank_metadata_40107522.json
```

Required input condition:

```json
{
  "classification_status": "CLASSIFIED"
}
```

Summary Engine v0.1 rejects records that are not classified.

## Summary Format

Output directory:

```text
data/summaries/
```

Output file:

```text
data/summaries/summary_world_bank_metadata_40107522.json
```

Required output fields:

- `headline`
- `summary`
- `key_findings`
- `institution`
- `region`
- `sector`
- `topic`
- `source_url`
- `publication_date`
- `document_id`
- `citation_block`

Additional control metadata:

- `summary_status`
- `schema_version`
- `generated_at_utc`

## Template Logic

The summary engine fills fixed templates from classified metadata fields.

Headline template:

```text
{institution} metadata classified under {topic}
```

Summary template:

```text
This classified metadata record is organised as {topic} within the {sector} sector for the {region} region. The source title is: {source_title}
```

Key findings template:

- `Institution: {institution}`
- `Region: {region}`
- `Sector: {sector}`
- `Topic: {topic}`
- `Document ID: {document_id}`
- `Publication date: {publication_date}`

If `publication_date` is absent from the classified record, Summary Engine v0.1 preserves the missing value as `null` and records:

```text
Publication date: not present in the classified record
```

This avoids reading from earlier pipeline stages and avoids inventing facts.

## Citation Block

The citation block is built from classified metadata only:

- `institution`
- `title`
- `source_url`
- `publication_date`
- `document_id`
- `classification_status`
- `classified_at_utc`

Observed citation values:

- Institution: `World Bank`
- Title: `Pacific 1 - EAST ASIA AND PACIFIC- P502591- Pacific Strengthening Correspondent Banking Relationships Project - Procurement Plan`
- Source URL: `https://documents.worldbank.org/curated/en/099060726202511445`
- Publication date: `null`
- Document ID: `40107522`
- Classification status: `CLASSIFIED`

## Test Results

Syntax check:

- `backend/summary/summary_generator.py`: passed

Generation run:

- Input: `data/classified/classified_world_bank_metadata_40107522.json`
- Output status: `GENERATED`
- Output: `data/summaries/summary_world_bank_metadata_40107522.json`
- Required fields present: yes
- Output JSON parsed successfully: yes

Generated summary values:

- Headline: `World Bank metadata classified under Banking`
- Institution: `World Bank`
- Region: `Asia-Pacific`
- Sector: `Finance`
- Topic: `Banking`
- Source URL: `https://documents.worldbank.org/curated/en/099060726202511445`
- Document ID: `40107522`
- Publication date: `null`

## Explicit Scope Limits

Summary Engine v0.1 does not include:

- AI summarisation
- Free-form generation
- Invented facts
- Opinion
- Predictions
- Publishing
- Frontend code
- Subscriber systems
- Additional institutions
- Databases
- Changes to ALIS source code
- Changes to Validator source code
- Changes to Abacus source code
- Changes to Pipeline Runner source code

## Readiness

Summary Engine v0.1 satisfies the milestone success criteria. It took one classified World Bank record, generated one citation-backed structured summary JSON, and stored it in `data/summaries/`.

Summary Engine v0.1 is ready for review.
