from flask import Blueprint, jsonify, request

from application.model.expense import Expense, ExpenseSchema
from application.model.income import Income, IncomeSchema
from application.model.transaction_type import TransactionType


cashman_blueprint = Blueprint("cashman_blueprint", __name__)

transactions = [
        Income('Salary', 5000),
        Income('Dividends', 200),
        Expense('piza', 50),
        Expense('Rock concert', 100)
]

@cashman_blueprint.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
            filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    print(f'incomes: {incomes}')
    
    #return jsonify(incomes.data)
    return jsonify(incomes)
    
@cashman_blueprint.route('/incomes', methods=["POST"])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)#removed .data
    return '', 204

@cashman_blueprint.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
            filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    #return jsonify(expenses.data)
    return jsonify(expenses)

@cashman_blueprint.route('/expenses', methods=["POST"])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)#removed .data
    return "", 204
