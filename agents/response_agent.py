# agents/response_agent.py

from graph.state import FinanceState


class ResponseAgent:
    """
    Collects responses from all executed agents and
    prepares the final markdown response.
    """

    @staticmethod
    def run(state: FinanceState):

        sections = []

        # -----------------------------
        # Expense Analysis
        # -----------------------------

        if state.get("analysis"):

            sections.append(
                "# 📊 Expense Analysis\n"
            )

            sections.append(
                state["analysis"]
            )

            sections.append("\n")

        # -----------------------------
        # Budget Advice
        # -----------------------------

        if state.get("budget_advice"):

            sections.append(
                "# 💰 Budget Recommendation\n"
            )

            sections.append(
                state["budget_advice"]
            )

            sections.append("\n")

        # -----------------------------
        # Finance Q&A
        # -----------------------------

        if state.get("finance_answer"):

            sections.append(
                "# 📚 Finance Information\n"
            )

            sections.append(
                state["finance_answer"]
            )

            sections.append("\n")

        # -----------------------------
        # Financial Planning
        # -----------------------------

        if state.get("financial_plan"):

            sections.append(
                "# 🎯 Financial Plan\n"
            )

            sections.append(
                state["financial_plan"]
            )

            sections.append("\n")

        # -----------------------------
        # Footer
        # -----------------------------

        sections.append(
            "---"
        )

        sections.append(
            "💡 **Finance Tip:** Track every rupee you spend. Small savings made consistently often have a greater long-term impact than occasional large savings."
        )

        state["final_response"] = "\n".join(sections)

        return state