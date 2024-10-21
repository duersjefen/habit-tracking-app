import storage_module
from habit import Habit
from datetime import datetime, timedelta


def prepopulate():
    storage_module.initialize_database()
    habits = [
        Habit('Drink Water', 'daily'),
        Habit('Exercise', 'daily'),
        Habit('Read Book', 'daily'),
        Habit('Weekly Meeting', 'weekly'),
        Habit('Grocery Shopping', 'weekly'),
    ]

    for habit in habits:
        storage_module.save_habit(habit)
        # Simulate completions over 4 weeks
        if habit.periodicity == 'daily':
            for i in range(28):
                date = datetime.now() - timedelta(days=28 - i)
                habit.completion_dates.append(date)
                storage_module.save_completion_manual(habit, date)
        elif habit.periodicity == 'weekly':
            for i in range(4):
                date = datetime.now() - timedelta(weeks=4 - i)
                habit.completion_dates.append(date)
                storage_module.save_completion_manual(habit, date)


if __name__ == '__main__':
    prepopulate()
