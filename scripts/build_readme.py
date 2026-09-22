#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "datasets.csv"
README_PATH = ROOT / "README.md"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"

def vals(row, field):
    return {x.strip().lower() for x in (row.get(field) or "").split(";") if x.strip()}

CATEGORY_ORDER = [
    ("Archives & collections", lambda r: r["resource_type"] == "archive"),
    ("Forecasting", lambda r: "forecasting" in vals(r, "tasks") and r["resource_type"] != "archive"),
    ("Human Activity Recognition", lambda r: "human activity" in vals(r, "domain")),
    ("ECG / Heartbeat", lambda r: "ecg" in vals(r, "domain")),
    ("Sleep / PSG", lambda r: "sleep" in vals(r, "domain")),
    ("Machinery / Fault Diagnosis", lambda r: "machinery" in vals(r, "domain") or "industrial" in vals(r, "domain")),
    ("Anomaly detection", lambda r: "anomaly detection" in vals(r, "tasks")),
    ("Physiological signals", lambda r: "healthcare" in vals(r, "domain")),
    ("Classification & regression", lambda r: "classification" in vals(r, "tasks") or "regression" in vals(r, "tasks")),
]

def esc(s):
    return (s or "").replace("|", r"\|").replace("\n", " ")

def table(rows):
    lines = [
        "| Resource | Tasks | Domain | Structure | Frequency | Scale | Access / license |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        scale = r["num_series"]
        if r["min_length"] or r["max_length"]:
            span = f'{r["min_length"] or "?"}–{r["max_length"] or "?"}'
            scale = f'{scale}; len {span}' if scale else f'len {span}'
        access = r["access"]
        if r["license"]:
            access = f'{access}; {r["license"]}' if access else r["license"]
        lines.append(
            f'| [{esc(r["name"])}]({r["source_url"]}) | '
            f'{esc(r["tasks"].replace(";", ", "))} | '
            f'{esc(r["domain"].replace(";", ", "))} | '
            f'{esc(r["series_structure"])} | '
            f'{esc(r["frequency"] or "—")} | '
            f'{esc(scale or "—")} | '
            f'{esc(access or "—")} |'
        )
    return "\n".join(lines)

def render(rows):
    used = set()
    sections = []
    for title, pred in CATEGORY_ORDER:
        selected = [r for r in rows if pred(r) and r["id"] not in used]
        if selected:
            used.update(r["id"] for r in selected)
            sections.append(f"### {title}\n\n{table(selected)}")
    rest = [r for r in rows if r["id"] not in used]
    if rest:
        sections.append(f"### Other\n\n{table(rest)}")
    return "\n\n".join(sections)

def generated_readme():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    text = README_PATH.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README catalog markers are missing")
    before, tail = text.split(START, 1)
    _, after = tail.split(END, 1)
    return f"{before}{START}\n\n{render(rows)}\n\n{END}{after}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    new_text = generated_readme()
    old_text = README_PATH.read_text(encoding="utf-8")
    if args.check:
        if new_text != old_text:
            print("README catalog is out of sync. Run: python scripts/build_readme.py")
            return 1
        print("README catalog is in sync.")
        return 0
    README_PATH.write_text(new_text, encoding="utf-8")
    print("README catalog regenerated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
