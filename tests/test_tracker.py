import unittest
from datetime import datetime, timedelta
from src.tracker import TimeEntry, total_hours, project_summary, billable_amount


class TestTracker(unittest.TestCase):
    def setUp(self):
        t = datetime(2026, 10, 19, 9)
        self.entries = [TimeEntry("Alex", "Alpha", t, t + timedelta(hours=2)),
                        TimeEntry("Sam", "Beta", t, t + timedelta(hours=1, minutes=30)),
                        TimeEntry("Alex", "Alpha", t, t + timedelta(minutes=30))]

    def test_entry_hours(self):
        self.assertEqual(self.entries[0].hours, 2)

    def test_invalid_time(self):
        t = datetime(2026, 10, 19, 9)
        with self.assertRaises(ValueError):
            TimeEntry("Alex", "Alpha", t, t).hours

    def test_total_hours(self):
        self.assertEqual(total_hours(self.entries), 4)

    def test_employee_filter(self):
        self.assertEqual(total_hours(self.entries, "Alex"), 2.5)

    def test_unknown_employee(self):
        self.assertEqual(total_hours(self.entries, "Nobody"), 0)

    def test_project_summary(self):
        self.assertEqual(project_summary(self.entries), {"Alpha": 2.5, "Beta": 1.5})

    def test_billable_amount(self):
        self.assertEqual(billable_amount(self.entries, 20), 80)

    def test_negative_rate(self):
        with self.assertRaises(ValueError):
            billable_amount(self.entries, -1)


if __name__ == "__main__":
    unittest.main()
