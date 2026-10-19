"""Educational time tracking utilities inspired by TrackPilotAI."""
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class TimeEntry:
    employee: str
    project: str
    start: datetime
    end: datetime

    @property
    def hours(self) -> float:
        if self.end <= self.start:
            raise ValueError("End time must be later than start time")
        return round((self.end - self.start).total_seconds() / 3600, 2)


def total_hours(entries: Iterable[TimeEntry], employee: str | None = None) -> float:
    return round(sum(entry.hours for entry in entries if employee is None or entry.employee == employee), 2)


def project_summary(entries: Iterable[TimeEntry]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for entry in entries:
        totals[entry.project] = round(totals.get(entry.project, 0) + entry.hours, 2)
    return totals


def billable_amount(entries: Iterable[TimeEntry], hourly_rate: float) -> float:
    if hourly_rate < 0:
        raise ValueError("Hourly rate cannot be negative")
    return round(total_hours(entries) * hourly_rate, 2)
