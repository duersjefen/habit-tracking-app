# Habit Tracking Application

## Introduction

This Habit Tracking Application allows users to create, manage, and analyze their daily and weekly habits through a command-line interface.

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.7 or later installed.
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Initialize the database:

```bash
python main.py
```

## Usage

### Create a Habit

```bash
python main.py create --name "Exercise" --periodicity "daily"
```

### Complete a Habit

```bash
python main.py complete --name "Exercise"
```

### List Habits

List all habits:

```bash
python main.py list
```

List habits filtered by periodicity:

```bash
python main.py list --periodicity "daily"
```

### Delete a Habit

```bash
python main.py delete --name "Exercise"
```

### Analyze Habits

Get the habit with the longest streak:

```bash
python main.py analyze --longest-streak
```

Get the longest streak for a specific habit:

```bash
python main.py analyze --habit-streak "Exercise"
```

### Predefined Habits

The application comes with 5 predefined habits. To load them, ensure the database is initialized, and the habits are inserted into the database.

## Running Tests

Navigate to the tests directory and run:

```bash
python -m unittest discover
```
