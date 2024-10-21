# habit.py

from datetime import datetime, timedelta


class Habit:
    """
    Represents a habit with its attributes and behaviors.
    """

    def __init__(self, name, periodicity, creation_date=None, completion_dates=None):
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.creation_date = creation_date if creation_date else datetime.now()
        self.completion_dates = completion_dates if completion_dates else []

    def complete(self):
        """Records the current timestamp as a completion date."""
        self.completion_dates.append(datetime.now())

    def is_broken(self):
        """Determines if the habit has been broken."""
        last_completion = max(
            self.completion_dates) if self.completion_dates else None
        if not last_completion:
            return True

        if self.periodicity == 'daily':
            return datetime.now() - last_completion > timedelta(days=1)
        elif self.periodicity == 'weekly':
            return datetime.now() - last_completion > timedelta(weeks=1)
        else:
            return True

    def get_current_streak(self):
        """Calculates the current streak."""
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates, reverse=True)
        streak = 1
        for i in range(len(sorted_dates) - 1):
            delta = sorted_dates[i] - sorted_dates[i + 1]
            if self.periodicity == 'daily' and delta <= timedelta(days=1):
                streak += 1
            elif self.periodicity == 'weekly' and delta <= timedelta(weeks=1):
                streak += 1
            else:
                break
        return streak

    def get_longest_streak(self):
        """Calculates the longest streak."""
        if not self.completion_dates:
            return 0

        sorted_dates = sorted(self.completion_dates)
        streaks = []
        streak = 1

        for i in range(1, len(sorted_dates)):
            delta = sorted_dates[i] - sorted_dates[i - 1]
            if self.periodicity == 'daily' and delta <= timedelta(days=1):
                streak += 1
            elif self.periodicity == 'weekly' and delta <= timedelta(weeks=1):
                streak += 1
            else:
                streaks.append(streak)
                streak = 1
        streaks.append(streak)
        return max(streaks)
