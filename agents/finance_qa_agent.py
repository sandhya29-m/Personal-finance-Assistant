# agents/finance_qa_agent.py

from graph.state import FinanceState
from models.llm import llm


class FinanceQAAgent:
    """
    Answers finance-related questions only.
    """

    SYSTEM_PROMPT = """
You are an AI Personal Finance Coach.

Your responsibility is to answer finance-related questions in simple,
clear English.

Topics you can answer:

- Budgeting
- Savings
- SIP
- Mutual Funds
- Stocks
- Inflation
- Taxes
- Insurance
- Loans
- Credit Score
- Emergency Fund
- Retirement Planning
- Fixed Deposits
- Recurring Deposits

Guidelines:

1. Explain simply.

2. Give practical examples.

3. Keep answers below 200 words.

4. Never provide guaranteed investment returns.

5. If investment advice is requested,
recommend consulting a certified financial advisor.

6. Use bullet points whenever possible.
"""

    @staticmethod
    def run(state: FinanceState):

        query = state.get("user_query", "")

        prompt = f"""
{FinanceQAAgent.SYSTEM_PROMPT}

User Question:

{query}
"""

        response = llm.invoke(prompt)

        state["finance_answer"] = response.content

        return state