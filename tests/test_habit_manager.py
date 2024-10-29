# tests/test_habit_manager.py

import unittest
from habit_manager import HabitManager
from habit import Habit
from datetime import datetime, timedelta


class TestHabitManager(unittest.TestCase):

    def setUp(self):
        # Initialize the HabitManager instance before each test
        self.habit_manager = HabitManager()
        # Ensure a fresh start by clearing any existing habits if there's persistence
        # This method should delete all stored habits
        self.habit_manager.delete_all_habits()
        # Add initial habits for testing
        self.habit_manager.create_habit("Exercise", "daily")
        self.habit_manager.create_habit("Read", "weekly")

    def tearDown(self):
        # Clean up after each test by clearing all habits
        self.habit_manager.delete_all_habits()

    def test_create_habit(self):
        # Test that a new habit can be created and added to the manager
        self.habit_manager.create_habit("Meditate", "daily")
        habit_names = [
            habit.name for habit in self.habit_manager.habits.values()]
        self.assertIn("Meditate", habit_names)

    def test_delete_habit(self):
        # Test that an existing habit can be deleted
        self.habit_manager.delete_habit("Read")
        habit_names = [
            habit.name for habit in self.habit_manager.habits.values()]
        self.assertNotIn("Read", habit_names)

    def test_get_habit(self):
        # Test retrieving an existing habit by name
        habit = self.habit_manager.get_habit("Exercise")
        self.assertIsInstance(habit, Habit)
        self.assertEqual(habit.name, "Exercise")

    def test_list_habits(self):
        # Test listing habits by periodicity (daily and weekly)
        daily_habits = self.habit_manager.list_habits("daily")
        weekly_habits = self.habit_manager.list_habits("weekly")
        self.assertEqual(len(daily_habits), 1)
        self.assertEqual(len(weekly_habits), 1)
        self.assertEqual(daily_habits[0].name, "Exercise")
        self.assertEqual(weekly_habits[0].name, "Read")

    def test_complete_habit(self):
        # Test marking a habit as completed and checking completion dates
        self.habit_manager.complete_habit("Exercise")
        habit = self.habit_manager.get_habit("Exercise")
        self.assertEqual(len(habit.completion_dates), 1)
        # Check that the completion date is recent
        self.assertAlmostEqual(
            habit.completion_dates[-1], datetime.now(), delta=timedelta(seconds=1))


if __name__ == '__main__':
    unittest.main()
