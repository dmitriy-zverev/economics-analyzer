from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from economics_analyzer.exceptions import DataSourceError, DataValidationError
from economics_analyzer.models import EconomicRecord


def _parse_record(
    raw: dict[str, str], file_path: Path, row_number: int
) -> EconomicRecord:
    try:
        return EconomicRecord(
            country=raw["country"],
            year=int(raw["year"]),
            gdp=float(raw["gdp"]),
            gdp_growth=float(raw["gdp_growth"]),
            inflation=float(raw["inflation"]),
            unemployment=float(raw["unemployment"]),
            population=float(raw["population"]),
            continent=raw["continent"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DataValidationError(
            f"Invalid row in '{file_path}' at line {row_number}: {exc}"
        ) from exc


def load_records(files: Iterable[str]) -> list[EconomicRecord]:
    records: list[EconomicRecord] = []

    for file_name in files:
        path = Path(file_name)

        if not path.exists() or not path.is_file():
            raise DataSourceError(f"File does not exist: {file_name}")

        try:
            with path.open("r", encoding="utf-8", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                for idx, row in enumerate(reader, start=2):
                    records.append(_parse_record(row, path, idx))
        except OSError as exc:
            raise DataSourceError(f"Cannot read file '{file_name}': {exc}") from exc

    return records
