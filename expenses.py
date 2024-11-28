# expenses.py

class Expense:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.description} - {self.amount} - {self.category} - {self.date}"