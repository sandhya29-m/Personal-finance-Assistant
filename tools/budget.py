class BudgetPlanner:

    @staticmethod
    def generate(income):

        return {

            "Needs": income * 0.50,

            "Wants": income * 0.30,

            "Savings": income * 0.20

        }