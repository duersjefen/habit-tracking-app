# habit_manager.py

from habit import Habit
import storage_module


class HabitManager:
    """
    Manages habit operations.
    """

    def __init__(self):
        self.habits = {}
        self.load_habits()

    def load_habits(self):
        """Loads habits from the storage."""
        habits_data = storage_module.load_habits()
        for data in habits_data:
            habit = Habit(
                name=data['name'],
                periodicity=data['periodicity'],
                creation_date=data['creation_date'],
                completion_dates=data['completion_dates']
            )
            self.habits[habit.name] = habit

    def create_habit(self, name, periodicity):
        """Creates a new habit."""
        if name in self.habits:
            print(f"Habit '{name}' already exists.")
            return
        habit = Habit(name, periodicity)
        self.habits[name] = habit
        storage_module.save_habit(habit)
        print(f"Habit '{name}' created.")

    def delete_habit(self, name):
        """Deletes an existing habit."""
        if name in self.habits:
            del self.habits[name]
            storage_module.delete_habit(name)
            print(f"Habit '{name}' deleted.")
        else:
            print(f"Habit '{name}' does not exist.")

    def get_habit(self, name):
        """Retrieves a habit by name."""
        return self.habits.get(name)

    def list_habits(self, periodicity=None):
        """Lists all habits, optionally filtered by periodicity."""
        if periodicity:
            return [habit for habit in self.habits.values() if habit.periodicity == periodicity]
        else:
            return list(self.habits.values())

    def complete_habit(self, name):
        """Marks a habit as completed."""
        habit = self.get_habit(name)
        if habit:
            habit.complete()
            storage_module.save_completion(habit)
            print(f"Habit '{name}' marked as completed.")
        else:
            print(f"Habit '{name}' does not exist.")
