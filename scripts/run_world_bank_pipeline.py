"""Run the GoDataBank World Bank pipeline.

Pipeline Runner v0.1 scope:
- ALIS World Bank metadata fetch
- Validator approval check
- Abacus deterministic classification
- no summarisation, publishing, search, subscriber systems, databases, frontend code, or extra institutions
"""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.abacus import classifier
from backend.alis import world_bank_connector
from backend.validators import schema, validator


class PipelineError(RuntimeError):
    """Raised when the pipeline cannot complete a required stage."""


def run_pipeline() -> dict[str, str]:
    fetch_result = world_bank_connector.run()
    metadata_path = Path(fetch_result["metadata_path"])

    validation_status, validation_errors, validated_path = validator.validate_file(metadata_path)
    if validation_status != schema.APPROVED_STATUS or validated_path is None:
        raise PipelineError(f"validation failed: {'; '.join(validation_errors) or validation_status}")

    classified_path, _ = classifier.classify_file(validated_path)

    return {
        "metadata_path": str(metadata_path),
        "validated_path": str(validated_path),
        "classified_path": str(classified_path),
    }


def main() -> int:
    try:
        run_pipeline()
    except Exception as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1

    print("FETCHED")
    print("VALIDATED")
    print("CLASSIFIED")
    print("COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
