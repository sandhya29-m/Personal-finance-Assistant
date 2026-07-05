# agents/manager.py

from graph.state import FinanceState


class ManagerAgent:
    """
    Decides which agents should execute.

    It DOES NOT solve the problem.
    It only creates an execution plan.
    """

    @staticmethod
    def run(state: FinanceState) -> FinanceState:

        query = state.get("user_query", "").lower()

        execution_plan = []

        # -----------------------------
        # Expense Analysis
        # -----------------------------

        expense_keywords = [
            "expense",
            "expenses",
            "income",
            "salary",
            "rent",
            "food",
            "shopping",
            "travel",
            "bill",
            "bills",
            "spend",
            "spent"
        ]

        # -----------------------------
        # Budget Planning
        # -----------------------------

        budget_keywords = [
            "budget",
            "save",
            "saving",
            "reduce expense",
            "reduce spending",
            "money management"
        ]

        # -----------------------------
        # Financial Planning
        # -----------------------------

        planning_keywords = [
            "goal",
            "buy",
            "car",
            "house",
            "bike",
            "future",
            "investment",
            "retirement",
            "education"
        ]

        # -----------------------------
        # Finance Q&A
        # -----------------------------

        finance_keywords = [
            "sip",
            "mutual fund",
            "stock",
            "fd",
            "inflation",
            "loan",
            "insurance",
            "tax",
            "credit score",
            "compound interest",
            "emi"
        ]

        # -----------------------------
        # Routing
        # -----------------------------

        if any(word in query for word in expense_keywords):
            execution_plan.append("expense")

        if any(word in query for word in budget_keywords):
            execution_plan.append("budget")

        if any(word in query for word in planning_keywords):
            execution_plan.append("planning")

        if any(word in query for word in finance_keywords):
            execution_plan.append("finance")

        # Default

        if not execution_plan:
            execution_plan.append("finance")

        # Remove duplicates

        execution_plan = list(dict.fromkeys(execution_plan))

        state["execution_plan"] = execution_plan

        return state