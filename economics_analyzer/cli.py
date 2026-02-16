from __future__ import annotations

import argparse
import sys
from typing import Sequence

from tabulate import tabulate

from economics_analyzer.exceptions import AppError
from economics_analyzer.loader import load_records
from economics_analyzer.report_registry import get_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="economics-analyzer",
        description="Build macroeconomic reports from CSV files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="One or more CSV files with economic data.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name (e.g. average-gdp).",
    )
    return parser


def run(files: Sequence[str], report_name: str) -> str:
    records = load_records(files)
    if not records:
        raise AppError("No records found in the provided files.")

    report = get_report(report_name)
    result = report.build(records)
    return tabulate(result.rows, headers=result.headers, tablefmt="psql")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        table = run(files=args.files, report_name=args.report)
    except AppError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
