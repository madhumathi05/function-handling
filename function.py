import csv
from datetime import datetime
from collections import defaultdict

# File name
FILE_NAME = "expenses.csv"

# Add an expense
def add_expense(category, amount, description):
    try:
        with open(FILE_NAME, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().date(), category, amount, description])
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error saving expense: {e}")

# Generate monthly report
def generate_monthly_report(month, year):
    expenses = defaultdict(float)
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 4:
                    continue
                date_str, category, amount, _ = row
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    if date.month == month and date.year == year:
                        expenses[category] += float(amount)
                except ValueError:
                    continue
        print(f"\n📊 Monthly Report for {month}/{year}")
        for cat, total in expenses.items():
            print(f"{cat}: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expense file found. Start by adding expenses.")
