
import csv
from datetime import datetime

from config import EXPENSE_FILE, DATE_FORMAT


def get_all_expenses():
    try:
        with open(EXPENSE_FILE, "r", newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def daily_total():
    expenses = get_all_expenses()
    today = datetime.now().strftime(DATE_FORMAT)

    total = sum(
        float(e["Amount"])
        for e in expenses
        if e["Date"] == today
    )

    print(f"\nToday's Total Expense: Rs. {total:.2f}")


def monthly_total():
    expenses = get_all_expenses()
    current_month = datetime.now().strftime("%Y-%m")

    total = sum(
        float(e["Amount"])
        for e in expenses
        if e["Date"].startswith(current_month)
    )

    print(f"\nMonthly Total Expense: Rs. {total:.2f}")


def category_summary():
    expenses = get_all_expenses()
    summary = {}

    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])

        summary[category] = summary.get(category, 0) + amount

    print("\n========== CATEGORY-WISE SUMMARY ==========")

    if not summary:
        print("No expenses available.")
        return

    for category, total in summary.items():
        print(f"{category:<20} Rs. {total:.2f}")
