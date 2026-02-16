from __future__ import annotations

from collections import defaultdict

from economics_analyzer.models import EconomicRecord
from economics_analyzer.reports.base import Report, ReportResult


class AverageUnemploymentReport(Report):
    name = "average-unemployment"

    def build(self, records: list[EconomicRecord]) -> ReportResult:
        unemployment_by_country: dict[str, list[float]] = defaultdict(list)

        for record in records:
            unemployment_by_country[record.country].append(record.unemployment)

        rows = []
        for country, values in unemployment_by_country.items():
            average = sum(values) / len(values)
            rows.append((country, round(average, 2)))

        rows.sort(key=lambda row: row[1], reverse=True)

        return ReportResult(headers=("country", "average_unemployment"), rows=rows)
