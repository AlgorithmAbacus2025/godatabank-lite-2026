from datetime import datetime, timezone
from pathlib import Path
import json
import urllib.request

API_URL = (
    "https://api.worldbank.org/v2/country/MUS/indicator/"
    "NY.GDP.PCAP.CD?format=json&per_page=100"
)

BASE_DIR = Path(__file__).resolve().parent
FETCHED_DIR = BASE_DIR / "fetched"
SOURCE_DIR = BASE_DIR / "source_records"

FETCHED_DIR.mkdir(parents=True, exist_ok=True)
SOURCE_DIR.mkdir(parents=True, exist_ok=True)

retrieved_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

with urllib.request.urlopen(API_URL, timeout=30) as response:
    raw_bytes = response.read()
    raw_text = raw_bytes.decode("utf-8")

raw_data = json.loads(raw_text)

raw_output = {
    "retrieved_at_utc": retrieved_at_utc,
    "api_url": API_URL,
    "raw_response": raw_data
}

raw_path = FETCHED_DIR / "raw.json"
source_path = SOURCE_DIR / "source.json"

if raw_path.exists():
    raise FileExistsError(f"Refusing to overwrite existing file: {raw_path}")

with raw_path.open("w", encoding="utf-8") as file:
    json.dump(raw_output, file, indent=2, ensure_ascii=False)

source_record = {
    "source_id": "world-bank-wdi-gdp-per-capita-mauritius",
    "institution": "World Bank",
    "institution_type": "Intergovernmental financial institution",
    "country": "Mauritius",
    "country_code": "MUS",
    "indicator_id": "NY.GDP.PCAP.CD",
    "indicator_name": "GDP per capita (current US$)",
    "api_url": API_URL,
    "retrieved_at_utc": retrieved_at_utc,
    "source_type": "World Development Indicators API",
    "admission_status": "review_required",
    "verification_status": "pending_human_review",
    "notes": "Fetched for manual GoDataBank Lite GDP per capita topic."
}

if source_path.exists():
    raise FileExistsError(f"Refusing to overwrite existing file: {source_path}")

with source_path.open("w", encoding="utf-8") as file:
    json.dump(source_record, file, indent=2, ensure_ascii=False)

print(f"Saved raw data: {raw_path}")
print(f"Saved source record: {source_path}")
print(f"Retrieved at UTC: {retrieved_at_utc}")
