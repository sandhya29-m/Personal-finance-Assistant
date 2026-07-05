# graph/state.py

from typing import TypedDict, Dict, List, Optional


class FinanceState(TypedDict, total=False):
    """
    Shared state passed between every LangGraph node.
    Every agent reads from and writes to this state.
    """

    # ===========================
    # User Input
    # ===========================

    user_query: str

    monthly_income: float

    expenses: Dict[str, float]

    financial_goal: str

    # ===========================
    # Manager Routing
    # ===========================

    execution_plan: List[str]

    # ===========================
    # Expense Agent
    # ===========================

    total_expense: float

    remaining_balance: float

    savings_rate: float

    highest_expense_category: str

    analysis: str

    # ===========================
    # Budget Agent
    # ===========================

    recommended_budget: Dict[str, float]

    budget_advice: str

    # ===========================
    # Finance QA
    # ===========================

    finance_answer: str

    # ===========================
    # Planning
    # ===========================

    financial_plan: str

    # ===========================
    # Final Response
    # ===========================

    final_response: str

    # ===========================
    # Conversation Memory
    # ===========================

    history: List[Dict]

    # ===========================
    # Error Handling
    # ===========================

    error: Optional[str]