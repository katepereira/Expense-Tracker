# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from data_storage import DataStorage
from expenses import Expense

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

data_storage = DataStorage()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']  # Add this line to capture the date input
        expense = Expense(amount, name, category, date)  # Pass all arguments to the constructor
        data_storage.add_expense(expense)
        flash("Expense added successfully!", "success")
    except ValueError:
        flash("Invalid input. Please enter a valid amount.", "error")
    return redirect(url_for('index'))

@app.route('/view_expenses')
def view_expenses():
    expenses = data_storage.get_expenses()
    total_spent = sum(expense.amount for expense in expenses)
    return render_template('view_expenses.html', expenses=expenses, total_spent=total_spent)

if __name__ == '__main__':
    app.run(debug=True)