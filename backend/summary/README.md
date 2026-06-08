# Summary Engine

## Status

Summary Engine v0.1 creates one controlled, citation-backed JSON summary from a classified metadata record.

This folder does not contain AI logic, publishing code, frontend code, subscriber systems, databases, source connectors, or additional institution handling.

## Purpose

The summary layer sits after Abacus. It consumes classified metadata from `data/classified/` and writes structured summary output to `data/summaries/`.

## v0.1 Responsibilities

Summary Engine v0.1 supports:

- Reading classified records only
- Rejecting non-classified inputs
- Template-based summary generation
- Citation block creation from classified metadata fields
- JSON summary storage under `data/summaries/`

## Summary Rules

The summary engine must:

- Use templates only
- Use classified metadata only
- Preserve missing fields as missing or `null`
- Avoid invented facts
- Avoid opinion
- Avoid predictions
- Avoid publishing

## Non-Goals

Summary Engine v0.1 must not introduce:

- AI summarisation
- Free-form generation
- Publishing
- Search
- Frontend code
- Subscriber systems
- Databases
- Additional institutions
- Changes to ALIS, Validator, Abacus, or Pipeline Runner source code
