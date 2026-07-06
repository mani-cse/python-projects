import csv
import os
from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = {}
        self.load_from_csv()

    def load_from_csv(self):
        if not os.path.exists("expenses.csv"):
            return

        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                expense = {
                    "category": row[0],
                    "amount": float(row[1]),
                    "date": row[2]
                }
                self.expenses.append(expense)
            print("Previous Expenses Loaded Successfully!")

    def set_budget(self, category, limit):
        self.budget[category] = limit
        print("Budget Set For", category, ":", limit)

    def add_expense(self, category, amount):
        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        expense = {
            "category": category,
            "amount": amount,
            "date": date
        }
        self.expenses.append(expense)
        print("Added", amount, "- $", category)
        self.check_budget_alert(category)
        self.save_to_csv()

    def check_budget_alert(self, category):
        if category not in self.budget:
            return

        total_spend = 0
        for exp in self.expenses:
            if exp["category"] == category:
                total_spend += exp["amount"]

        if total_spend > self.budget[category]:
            print("ALERT: You Exceeded your", category, "Budget! Spent:", total_spend, "Limit", self.budget[category])

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.save_to_csv()
            print("Deleted:", removed)
        else:
            print("Invalid index! Please check and try again")

    def generate_report(self):
        if not self.expenses:
            print("No Expenses to Summarize!")
            return
        summary = {}
        for exp in self.expenses:
            cat = exp["category"]
            summary[cat] = summary.get(cat, 0) + exp["amount"]

        print("\n----- Expense Report (By Category) -----")
        total = 0
        for cat, amt in summary.items():
            print(cat, ":", amt)
            total += amt
        print("-----------------------------------------")
        print("Total Spent:", total)

    def view_expenses(self):
        if not self.expenses:
            print("No Expenses Recorded yet!")
        for i, exp in enumerate(self.expenses):
            print(i, "- DATE:", exp["date"], "CATEGORY:", exp["category"], "AMOUNT:", exp["amount"])

    def save_to_csv(self):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount", "Date"])
            for exp in self.expenses:
                writer.writerow([exp["category"], exp["amount"], exp["date"]])


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n ------- Expense Tracker Menu --------")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Set Budget")
        print("4. Delete Expense")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6): ")

        if choice == "1":
            category = input("Enter Category (e.g. FOOD, TRAVEL...): ")
            amount = float(input("Enter Amount: "))
            tracker.add_expense(category, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter category for budget: ")
            limit = float(input("Enter budget: "))
            tracker.set_budget(category, limit)

        elif choice == "4":
            tracker.view_expenses()
            index = int(input("Enter index of expense to delete: "))
            tracker.delete_expense(index)

        elif choice == "5":
            tracker.generate_report()

        elif choice == "6":
            print("Exiting....Good Bye!")
            break
        else:
            print("Invalid choice! Please enter 1-6.")


main()