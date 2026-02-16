from __future__ import annotations

from collections import defaultdict

from economics_analyzer.models import EconomicRecord
from economics_analyzer.reports.base import Report, ReportResult


class AverageGDPReport(Report):
    name = "average-gdp"

    def build(self, records: list[EconomicRecord]) -> ReportResult:
        gdp_by_country: dict[str, list[float]] = defaultdict(list)

        for record in records:
            gdp_by_country[record.country].append(record.gdp)

        rows = []
        for country, gdp_values in gdp_by_country.items():
            average = sum(gdp_values) / len(gdp_values)
            rows.append((country, round(average, 2)))

        rows.sort(key=lambda row: row[1], reverse=True)

        return ReportResult(headers=("country", "average_gdp"), rows=rows)
