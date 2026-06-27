from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

RAW_PATH = BASE_DIR / "fetched" / "raw.json"
OUTPUT_DIR = BASE_DIR / "analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "analysis.json"

with RAW_PATH.open("r", encoding="utf-8") as file:
    raw_file = json.load(file)

raw_response = raw_file["raw_response"]
metadata = raw_response[0]
records = raw_response[1]

valid_records = []

for record in records:
    value = record.get("value")
    if value is not None:
        valid_records.append({
            "year": int(record["date"]),
            "value_percent_gdp": float(value)
        })

valid_records = sorted(valid_records, key=lambda item: item["year"])

if not valid_records:
    raise ValueError("No valid remittance values found.")

latest = valid_records[-1]
highest = max(valid_records, key=lambda item: item["value_percent_gdp"])
lowest = min(valid_records, key=lambda item: item["value_percent_gdp"])

analysis = {
    "source_file": str(RAW_PATH),
    "retrieved_at_utc": raw_file["retrieved_at_utc"],
    "api_url": raw_file["api_url"],
    "world_bank_last_updated": metadata.get("lastupdated"),
    "indicator_id": records[0]["indicator"]["id"],
    "indicator_name": records[0]["indicator"]["value"],
    "country": records[0]["country"]["value"],
    "country_code": records[0]["countryiso3code"],
    "valid_year_count": len(valid_records),
    "first_valid_year": valid_records[0]["year"],
    "latest_valid_year": latest["year"],
    "latest_value_percent_gdp": latest["value_percent_gdp"],
    "highest_year": highest["year"],
    "highest_value_percent_gdp": highest["value_percent_gdp"],
    "lowest_year": lowest["year"],
    "lowest_value_percent_gdp": lowest["value_percent_gdp"],
    "valid_records": valid_records
}

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(analysis, file, indent=2, ensure_ascii=False)

print("Analysis complete.")
print(f"Saved: {OUTPUT_PATH}")
print(f"Valid years: {analysis['first_valid_year']} to {analysis['latest_valid_year']}")
print(f"Latest valid value: {analysis['latest_value_percent_gdp']}% of GDP in {analysis['latest_valid_year']}")
print(f"Highest value: {analysis['highest_value_percent_gdp']}% of GDP in {analysis['highest_year']}")
print(f"Lowest value: {analysis['lowest_value_percent_gdp']}% of GDP in {analysis['lowest_year']}")
