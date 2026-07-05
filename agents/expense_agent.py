# agents/expense_agent.py

from graph.state import FinanceState
from tools.calculator import FinanceCalculator


class ExpenseAnalysisAgent:
    """
    Expense Analysis Agent

    Responsibilities:
    - Calculate total expenses
    - Calculate remaining balance
    - Calculate savings rate
    - Find highest expense
    - Generate basic financial analysis
    """

    @staticmethod
    def run(state: FinanceState) -> FinanceState:

        income = state.get("monthly_income", 0)

        expenses = state.get("expenses", {})

        # -----------------------------
        # Calculations
        # -----------------------------

        total_expense = FinanceCalculator.total_expenses(
            expenses
        )

        remaining_balance = FinanceCalculator.remaining_balance(
            income,
            expenses
        )

        savings_rate = FinanceCalculator.savings_rate(
            income,
            expenses
        )

        highest_expense = FinanceCalculator.highest_expense(
            expenses
        )

        # -----------------------------
        # Rule-Based Analysis
        # -----------------------------

        analysis = []

        analysis.append(
            f"Monthly Income : ₹{income:,.2f}"
        )

        analysis.append(
            f"Total Expenses : ₹{total_expense:,.2f}"
        )

        analysis.append(
            f"Remaining Balance : ₹{remaining_balance:,.2f}"
        )

        analysis.append(
            f"Savings Rate : {savings_rate:.2f}%"
        )

        if highest_expense:

            analysis.append(
                f"Highest Expense Category : {highest_expense}"
            )

        # -----------------------------
        # Suggestions
        # -----------------------------

        if savings_rate >= 30:

            analysis.append(
                "Excellent! Your savings rate is very healthy."
            )

        elif savings_rate >= 20:

            analysis.append(
                "Good savings rate. Try increasing it gradually."
            )

        elif savings_rate >= 10:

            analysis.append(
                "Savings are moderate. Reduce unnecessary spending."
            )

        elif savings_rate >= 0:

            analysis.append(
                "Your savings are low. Review discretionary expenses."
            )

        else:

            analysis.append(
                "Warning: Your expenses exceed your income."
            )

        # -----------------------------
        # Update State
        # -----------------------------

        state["total_expense"] = total_expense

        state["remaining_balance"] = remaining_balance

        state["savings_rate"] = savings_rate

        state["highest_expense_category"] = highest_expense

        state["analysis"] = "\n".join(analysis)

        return state