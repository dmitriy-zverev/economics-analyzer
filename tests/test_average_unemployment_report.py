from economics_analyzer.models import EconomicRecord
from economics_analyzer.reports.average_unemployment import AverageUnemploymentReport


def _record(country: str, unemployment: float) -> EconomicRecord:
    return EconomicRecord(
        country=country,
        year=2023,
        gdp=100.0,
        gdp_growth=1.0,
        inflation=2.0,
        unemployment=unemployment,
        population=10.0,
        continent="X",
    )


def test_average_unemployment_report_builds_sorted_averages() -> None:
    report = AverageUnemploymentReport()
    records = [
        _record("A", 8.0),
        _record("B", 6.0),
        _record("A", 10.0),
        _record("B", 4.0),
        _record("C", 2.0),
    ]

    result = report.build(records)

    assert tuple(result.headers) == ("country", "average_unemployment")
    assert result.rows == [
        ("A", 9.0),
        ("B", 5.0),
        ("C", 2.0),
    ]
