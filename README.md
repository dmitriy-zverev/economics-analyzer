# Economics Analyzer

Small CLI tool for building macroeconomic reports from CSV files.

Implemented report:
- `average-gdp` — arithmetic mean GDP by country across all provided files, sorted descending.
- `average-unemployment` — arithmetic mean unemployment by country across all provided files, sorted descending.

## Run

```bash
uv sync
uv run economics-analyzer --files data/economic1.csv data/economic2.csv --report average-gdp
uv run economics-analyzer --files data/economic1.csv data/economic2.csv --report average-unemployment
```

## Test

```bash
uv run pytest
```

## Add a new report

1. Create a report class in `economics_analyzer/reports/` implementing `Report.build(...)`.
2. Register it in `economics_analyzer/report_registry.py`.
3. Run with `--report <new-name>`.