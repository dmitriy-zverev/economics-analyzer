from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence

from economics_analyzer.models import EconomicRecord


@dataclass(frozen=True)
class ReportResult:
    headers: Sequence[str]
    rows: Sequence[Sequence[object]]


class Report(ABC):
    """Base report contract for all report implementations."""

    name: str

    @abstractmethod
    def build(self, records: list[EconomicRecord]) -> ReportResult:
        """Build report data structure from economic records."""
