import json
from datetime import datetime
import os
import matplotlib.pyplot as plt

class Habit:
    def __init__(self, name):
        self.name = name
        self.start_date = str(datetime.today().date())
        self.streak = 0
        self.progress = {}  # date: "completed" or "missed"

    def mark_completed(self):
        today = str(datetime.today().date())
        if today not in self.progress:
            self.progress[today] = "completed"
            self.streak += 1
        else:
            print(f"Habit '{self.name}' already marked for today.")

    def save(self):
        """Save the habit's data to a file."""
        try:
            # Create data directory if it doesn't exist
            os.makedirs('src/data', exist_ok=True)

            with open('src/data/habits.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data[self.name] = {
            "start_date": self.start_date,
            "streak": self.streak,
            "progress": self.progress
        }

        with open('src/data/habits.json', 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load():
        """Load all habits from the JSON file."""
        try:
            with open('src/data/habits.json', 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return {}

class HabitTracker:
    def __init__(self):
        self.habits = Habit.load()  # Load existing habits from file

    def add_habit(self, name):
        if name in self.habits:
            print(f"Habit '{name}' already exists.")
        else:
            new_habit = Habit(name)
            new_habit.save()
            print(f"Added new habit: {name}")

    def mark_habit(self, name):
        if name in self.habits:
            habit_data = self.habits[name]
            habit_obj = Habit(name)
            habit_obj.progress = habit_data['progress']
            habit_obj.streak = habit_data['streak']
            habit_obj.mark_completed()
            habit_obj.save()
        else:
            print(f"Habit '{name}' does not exist.")

    def view_habits(self):
        if self.habits:
            for name, details in self.habits.items():
                print(f"Habit: {name}, Streak: {details['streak']}")
        else:
            print("No habits found.")

    def visualize_habit(self, name):
        if name in self.habits:
            habit = self.habits[name]
            progress = habit['progress']

            # Extract dates and completion status from progress
            dates = list(progress.keys())
            completion = [1 if progress[date] == "completed" else 0 for date in dates]

            # Convert date strings to datetime objects for plotting
            dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

            # Create the plot
            plt.figure(figsize=(10, 5))
            plt.plot(dates, completion, marker='o', linestyle='-', color='b')
            plt.ylim(-0.1, 1.1)  # Limits to better display 0 and 1 values
            plt.yticks([0, 1], ['Missed', 'Completed'])
            plt.xlabel('Date')
            plt.ylabel('Habit Completion')
            plt.title(f"Habit Progress: {name}")
            plt.grid(True)

            # Show the plot
            plt.show()
        else:
            print(f"Habit '{name}' does not exist.")

    def delete_habit(self, name):
        """Delete a habit and wipe all its data."""
        if name in self.habits:
            del self.habits[name]
            self.save_all_habits()
            print(f"Deleted habit: {name}")
        else:
            print(f"Habit '{name}' does not exist.")

    def save_all_habits(self):
        """Save all habits to the JSON file."""
        with open('src/data/habits.json', 'w') as f:
            json.dump(self.habits, f, indent=4)
