"""Report implementations."""

from economics_analyzer.reports.average_gdp import AverageGDPReport
from economics_analyzer.reports.average_unemployment import AverageUnemploymentReport
from economics_analyzer.reports.base import Report, ReportResult

__all__ = [
    "Report",
    "ReportResult",
    "AverageGDPReport",
    "AverageUnemploymentReport",
]
