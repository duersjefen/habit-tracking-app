# analytics_module.py

from functools import reduce


def get_all_habits(habits):
    """Returns a list of all current habits."""
    return list(habits.values())


def get_habits_by_periodicity(habits, periodicity):
    """Returns habits filtered by periodicity."""
    return list(filter(lambda h: h.periodicity == periodicity, habits.values()))


def get_longest_streak(habits):
    """Returns the habit with the longest streak."""
    if not habits:
        return None
    return max(habits.values(), key=lambda h: h.get_longest_streak())


def get_longest_streak_for_habit(habit):
    """Returns the longest streak for a specific habit."""
    return habit.get_longest_streak()
