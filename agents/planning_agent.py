# agents/planning_agent.py

import re

from graph.state import FinanceState
from models.llm import llm


class FinancialPlanningAgent:

    @staticmethod
    def extract_goal_details(goal: str):

        amount = 0
        years = 1

        # -------------------------
        # Extract Amount
        # -------------------------

        numbers = re.findall(r"\d[\d,]*", goal)

        if numbers:
            amount = int(
                numbers[0].replace(",", "")
            )

        # -------------------------
        # Extract Years
        # -------------------------

        year_match = re.search(
            r"(\d+)\s*year",
            goal.lower()
        )

        if year_match:

            years = int(
                year_match.group(1)
            )

        return amount, years

    @staticmethod
    def investment_suggestion(years):

        if years <= 2:

            return "Recurring Deposit (RD) or Fixed Deposit (FD)"

        elif years <= 5:

            return "Hybrid Mutual Fund or SIP"

        else:

            return "Equity Mutual Fund SIP"

    @staticmethod
    def run(state: FinanceState):

        goal = state.get(
            "financial_goal",
            ""
        )

        income = state.get(
            "monthly_income",
            0
        )

        savings = state.get(
            "remaining_balance",
            0
        )

        amount, years = FinancialPlanningAgent.extract_goal_details(
            goal
        )

        months = max(1, years * 12)

        required_monthly = amount / months if amount else 0

        achievable = savings >= required_monthly

        investment = FinancialPlanningAgent.investment_suggestion(
            years
        )

        prompt = f"""
You are a professional financial advisor.

Income:
₹{income}

Current Monthly Savings:
₹{savings}

Financial Goal:
{goal}

Goal Amount:
₹{amount}

Time:
{years} years

Required Monthly Savings:
₹{required_monthly:.2f}

Goal Achievable:
{"Yes" if achievable else "No"}

Recommended Investment:
{investment}

Generate a friendly financial roadmap.

Include

1. Monthly saving strategy

2. Investment suggestion

3. Things to avoid

4. Emergency fund advice

Keep under 180 words.
"""

        response = llm.invoke(prompt)

        report = f"""
🎯 Financial Goal

{goal}

Goal Amount : ₹{amount:,.2f}

Duration : {years} years

Monthly Saving Required : ₹{required_monthly:,.2f}

Current Monthly Savings : ₹{savings:,.2f}

Goal Achievable : {"Yes ✅" if achievable else "No ❌"}

Suggested Investment

{investment}

----------------------------------------

{response.content}
"""

        state["financial_plan"] = report

        return state