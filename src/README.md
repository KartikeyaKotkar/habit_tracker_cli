# CLI Habit Tracker

A simple command-line application to help you track your daily habits, monitor your progress, and visualize your streaks using Python.

## Features

- Add new habits
- Mark habits as completed
- View current habits and their streaks
- Visualize habit progress over time with charts

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CLI_habit_tracker.git
   cd CLI_habit_tracker
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the `data` directory** (if it doesn't exist):
   ```bash
   mkdir -p src/data
   ```

## Usage

1. Run the application:
   ```bash
   python -m src.habit_tracker.main
   ```

2. Use the following commands to interact with the tracker:
   - `add`: Add a new habit.
   - `track`: Mark a habit as completed for today.
   - `view`: View all current habits and their streaks.
   - `visualize`: Visualize the progress of a specific habit over time.
   - `quit`: Exit the application.

### Example Commands

- To add a habit:
  ```
  > add
  Enter habit name: Edging
  ```

- To track a habit:
  ```
  > track
  Enter habit name to mark as completed: react web frontend
  ```

- To view habits:
  ```
  > view
  Enter habit name to view: brunch
  ```

- To visualize a habit:
  ```
  > visualize
  Enter habit name to visualize: yoga
  ```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
