import pytest

from economics_analyzer.exceptions import UnknownReportError
from economics_analyzer.report_registry import available_report_names, get_report
from economics_analyzer.reports.average_gdp import AverageGDPReport
from economics_analyzer.reports.average_unemployment import AverageUnemploymentReport


def test_registry_returns_average_gdp_report() -> None:
    report = get_report("average-gdp")
    assert isinstance(report, AverageGDPReport)


def test_registry_lists_available_reports() -> None:
    assert "average-gdp" in available_report_names()
    assert "average-unemployment" in available_report_names()


def test_registry_returns_average_unemployment_report() -> None:
    report = get_report("average-unemployment")
    assert isinstance(report, AverageUnemploymentReport)


def test_registry_raises_for_unknown_report() -> None:
    with pytest.raises(UnknownReportError, match="Unknown report"):
        get_report("unknown")
