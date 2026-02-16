from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EconomicRecord:
    country: str
    year: int
    gdp: float
    gdp_growth: float
    inflation: float
    unemployment: float
    population: float
    continent: str
