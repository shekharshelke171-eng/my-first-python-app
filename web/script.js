
const expenseForm = document.getElementById("expenseForm");
const expenseList = document.getElementById("expenseList");

let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

const today = new Date();
const todayString = formatDate(today);

document.getElementById("todayDate").textContent =
    today.toLocaleDateString("en-IN", {
        day: "2-digit",
        month: "long",
        year: "numeric"
    });

document.getElementById("expenseDate").value = todayString;


function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");

    return `${year}-${month}-${day}`;
}


function saveExpenses() {
    localStorage.setItem("expenses", JSON.stringify(expenses));
}


function formatAmount(amount) {
    return "₹" + Number(amount).toFixed(2);
}


function renderExpenses() {
    expenseList.innerHTML = "";

    if (expenses.length === 0) {
        expenseList.innerHTML = `
            <tr>
                <td colspan="6" style="text-align:center;">
                    No expenses found.
                </td>
            </tr>
        `;
    } else {
        expenses.forEach(expense => {
            const row = document.createElement("tr");

            const values = [
                expense.id,
                expense.date,
                expense.category,
                expense.description,
                formatAmount(expense.amount)
            ];

            values.forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            });

            const actionCell = document.createElement("td");
            const deleteButton = document.createElement("button");

            deleteButton.textContent = "Delete";
            deleteButton.className = "delete-btn";
            deleteButton.addEventListener("click", () => {
                deleteExpense(expense.id);
            });

            actionCell.appendChild(deleteButton);
            row.appendChild(actionCell);

            expenseList.appendChild(row);
        });
    }

    updateSummary();
    updateCategorySummary();
}


function addExpense(event) {
    event.preventDefault();

    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value.trim();
    const amount = Number(document.getElementById("amount").value);
    const date = document.getElementById("expenseDate").value;

    if (!category || !description || !date || !Number.isFinite(amount) || amount <= 0) {
        alert("Please enter valid expense details.");
        return;
    }

    const expense = {
        id: expenses.length
            ? Math.max(...expenses.map(item => item.id)) + 1
            : 1,
        date,
        category,
        description,
        amount
    };

    expenses.push(expense);

    saveExpenses();
    renderExpenses();

    expenseForm.reset();
    document.getElementById("expenseDate").value = todayString;

    alert("Expense added successfully!");
}


function deleteExpense(id) {
    const confirmed = confirm("Are you sure you want to delete this expense?");

    if (!confirmed) {
        return;
    }

    expenses = expenses.filter(expense => expense.id !== id);

    saveExpenses();
    renderExpenses();
}


function updateSummary() {
    const todayTotal = expenses
        .filter(expense => expense.date === todayString)
        .reduce((total, expense) => total + expense.amount, 0);

    const currentMonth = todayString.substring(0, 7);

    const monthlyTotal = expenses
        .filter(expense => expense.date.startsWith(currentMonth))
        .reduce((total, expense) => total + expense.amount, 0);

    const overallTotal = expenses.reduce(
        (total, expense) => total + expense.amount,
        0
    );

    document.getElementById("totalExpense").textContent =
        formatAmount(overallTotal);

    document.getElementById("dailyExpense").textContent =
        formatAmount(todayTotal);

    document.getElementById("monthlyExpense").textContent =
        formatAmount(monthlyTotal);
}


function updateCategorySummary() {
    const summaryElement = document.getElementById("categorySummary");
    const summary = {};

    expenses.forEach(expense => {
        summary[expense.category] =
            (summary[expense.category] || 0) + expense.amount;
    });

    summaryElement.innerHTML = "";

    if (Object.keys(summary).length === 0) {
        summaryElement.textContent = "No expenses available.";
        return;
    }

    Object.entries(summary).forEach(([category, total]) => {
        const item = document.createElement("div");
        item.className = "category-item";

        const name = document.createElement("span");
        name.textContent = category;

        const amount = document.createElement("strong");
        amount.textContent = formatAmount(total);

        item.appendChild(name);
        item.appendChild(amount);

        summaryElement.appendChild(item);
    });
}


expenseForm.addEventListener("submit", addExpense);

renderExpenses();
