# storage_module.py

import sqlite3
from datetime import datetime
from habit import Habit
import os

DB_PATH = 'data/habits.db'


def initialize_database():
    """Initializes the database and tables."""
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            name TEXT PRIMARY KEY,
            periodicity TEXT,
            creation_date TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_name TEXT,
            completion_date TEXT,
            FOREIGN KEY(habit_name) REFERENCES habits(name)
        )
    ''')
    conn.commit()
    conn.close()


def save_habit(habit):
    """Inserts or updates a habit in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO habits (name, periodicity, creation_date)
        VALUES (?, ?, ?)
    ''', (habit.name, habit.periodicity, habit.creation_date.isoformat()))
    conn.commit()
    conn.close()


def delete_habit(name):
    """Deletes a habit from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM habits WHERE name = ?', (name,))
    cursor.execute('DELETE FROM completions WHERE habit_name = ?', (name,))
    conn.commit()
    conn.close()


def load_habits():
    """Loads all habits from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name, periodicity, creation_date FROM habits')
    habits = cursor.fetchall()
    habits_data = []
    for name, periodicity, creation_date in habits:
        cursor.execute(
            'SELECT completion_date FROM completions WHERE habit_name = ?', (name,))
        completions = cursor.fetchall()
        completion_dates = [datetime.fromisoformat(
            row[0]) for row in completions]
        habits_data.append({
            'name': name,
            'periodicity': periodicity,
            'creation_date': datetime.fromisoformat(creation_date),
            'completion_dates': completion_dates
        })
    conn.close()
    return habits_data


def save_completion(habit):
    """Records a completion event."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO completions (habit_name, completion_date)
        VALUES (?, ?)
    ''', (habit.name, habit.completion_dates[-1].isoformat()))
    conn.commit()
    conn.close()


def save_completion_manual(habit, date):
    """Records a completion event for a given date."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO completions (habit_name, completion_date)
        VALUES (?, ?)
    ''', (habit.name, date.isoformat()))
    conn.commit()
    conn.close()
