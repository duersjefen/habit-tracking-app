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
        habit.completion_dates = [
            datetime.now() - timedelta(days=3),
            datetime.now() - timedelta(days=2),
            datetime.now() - timedelta(days=1),
            datetime.now(),
        ]
        self.assertEqual(habit.get_current_streak(), 4)

    def test_get_longest_streak(self):
        habit = Habit('Test Habit', 'daily')
        habit.completion_dates = [
            datetime.now() - timedelta(days=6),
            datetime.now() - timedelta(days=5),
            datetime.now() - timedelta(days=3),
            datetime.now() - timedelta(days=2),
            datetime.now() - timedelta(days=1),
            datetime.now(),
        ]
        self.assertEqual(habit.get_longest_streak(), 3)


if __name__ == '__main__':
    unittest.main()
