from __future__ import annotations

from pathlib import Path

from economics_analyzer.cli import main, run


def _write_csv(path: Path, rows: str) -> None:
    path.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        + rows,
        encoding="utf-8",
    )


def test_run_returns_table() -> None:
    table = run(
        files=["data/economic1.csv", "data/economic2.csv"], report_name="average-gdp"
    )

    assert "| country" in table
    assert "United States" in table


def test_run_returns_table_for_average_unemployment() -> None:
    table = run(
        files=["data/economic1.csv", "data/economic2.csv"],
        report_name="average-unemployment",
    )

    assert "| country" in table
    assert "average_unemployment" in table


def test_main_success(capsys, tmp_path: Path) -> None:
    data_file = tmp_path / "test.csv"
    _write_csv(data_file, "A,2023,100,1.0,2.0,3.0,10,Europe\n")

    exit_code = main(["--files", str(data_file), "--report", "average-gdp"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "A" in captured.out
    assert captured.err == ""


def test_main_unknown_report(capsys, tmp_path: Path) -> None:
    data_file = tmp_path / "test.csv"
    _write_csv(data_file, "A,2023,100,1.0,2.0,3.0,10,Europe\n")

    exit_code = main(["--files", str(data_file), "--report", "wrong-report"])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Unknown report" in captured.err


def test_main_missing_file(capsys, tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"

    exit_code = main(["--files", str(missing), "--report", "average-gdp"])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "File does not exist" in captured.err
