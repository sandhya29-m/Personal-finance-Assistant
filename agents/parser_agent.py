# agents/parser_agent.py

import json
import re

from graph.state import FinanceState
from models.llm import llm


class ParserAgent:

    @staticmethod
    def extract_json(text: str):

        """
        Extract JSON object even if the LLM wraps it
        inside markdown or explanatory text.
        """

        text = text.strip()

        # Remove markdown fences

        text = re.sub(
            r"```json",
            "",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"```",
            "",
            text
        )

        # Find first JSON object

        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:

            return text[start:end + 1]

        return text

    @staticmethod
    def run(state: FinanceState):

        query = state.get(
            "user_query",
            ""
        )

        prompt = f"""
You are a financial data extraction engine.

Extract information from the user's message.

Return ONLY ONE valid JSON object.

Schema:

{{
  "monthly_income": number,
  "expenses": {{
      "Rent": number,
      "Food": number,
      "Shopping": number,
      "Travel": number,
      "Bills": number,
      "Insurance": number,
      "Medicine": number,
      "Entertainment": number,
      "Utilities": number,
      "Transport": number
  }},
  "financial_goal": "string"
}}

Rules

- Never return markdown.

- Never explain.

- Output JSON only.

- Convert

80k → 80000

9 lakh → 900000

1 crore → 10000000

If any field is missing

monthly_income = 0

expenses = {{}}

financial_goal = ""

User Message

{query}
"""

        try:

            response = llm.invoke(prompt)

            print("\n========== RAW RESPONSE ==========")
            print(response.content)
            print("==================================\n")

            cleaned = ParserAgent.extract_json(
                response.content
            )

            print("\n========== CLEANED JSON ==========")
            print(cleaned)
            print("==================================\n")

            data = json.loads(cleaned)

            print("\n========== PARSED ==========")
            print(data)
            print("============================\n")

        except Exception as e:

            print("\nParser Error")
            print(e)

            data = {}

        income = data.get(
            "monthly_income",
            0
        )

        expenses = data.get(
            "expenses",
            {}
        )

        goal = data.get(
            "financial_goal",
            ""
        )

        if income:

            state["monthly_income"] = float(income)

        if expenses:

            current = state.get(
                "expenses",
                {}
            )

            current.update(expenses)

            state["expenses"] = current

        if goal:

            state["financial_goal"] = goal

        print("\n========== FINAL STATE ==========")
        print(state)
        print("=================================\n")

        return state