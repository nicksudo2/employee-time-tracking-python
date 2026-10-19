"""Run a sample employee time tracking report."""
from datetime import datetime

try:
    from .tracker import TimeEntry, total_hours, project_summary, billable_amount
except ImportError:
    from tracker import TimeEntry, total_hours, project_summary, billable_amount


def main() -> None:
    entries = [
        TimeEntry("Alex", "Website", datetime(2026, 10, 19, 9), datetime(2026, 10, 19, 12, 30)),
        TimeEntry("Alex", "Support", datetime(2026, 10, 19, 13), datetime(2026, 10, 19, 15)),
    ]
    print("Total hours:", total_hours(entries))
    print("By project:", project_summary(entries))
    print("Billable amount at $40/hr:", billable_amount(entries, 40))


if __name__ == "__main__":
    main()
