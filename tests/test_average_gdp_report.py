from economics_analyzer.models import EconomicRecord
from economics_analyzer.reports.average_gdp import AverageGDPReport


def _record(country: str, gdp: float) -> EconomicRecord:
    return EconomicRecord(
        country=country,
        year=2023,
        gdp=gdp,
        gdp_growth=1.0,
        inflation=2.0,
        unemployment=3.0,
        population=10.0,
        continent="X",
    )


def test_average_gdp_report_builds_sorted_averages() -> None:
    report = AverageGDPReport()
    records = [
        _record("A", 100),
        _record("B", 300),
        _record("A", 200),
        _record("B", 100),
        _record("C", 50),
    ]

    result = report.build(records)

    assert tuple(result.headers) == ("country", "average_gdp")
    assert result.rows == [
        ("B", 200.0),
        ("A", 150.0),
        ("C", 50.0),
    ]
