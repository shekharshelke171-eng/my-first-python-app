
import csv
import os
from datetime import datetime

from config import EXPENSE_FILE, DATE_FORMAT, CSV_FIELDS


def initialize_file():
    os.makedirs(os.path.dirname(EXPENSE_FILE), exist_ok=True)

    if not os.path.exists(EXPENSE_FILE) or os.path.getsize(EXPENSE_FILE) == 0:
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            writer.writeheader()


def add_expense(category, description, amount):
    initialize_file()

    with open(EXPENSE_FILE, "r", newline="") as file:
        expenses = list(csv.DictReader(file))

    expense_id = max(
        [int(row["ID"]) for row in expenses],
        default=0
    ) + 1

    expense = {
        "ID": expense_id,
        "Date": datetime.now().strftime(DATE_FORMAT),
        "Category": category,
        "Description": description,
        "Amount": f"{amount:.2f}"
    }

    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writerow(expense)

    print("\nExpense added successfully!")


def view_expenses():
    initialize_file()

    with open(EXPENSE_FILE, "r", newline="") as file:
        expenses = list(csv.DictReader(file))

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)
    print(f"{'ID':<5}{'Date':<15}{'Category':<18}{'Description':<22}{'Amount':>12}")
    print("=" * 75)

    for expense in expenses:
        print(
            f"{expense['ID']:<5}"
            f"{expense['Date']:<15}"
            f"{expense['Category']:<18}"
            f"{expense['Description'][:20]:<22}"
            f"Rs. {float(expense['Amount']):>7.2f}"
        )

    print("=" * 75)


def delete_expense(expense_id):
    initialize_file()

    with open(EXPENSE_FILE, "r", newline="") as file:
        expenses = list(csv.DictReader(file))

    updated_expenses = [
        expense for expense in expenses
        if int(expense["ID"]) != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("\nExpense ID not found.")
        return

    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(updated_expenses)

    print("\nExpense deleted successfully!")
