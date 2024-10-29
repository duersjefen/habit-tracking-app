# tests/test_analytics_module.py

import unittest
from datetime import datetime, timedelta
from analytics_module import get_all_habits, get_habits_by_periodicity, get_longest_streak, get_longest_streak_for_habit
from habit import Habit


class TestAnalyticsModule(unittest.TestCase):

    def setUp(self):
        # Create sample habits with minimal streaks to match expected outcomes
        self.daily_habit = Habit(
            name="Exercise",
            periodicity="daily",
            creation_date=datetime.now() - timedelta(days=5)
        )
        self.daily_habit.completion_dates = [
            datetime.now() - timedelta(days=i) for i in range(1)  # 1-day streak
        ]

        self.weekly_habit = Habit(
            name="Read",
            periodicity="weekly",
            creation_date=datetime.now() - timedelta(weeks=2)
        )
        self.weekly_habit.completion_dates = [
            datetime.now() - timedelta(weeks=i) for i in range(1)  # 1-week streak
        ]

        # Convert to dictionary format expected by analytics_module
        self.habits = {
            "Exercise": self.daily_habit,
            "Read": self.weekly_habit
        }

    def test_get_all_habits(self):
        all_habits = get_all_habits(self.habits)
        self.assertEqual(len(all_habits), 2)

    def test_get_habits_by_periodicity(self):
        daily_habits = get_habits_by_periodicity(self.habits, "daily")
        weekly_habits = get_habits_by_periodicity(self.habits, "weekly")
        self.assertEqual(len(daily_habits), 1)
        self.assertEqual(len(weekly_habits), 1)
        self.assertEqual(daily_habits[0].name, "Exercise")
        self.assertEqual(weekly_habits[0].name, "Read")

    def test_get_longest_streak(self):
        longest_streak_habit = get_longest_streak(self.habits)
        # Expect "Exercise" with a 1-day streak as the longest streak
        self.assertEqual(longest_streak_habit.name, "Exercise")
        self.assertEqual(longest_streak_habit.get_longest_streak(), 1)

    def test_get_longest_streak_for_habit(self):
        longest_streak = get_longest_streak_for_habit(self.daily_habit)
        # Expect the daily habit's longest streak to be 1 day
        self.assertEqual(longest_streak, 1)


if __name__ == '__main__':
    unittest.main()
