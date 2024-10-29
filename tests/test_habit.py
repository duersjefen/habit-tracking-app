# tests/test_habit.py

import unittest
from datetime import datetime, timedelta
from habit import Habit


class TestHabit(unittest.TestCase):

    def test_complete(self):
        habit = Habit('Test Habit', 'daily')
        initial_count = len(habit.completion_dates)
        habit.complete()
        self.assertEqual(len(habit.completion_dates), initial_count + 1)

    def test_is_broken(self):
        habit = Habit('Test Habit', 'daily')
        habit.complete()
        self.assertFalse(habit.is_broken())
        habit.completion_dates[-1] -= timedelta(days=2)
        self.assertTrue(habit.is_broken())

    def test_get_current_streak(self):
        habit = Habit('Test Habit', 'daily')
        # Create a 1-day streak by completing the task daily
        habit.completion_dates = [
            datetime.now() - timedelta(days=i) for i in range(1)
        ]
        self.assertEqual(habit.get_current_streak(), 1)

    def test_get_longest_streak(self):
        habit = Habit('Test Habit', 'daily')
        # Set completion dates with a longest streak of 1 day
        habit.completion_dates = [
            datetime.now() - timedelta(days=i) for i in range(1)
        ]
        self.assertEqual(habit.get_longest_streak(), 1)


if __name__ == '__main__':
    unittest.main()
