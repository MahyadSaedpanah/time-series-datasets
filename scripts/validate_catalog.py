#!/usr/bin/env python3
import csv
import datetime as dt
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "datasets.csv"

REQUIRED_COLUMNS = {
    "id","name","resource_type","tasks","domain","series_structure","multivariate",
    "license","access","source_url","last_verified"
}
ALLOWED_TYPES = {"dataset","archive","benchmark","competition"}
ALLOWED_MULTIVARIATE = {"yes","no","varies",""}

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def valid_url(value):
    p = urlparse(value)
    return p.scheme in {"http","https"} and bool(p.netloc)

def valid_iso_date(value):
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False

def main():
    errors = []
    with CATALOG.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = set(reader.fieldnames or [])
        missing_columns = REQUIRED_COLUMNS - columns
        if missing_columns:
            errors.append(f"Missing required columns: {sorted(missing_columns)}")
            rows = []
        else:
            rows = list(reader)

    seen_ids = set()

    for line_no, row in enumerate(rows, start=2):
        rid = row["id"].strip()

        if not rid or not ID_RE.fullmatch(rid):
            errors.append(f"Row {line_no}: invalid id {rid!r}")
        elif rid in seen_ids:
            errors.append(f"Row {line_no}: duplicate id {rid!r}")
        seen_ids.add(rid)

        if row["resource_type"].strip() not in ALLOWED_TYPES:
            errors.append(f"Row {line_no}: invalid resource_type {row['resource_type']!r}")

        if row["multivariate"].strip() not in ALLOWED_MULTIVARIATE:
            errors.append(f"Row {line_no}: invalid multivariate value {row['multivariate']!r}")

        for field in ("name","tasks","domain","series_structure","license","access"):
            if not row[field].strip():
                errors.append(f"Row {line_no}: empty {field}")

        if not valid_url(row["source_url"].strip()):
            errors.append(f"Row {line_no}: invalid source_url {row['source_url']!r}")

        citation = row.get("citation_url","").strip()
        if citation and not valid_url(citation):
            errors.append(f"Row {line_no}: invalid citation_url {citation!r}")

        if not valid_iso_date(row["last_verified"].strip()):
            errors.append(f"Row {line_no}: invalid last_verified date")

    if errors:
        print("Catalog validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print(f"Catalog validation passed: {len(rows)} entries.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
