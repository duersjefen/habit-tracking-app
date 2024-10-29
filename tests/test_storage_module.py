# tests/test_storage_module.py

import unittest
from storage_module import save_habit, load_habits, delete_habit, save_completion
from habit import Habit
from datetime import datetime, timedelta


class TestStorageModule(unittest.TestCase):

    def setUp(self):
        # Clear all data at the beginning of each test
        self.clear_all_habits()

    def tearDown(self):
        # Clear all data after each test
        self.clear_all_habits()

    def clear_all_habits(self):
        """Helper function to clear all habits from the database for test isolation."""
        for habit_dict in load_habits():
            delete_habit(habit_dict['name'])

    def create_habit_instance(self, name="Exercise", periodicity="daily"):
        """Creates a Habit instance and saves it."""
        habit = Habit(name=name, periodicity=periodicity,
                      creation_date=datetime.now())
        save_habit(habit)
        return habit

    def test_save_habit(self):
        # Save a new habit and verify it exists in storage
        self.create_habit_instance()
        saved_habits = load_habits()
        self.assertEqual(len(saved_habits), 1)
        self.assertEqual(saved_habits[0]['name'], "Exercise")

    def test_delete_habit(self):
        # Save and then delete a habit
        self.create_habit_instance("Read", "weekly")
        delete_habit("Read")
        saved_habits = load_habits()
        self.assertEqual(len(saved_habits), 0)

    def test_load_habits(self):
        # Save multiple habits and verify they are loaded correctly
        self.create_habit_instance("Exercise", "daily")
        self.create_habit_instance("Read", "weekly")
        saved_habits = load_habits()
        habit_names = {habit['name'] for habit in saved_habits}
        self.assertEqual(habit_names, {"Exercise", "Read"})

    def test_save_completion(self):
        # Create and save a habit
        habit = self.create_habit_instance("Exercise", "daily")
        completion_date = datetime.now()

        # Add completion date to the habit directly before calling save_completion
        habit.completion_dates.append(completion_date)
        save_completion(habit)

        # Reload habit to verify completion date is saved
        reloaded_habits = load_habits()
        reloaded_habit = next(
            h for h in reloaded_habits if h['name'] == "Exercise")
        self.assertEqual(len(reloaded_habit['completion_dates']), 1)

        # Since reloaded_habit['completion_dates'][0] is already a datetime object,
        # we can directly compare it with completion_date
        reloaded_completion_date = reloaded_habit['completion_dates'][0]
        self.assertIsInstance(reloaded_completion_date, datetime)
        self.assertAlmostEqual(
            reloaded_completion_date,
            completion_date,
            delta=timedelta(seconds=1)
        )


if __name__ == '__main__':
    unittest.main()
