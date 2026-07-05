from fastapi import FastAPI
from pydantic import BaseModel
from graph.finance_graph import finance_graph

app = FastAPI(
    title="Personal Finance Coach API",
    version="1.0.0"
)


class FinanceRequest(BaseModel):
    user_query: str
    monthly_income: float = 0
    expenses: dict = {}
    financial_goal: str = ""
    history: list = []


@app.get("/")
def home():
    return {
        "message": "Personal Finance Coach API Running"
    }


@app.post("/chat")
def chat(request: FinanceRequest):

    state = {

        "user_query": request.user_query,

        "monthly_income": request.monthly_income,

        "expenses": request.expenses,

        "financial_goal": request.financial_goal,

        "history": request.history

    }

    result = finance_graph.invoke(state)

    return {

        "response": result["final_response"],

        "analysis": result.get("analysis", ""),

        "budget": result.get("budget_advice", ""),

        "finance_answer": result.get("finance_answer", ""),

        "financial_plan": result.get("financial_plan", "")

    }