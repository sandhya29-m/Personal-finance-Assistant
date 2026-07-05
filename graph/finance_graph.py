from langgraph.graph import StateGraph, END

from graph.state import FinanceState

from agents.parser_agent import ParserAgent
from agents.manager import ManagerAgent
from agents.expense_agent import ExpenseAnalysisAgent
from agents.budget_agent import BudgetPlanningAgent
from agents.finance_qa_agent import FinanceQAAgent
from agents.planning_agent import FinancialPlanningAgent
from agents.response_agent import ResponseAgent


# ===========================================================
# Nodes
# ===========================================================

def parser_node(state: FinanceState):
    return ParserAgent.run(state)


def manager_node(state: FinanceState):
    return ManagerAgent.run(state)


def expense_node(state: FinanceState):
    return ExpenseAnalysisAgent.run(state)


def budget_node(state: FinanceState):
    return BudgetPlanningAgent.run(state)


def finance_node(state: FinanceState):
    return FinanceQAAgent.run(state)


def planning_node(state: FinanceState):
    return FinancialPlanningAgent.run(state)


def response_node(state: FinanceState):
    return ResponseAgent.run(state)


# ===========================================================
# Routing
# ===========================================================

def after_manager(state: FinanceState):

    plan = state.get("execution_plan", [])

    if "expense" in plan:
        return "expense"

    if "finance" in plan:
        return "finance"

    if "planning" in plan:
        return "planning"

    return "response"


def after_expense(state: FinanceState):

    plan = state.get("execution_plan", [])

    if "budget" in plan:
        return "budget"

    if "planning" in plan:
        return "planning"

    return "response"


def after_budget(state: FinanceState):

    if "planning" in state.get("execution_plan", []):
        return "planning"

    return "response"


def after_finance(state: FinanceState):

    if "planning" in state.get("execution_plan", []):
        return "planning"

    return "response"


def after_planning(state: FinanceState):

    return "response"
# ===========================================================
# Graph Builder
# ===========================================================

builder = StateGraph(FinanceState)

# ----------------------------
# Register Nodes
# ----------------------------

builder.add_node("parser", parser_node)
builder.add_node("manager", manager_node)
builder.add_node("expense", expense_node)
builder.add_node("budget", budget_node)
builder.add_node("finance", finance_node)
builder.add_node("planning", planning_node)
builder.add_node("response", response_node)

# ----------------------------
# Entry Point
# ----------------------------

builder.set_entry_point("parser")

# ----------------------------
# Parser → Manager
# ----------------------------

builder.add_edge(
    "parser",
    "manager"
)

# ----------------------------
# Manager Routing
# ----------------------------

builder.add_conditional_edges(

    "manager",

    after_manager,

    {

        "expense": "expense",

        "finance": "finance",

        "planning": "planning",

        "response": "response"

    }

)

# ----------------------------
# Expense Routing
# ----------------------------

builder.add_conditional_edges(

    "expense",

    after_expense,

    {

        "budget": "budget",

        "planning": "planning",

        "response": "response"

    }

)

# ----------------------------
# Budget Routing
# ----------------------------

builder.add_conditional_edges(

    "budget",

    after_budget,

    {

        "planning": "planning",

        "response": "response"

    }

)

# ----------------------------
# Finance Routing
# ----------------------------

builder.add_conditional_edges(

    "finance",

    after_finance,

    {

        "planning": "planning",

        "response": "response"

    }

)

# ----------------------------
# Planning Routing
# ----------------------------

builder.add_conditional_edges(

    "planning",

    after_planning,

    {

        "response": "response"

    }

)

# ----------------------------
# Finish
# ----------------------------

builder.add_edge(
    "response",
    END
)

# ----------------------------
# Compile Graph
# ----------------------------

finance_graph = builder.compile()