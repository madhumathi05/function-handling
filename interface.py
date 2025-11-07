import csv
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"

# Function to add an expense
def add_expense(category, amount, description):
    try:
        with open(FILE_NAME, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().date(), category, amount, description])
        print("✅ Expense added successfully.")
    except Exception as e:
        print(f"❌ Error saving expense: {e}")

# Function to generate monthly report
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
        print("⚠️ No expense file found. Start by adding expenses.")

# Main menu loop
def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Expense")
        print("2. Generate Monthly Report")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Travel): ")
            try:
                amount = float(input("Enter amount: ₹"))
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                continue
            description = input("Enter description: ")
            add_expense(category, amount, description)

        elif choice == "2":
            try:
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2025): "))
                generate_monthly_report(month, year)
            except ValueError:
                print("❌ Invalid month or year. Please enter numbers.")
                continue

        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

main()
