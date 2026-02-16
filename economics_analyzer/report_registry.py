from __future__ import annotations

from economics_analyzer.exceptions import UnknownReportError
from economics_analyzer.reports import (
    AverageGDPReport,
    AverageUnemploymentReport,
    Report,
)

REPORTS: dict[str, type[Report]] = {
    AverageGDPReport.name: AverageGDPReport,
    AverageUnemploymentReport.name: AverageUnemploymentReport,
}


def available_report_names() -> list[str]:
    return sorted(REPORTS)


def get_report(report_name: str) -> Report:
    report_cls = REPORTS.get(report_name)
    if report_cls is None:
        allowed = ", ".join(available_report_names())
        raise UnknownReportError(
            f"Unknown report '{report_name}'. Available reports: {allowed}"
        )
    return report_cls()
