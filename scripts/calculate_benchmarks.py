#!/usr/bin/env python3
"""Calculate core real-estate lead benchmark metrics from a CSV export.

Usage:
    python scripts/calculate_benchmarks.py examples/synthetic-leads.csv

The script uses only the Python standard library.
"""

from __future__ import annotations

import csv
import sys
from datetime import datetime
from statistics import median
from typing import Iterable

TRUE_VALUES = {"true", "1", "yes", "y"}


def as_bool(value: str | None) -> bool:
    return (value or "").strip().lower() in TRUE_VALUES


def parse_dt(value: str | None) -> datetime | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return values[0]
    k = (len(values) - 1) * p
    f = int(k)
    c = min(f + 1, len(values) - 1)
    if f == c:
        return values[f]
    return values[f] + (values[c] - values[f]) * (k - f)


def safe_rate(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return numerator / denominator


def fmt_rate(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.1%}"


def fmt_num(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.1f}"


def response_band(minutes: float | None) -> str:
    if minutes is None:
        return "no_attempt"
    if minutes <= 5:
        return "0-5m"
    if minutes <= 15:
        return "6-15m"
    if minutes <= 30:
        return "16-30m"
    if minutes <= 60:
        return "31-60m"
    if minutes <= 240:
        return "1-4h"
    if minutes <= 1440:
        return "4-24h"
    return "24h+"


def read_rows(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def calculate(rows: Iterable[dict[str, str]]) -> dict[str, object]:
    rows = list(rows)
    total = len(rows)
    attempted = 0
    contacted = 0
    qualified = 0
    appointments = 0
    completed = 0
    won = 0
    lost = 0
    response_minutes: list[float] = []
    bands: dict[str, int] = {}

    for row in rows:
        created = parse_dt(row.get("lead_created_at"))
        attempted_at = parse_dt(row.get("first_attempt_at"))

        if attempted_at:
            attempted += 1

        minutes = None
        if created and attempted_at:
            delta = (attempted_at - created).total_seconds() / 60
            if delta >= 0:
                minutes = delta
                response_minutes.append(delta)

        band = response_band(minutes)
        bands[band] = bands.get(band, 0) + 1

        contacted += int(as_bool(row.get("contacted")))
        qualified += int(as_bool(row.get("qualified")))
        appointments += int(as_bool(row.get("appointment_scheduled")))
        completed += int(as_bool(row.get("appointment_completed")))
        won += int(as_bool(row.get("won")))
        lost += int(as_bool(row.get("lost")))

    return {
        "total": total,
        "attempted": attempted,
        "contacted": contacted,
        "qualified": qualified,
        "appointments": appointments,
        "completed": completed,
        "won": won,
        "lost": lost,
        "median_speed": median(response_minutes) if response_minutes else None,
        "p75_speed": percentile(response_minutes, 0.75),
        "p90_speed": percentile(response_minutes, 0.90),
        "contact_rate": safe_rate(contacted, total),
        "qualification_rate": safe_rate(qualified, contacted),
        "appointment_rate_contacted": safe_rate(appointments, contacted),
        "show_up_rate": safe_rate(completed, appointments),
        "lead_to_sale": safe_rate(won, total),
        "contact_to_sale": safe_rate(won, contacted),
        "bands": bands,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/calculate_benchmarks.py <csv-file>")
        return 2

    rows = read_rows(sys.argv[1])
    metrics = calculate(rows)

    print("Real Estate Lead Benchmark Summary")
    print("=" * 35)
    print(f"Total leads: {metrics['total']}")
    print(f"Attempted: {metrics['attempted']}")
    print(f"Contacted: {metrics['contacted']}")
    print(f"Qualified: {metrics['qualified']}")
    print(f"Appointments: {metrics['appointments']}")
    print(f"Completed appointments: {metrics['completed']}")
    print(f"Won: {metrics['won']}")
    print(f"Lost: {metrics['lost']}")
    print()
    print(f"Median speed-to-lead (min): {fmt_num(metrics['median_speed'])}")
    print(f"P75 speed-to-lead (min): {fmt_num(metrics['p75_speed'])}")
    print(f"P90 speed-to-lead (min): {fmt_num(metrics['p90_speed'])}")
    print(f"Contact rate: {fmt_rate(metrics['contact_rate'])}")
    print(f"Qualification rate: {fmt_rate(metrics['qualification_rate'])}")
    print(f"Appointment rate (contacted basis): {fmt_rate(metrics['appointment_rate_contacted'])}")
    print(f"Show-up rate: {fmt_rate(metrics['show_up_rate'])}")
    print(f"Lead-to-sale conversion: {fmt_rate(metrics['lead_to_sale'])}")
    print(f"Contact-to-sale conversion: {fmt_rate(metrics['contact_to_sale'])}")
    print()
    print("Response-time bands:")
    for band, count in sorted(metrics["bands"].items()):
        print(f"  {band}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
