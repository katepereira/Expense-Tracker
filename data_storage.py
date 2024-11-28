import json
from expenses import Expense

class DataStorage:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                data = json.load(file)
                # Ensure all required fields are present
                return [
                    Expense(
                        amount=expense.get('amount'),
                        description=expense.get('description'),
                        category=expense.get('category'),
                        date=expense.get('date', '1970-01-01')  # Provide a default date if missing
                    ) for expense in data
                ]
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist
        except json.JSONDecodeError:
            return []  # Return an empty list if there's an error decoding JSON

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump([expense.__dict__ for expense in self.expenses], file)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def get_expenses(self):
        return self.expenses