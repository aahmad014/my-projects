# Personal Expense Tracker

A simple command-line app to record and review daily spending, built with Python.

## Features
- Add expenses with a category and amount (date is saved automatically)
- View all recorded expenses
- See total spending, number of expenses, and average per expense
- See totals for each category
- Data is saved to a CSV file, so nothing is lost when you close the program
- Input validation for empty categories and invalid amounts

## How to run
1. Install Python 3.
2. Download or clone this project.
3. Open a terminal in the project folder and run:

```
python tracker.py
```

## Example
```
===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. View Total
4. Category Total
5. Exit
```

## What I learned
- Reading and writing CSV files
- Validating user input with try/except
- Organizing code into small functions
- Using dictionaries to group data

## Planned features
- Delete and edit expenses
- Monthly budget warnings
- SQLite database
- Web interface and AI-powered entry