
import csv
import pytest

import expense_manager

from expense_manager import (
    initialize_file,
    add_expense,
    view_expenses,
    delete_expense
)


@pytest.fixture
def temporary_csv(tmp_path, monkeypatch):
    test_file = tmp_path / "expenses.csv"

    monkeypatch.setattr(
        expense_manager,
        "EXPENSE_FILE",
        str(test_file)
    )

    initialize_file()
    return test_file


def test_initialize_file(temporary_csv):
    assert temporary_csv.exists()


def test_add_expense(temporary_csv):
    add_expense("Food", "Lunch", 150)

    with open(temporary_csv, newline="") as file:
        expenses = list(csv.DictReader(file))

    assert len(expenses) == 1
    assert expenses[0]["Category"] == "Food"
    assert expenses[0]["Description"] == "Lunch"
    assert float(expenses[0]["Amount"]) == 150.0


def test_view_expenses(temporary_csv, capsys):
    add_expense("Food", "Lunch", 150)

    view_expenses()

    output = capsys.readouterr().out

    assert "Lunch" in output
    assert "150.00" in output


def test_delete_expense(temporary_csv):
    add_expense("Food", "Lunch", 150)

    delete_expense(1)

    with open(temporary_csv, newline="") as file:
        expenses = list(csv.DictReader(file))

    assert len(expenses) == 0


def test_delete_invalid_expense(temporary_csv, capsys):
    delete_expense(999)

    output = capsys.readouterr().out

    assert "Expense ID not found" in output
