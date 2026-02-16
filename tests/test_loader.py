from __future__ import annotations

from pathlib import Path

import pytest

from economics_analyzer.exceptions import DataSourceError, DataValidationError
from economics_analyzer.loader import load_records


def test_load_records_from_multiple_files(tmp_path: Path) -> None:
    file_1 = tmp_path / "a.csv"
    file_1.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "A,2023,100,1.0,2.0,3.0,10,Europe\n",
        encoding="utf-8",
    )
    file_2 = tmp_path / "b.csv"
    file_2.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "B,2022,200,1.1,2.1,3.1,20,Asia\n",
        encoding="utf-8",
    )

    records = load_records([str(file_1), str(file_2)])

    assert len(records) == 2
    assert records[0].country == "A"
    assert records[1].country == "B"


def test_load_records_raises_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"

    with pytest.raises(DataSourceError, match="File does not exist"):
        load_records([str(missing)])


def test_load_records_raises_for_invalid_row(tmp_path: Path) -> None:
    broken = tmp_path / "broken.csv"
    broken.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "A,not-an-int,100,1.0,2.0,3.0,10,Europe\n",
        encoding="utf-8",
    )

    with pytest.raises(DataValidationError, match="Invalid row"):
        load_records([str(broken)])
