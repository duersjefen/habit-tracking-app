# cli.py

import argparse
from habit_manager import HabitManager
import analytics_module
import storage_module


def main():
    storage_module.initialize_database()
    manager = HabitManager()

    parser = argparse.ArgumentParser(description='Habit Tracking Application')
    subparsers = parser.add_subparsers(dest='command')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new habit')
    create_parser.add_argument(
        '--name', required=True, help='Name of the habit')
    create_parser.add_argument('--periodicity', required=True,
                               choices=['daily', 'weekly'], help='Periodicity of the habit')

    # Delete command
    delete_parser = subparsers.add_parser(
        'delete', help='Delete an existing habit')
    delete_parser.add_argument(
        '--name', required=True, help='Name of the habit to delete')

    # Complete command
    complete_parser = subparsers.add_parser(
        'complete', help='Mark a habit as completed')
    complete_parser.add_argument(
        '--name', required=True, help='Name of the habit to complete')

    # List command
    list_parser = subparsers.add_parser('list', help='List current habits')
    list_parser.add_argument(
        '--periodicity', choices=['daily', 'weekly'], help='Filter habits by periodicity')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze habits')
    analyze_parser.add_argument(
        '--longest-streak', action='store_true', help='Show habit with the longest streak')
    analyze_parser.add_argument(
        '--habit-streak', help='Show longest streak for a specific habit')

    args = parser.parse_args()

    if args.command == 'create':
        manager.create_habit(args.name, args.periodicity)

    elif args.command == 'delete':
        manager.delete_habit(args.name)

    elif args.command == 'complete':
        manager.complete_habit(args.name)

    elif args.command == 'list':
        habits = manager.list_habits(args.periodicity)
        if habits:
            for habit in habits:
                print(f"- {habit.name} ({habit.periodicity})")
        else:
            print("No habits found.")

    elif args.command == 'analyze':
        if args.longest_streak:
            habit = analytics_module.get_longest_streak(manager.habits)
            if habit:
                print(f"Habit '{habit.name}' has the longest streak of {
                      habit.get_longest_streak()} periods.")
            else:
                print("No habits found.")
        elif args.habit_streak:
            habit = manager.get_habit(args.habit_streak)
            if habit:
                streak = analytics_module.get_longest_streak_for_habit(habit)
                print(f"Habit '{habit.name}' longest streak: {
                      streak} periods.")
            else:
                print(f"Habit '{args.habit_streak}' does not exist.")
        else:
            print("Please specify an analysis option. Use --help for more information.")
    else:
        parser.print_help()
