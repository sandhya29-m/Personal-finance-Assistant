# agents/budget_agent.py

from graph.state import FinanceState
from tools.budget import BudgetPlanner


class BudgetPlanningAgent:
    """
    Budget Planning Agent

    Uses the 50-30-20 budgeting rule.

    50% Needs
    30% Wants
    20% Savings
    """

    NEEDS = {
        "Rent",
        "Food",
        "Bills",
        "Utilities",
        "Insurance",
        "Medicine",
        "Transport",
        "Transportation"
    }

    WANTS = {
        "Shopping",
        "Entertainment",
        "Travel",
        "Dining",
        "Movies",
        "Subscriptions"
    }

    @staticmethod
    def run(state: FinanceState):

        income = state.get("monthly_income", 0)

        expenses = state.get("expenses", {})

        recommended = BudgetPlanner.generate(income)

        needs_spent = 0
        wants_spent = 0
        others = 0

        for category, amount in expenses.items():

            if category in BudgetPlanningAgent.NEEDS:
                needs_spent += amount

            elif category in BudgetPlanningAgent.WANTS:
                wants_spent += amount

            else:
                others += amount

        savings = income - (
            needs_spent +
            wants_spent +
            others
        )

        advice = []

        advice.append("📊 Budget Summary\n")

        advice.append(
            f"Needs Budget : ₹{recommended['Needs']:,.2f}"
        )

        advice.append(
            f"Needs Spent : ₹{needs_spent:,.2f}"
        )

        advice.append("")

        advice.append(
            f"Wants Budget : ₹{recommended['Wants']:,.2f}"
        )

        advice.append(
            f"Wants Spent : ₹{wants_spent:,.2f}"
        )

        advice.append("")

        advice.append(
            f"Recommended Savings : ₹{recommended['Savings']:,.2f}"
        )

        advice.append(
            f"Current Savings : ₹{savings:,.2f}"
        )

        advice.append("")

        # ------------------------------------
        # Suggestions
        # ------------------------------------

        if needs_spent > recommended["Needs"]:

            advice.append(
                "⚠️ Your essential expenses are higher than recommended."
            )

        if wants_spent > recommended["Wants"]:

            advice.append(
                "⚠️ Reduce discretionary spending like shopping or entertainment."
            )

        if savings < recommended["Savings"]:

            advice.append(
                "⚠️ Increase your monthly savings to reach the recommended 20%."
            )

        if (
            needs_spent <= recommended["Needs"]
            and wants_spent <= recommended["Wants"]
            and savings >= recommended["Savings"]
        ):

            advice.append(
                "✅ Great! You're following the 50-30-20 budgeting rule."
            )

        advice.append("")
        advice.append("💡 Budget Tips")

        advice.append(
            "• Track expenses every month."
        )

        advice.append(
            "• Avoid impulse purchases."
        )

        advice.append(
            "• Save before spending."
        )

        advice.append(
            "• Maintain an emergency fund."
        )

        state["recommended_budget"] = recommended

        state["budget_advice"] = "\n".join(advice)

        return state