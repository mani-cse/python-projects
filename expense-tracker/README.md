 # 💰 Personal Expense & Budget Tracker

A command-line **Expense Tracker** built in Python using Object-Oriented Programming. It helps users log daily expenses, set category-wise budgets, and get alerted when spending exceeds the limit — with all data automatically saved to a CSV file.

## 📋 Features

- **Add Expense** – Log an expense with category, amount, and auto-generated timestamp
- **View Expenses** – Display all recorded expenses with date, category, and amount
- **Set Budget** – Set a spending limit for any category (e.g. FOOD, TRAVEL)
- **Budget Alerts** – Automatically warns when spending in a category exceeds its set budget
- **Delete Expense** – Remove a specific expense record by index
- **Generate Report** – View a category-wise summary of total spending
- **CSV Persistence** – All expenses are saved to `expenses.csv` and reloaded automatically the next time the program runs

## 🛠️ Technologies & Concepts Used

- **Python 3**
- **Object-Oriented Programming (OOP)** – Class-based design to manage expenses and budgets
- **File Handling** – Reading/writing data using the `csv` module
- **`datetime` module** – Auto-timestamping each expense
- **Exception-safe file checks** – Uses `os.path.exists()` to avoid errors on first run
- **Menu-driven loop** – Continuous `while` loop with `if-elif` based navigation

## 🚀 How to Run

1. Clone this repository:
```bash
   git clone https://github.com/mani-cse/python-projects.git
   cd python-projects/expense-tracker
```
2. Run the script:
```bash
   python expense_tracker.py
```
3. Use the menu to add expenses, set budgets, view records, or generate a report. Data is automatically saved to `expenses.csv` in the same folder.

## 📸 Sample Menu
------- Expense Tracker Menu --------

Add Expense
View Expense
Set Budget
Delete Expense
Generate Report
Exit
Enter Your Choice (1-6):


## 🖥️ Demo

![Expense Tracker Demo](demo_screenshot.png)

## 🔮 Future Improvements

- Migrate storage from CSV to a database (SQLite) for larger datasets
- Add monthly/date-range filtering for reports
- Add input validation (e.g. negative amounts, empty categories)
- Visualize spending with charts (matplotlib)

## 👤 Author

**Manikandan**
- GitHub: [@mani-cse](https://github.com/mani-cse)
- B.E. Electrical and Electronics Engineering | Aspiring Python Developer
