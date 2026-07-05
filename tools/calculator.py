class FinanceCalculator:

    @staticmethod
    def total_expenses(expenses):

        return sum(expenses.values())

    @staticmethod
    def remaining_balance(income, expenses):

        return income - sum(expenses.values())

    @staticmethod
    def savings_rate(income, expenses):

        total = sum(expenses.values())

        remaining = income - total

        if income == 0:
            return 0

        return round(
            remaining / income * 100,
            2
        )

    @staticmethod
    def highest_expense(expenses):

        if not expenses:
            return None

        return max(
            expenses,
            key=expenses.get
        )