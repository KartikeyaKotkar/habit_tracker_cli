from src.habit_tracker.habit import HabitTracker


def     main():
    tracker = HabitTracker()

    while True:
        command = input("Enter a command (add, track, view, visualize, delete, quit): ").strip().lower()

        if command == 'add':
            name = input("Enter habit name: ")
            tracker.add_habit(name)

        elif command == 'track':
            name = input("Enter habit name to mark as completed: ")
            tracker.mark_habit(name)


        elif command == 'view':
            tracker.view_habits()

        elif command == 'visualize':
            name = input("Enter habit name to visualize: ")
            tracker.visualize_habit(name)

        elif command == 'delete':
            name = input("Enter habit name to delete: ")
            tracker.delete_habit(name)

        elif command == 'quit':
            print("Exiting the Habit Tracker. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
