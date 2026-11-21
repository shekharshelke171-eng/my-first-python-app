
from expense_manager import (
    initialize_file,
    add_expense,
    view_expenses,
    delete_expense
)

from calculations import (
    daily_total,
    monthly_total,
    category_summary
)

from config import CATEGORIES


def main():
    initialize_file()

    while True:
        print("\n" + "=" * 45)
        print("       DAILY EXPENSE CALCULATOR")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Daily Expense Summary")
        print("5. Monthly Expense Summary")
        print("6. Category-wise Summary")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAVAILABLE CATEGORIES")

            for index, category in enumerate(CATEGORIES, start=1):
                print(f"{index}. {category}")

            try:
                category_choice = int(input("Select category number: "))

                if not 1 <= category_choice <= len(CATEGORIES):
                    print("Invalid category selection.")
                    continue

                category = CATEGORIES[category_choice - 1]

                description = input("Enter description: ").strip()

                if not description:
                    print("Description cannot be empty.")
                    continue

                amount = float(input("Enter amount (Rs.): "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                add_expense(category, description, amount)

            except ValueError:
                print("Please enter valid input.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            try:
                expense_id = int(input("Enter Expense ID: "))

                if expense_id <= 0:
                    print("Enter a valid positive ID.")
                    continue

                delete_expense(expense_id)

            except ValueError:
                print("Please enter a valid ID.")

        elif choice == "4":
            daily_total()

        elif choice == "5":
            monthly_total()

        elif choice == "6":
            category_summary()

        elif choice == "7":
            print("\nThank you for using Daily Expense Calculator!")
            print("Have a great day!")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
