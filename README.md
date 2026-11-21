
# Daily Expense Calculator

A simple and user-friendly Python-based application to record, manage, and analyze daily expenses.

## 1. Project Overview

The Daily Expense Calculator is a command-line application developed using Python. It helps users maintain a record of their daily spending, organize expenses into categories, and calculate daily and monthly expenditure.

The application stores expense records in a CSV file, making data management simple and lightweight without requiring an external database.

## 2. Problem Statement

Managing daily expenses manually can be difficult and time-consuming. Users may find it challenging to track their spending, maintain records, and understand where their money is being spent.

This project provides a simple digital solution to record expenses, manage transactions, and generate expense summaries.

## 3. Project Objectives

- To develop a simple expense management application using Python.
- To record daily expenses with date, category, description, and amount.
- To provide options to view and delete expense records.
- To calculate daily and monthly expenditure.
- To generate category-wise expense summaries.
- To implement automated testing using pytest.

## 4. Key Features

- Add new expense records.
- Select expenses from predefined categories.
- View all recorded expenses.
- Delete expenses using Expense ID.
- Calculate today's total expenditure.
- Calculate current month's total expenditure.
- Generate category-wise expense summaries.
- Store records permanently in a CSV file.
- Validate user input.
- Automated testing using pytest.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| CSV | Expense data storage |
| Pytest | Automated testing |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Source code hosting |

## 6. Expense Categories

The application supports the following categories:

1. Food
2. Travel
3. Shopping
4. Entertainment
5. Healthcare
6. Education
7. Other

## 7. Project Structure

```text
my-first-python-app/
│
├── data/
│   └── expenses.csv
│
├── tests/
│   └── test_expenses.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── calculations.py
├── config.py
├── expense_manager.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 8. Installation and Setup

### Prerequisites

- Python 3.10 or above
- Visual Studio Code
- pip package manager

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to Project Folder

```bash
cd my-first-python-app
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 9. How to Run the Application

Execute the following command:

```bash
python main.py
```

The application will display a menu with the following options:

```text
=============================================
       DAILY EXPENSE CALCULATOR
=============================================
1. Add Expense
2. View All Expenses
3. Delete Expense
4. Daily Expense Summary
5. Monthly Expense Summary
6. Category-wise Summary
7. Exit
=============================================
```

Select an option by entering its corresponding number.

## 10. Data Storage

All expense records are stored in:

`data/expenses.csv`

The CSV file contains the following fields:

| Field | Description |
|---|---|
| ID | Unique expense identifier |
| Date | Expense transaction date |
| Category | Expense category |
| Description | Details of the expense |
| Amount | Expense amount |

## 11. Automated Testing

The project uses pytest for automated testing.

Run the following command:

```bash
python -m pytest tests/test_expenses.py -v
```

### Test Results

| Test Case | Status |
|---|---|
| File Initialization | PASSED |
| Add Expense | PASSED |
| View Expenses | PASSED |
| Delete Expense | PASSED |
| Invalid Expense ID | PASSED |

**Total Test Cases: 5**

**Result: 5 Passed, 0 Failed**

## 12. Future Enhancements

- Graphical User Interface (GUI).
- Monthly expense visualization using charts.
- Export expense reports to PDF and Excel.
- Search and filter expenses by date and category.
- Budget management and spending alerts.
- Database integration using SQLite or MySQL.

## 13. Conclusion

The Daily Expense Calculator demonstrates the practical implementation of Python programming concepts, file handling, modular programming, data management, input validation, and automated testing.

The application provides a simple and effective solution for tracking personal expenses and understanding spending patterns.

---

**Project:** Daily Expense Calculator  
**Language:** Python  
**Testing Framework:** Pytest  
**Storage:** CSV
