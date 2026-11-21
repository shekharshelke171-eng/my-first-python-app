
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

EXPENSE_FILE = os.path.join(DATA_DIR, "expenses.csv")

CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Entertainment",
    "Healthcare",
    "Education",
    "Other"
]

DATE_FORMAT = "%Y-%m-%d"

CSV_FIELDS = ["ID", "Date", "Category", "Description", "Amount"]
