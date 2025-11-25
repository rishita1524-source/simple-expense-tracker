from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date.isoformat(),
            'created_at': self.created_at.isoformat()
        }

# Categories list
CATEGORIES = [
    'Food & Dining',
    'Transportation',
    'Shopping',
    'Entertainment',
    'Bills & Utilities',
    'Education',
    'Health & Fitness',
    'Travel',
    'Personal Care',
    'Other'
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return jsonify([expense.to_dict() for expense in expenses])

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.json
    try:
        expense = Expense(
            amount=float(data['amount']),
            category=data['category'],
            description=data.get('description', ''),
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )
        db.session.add(expense)
        db.session.commit()
        return jsonify(expense.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted successfully'}), 200

@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify(CATEGORIES)

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    expenses = Expense.query.all()
    
    total_expenses = sum(exp.amount for exp in expenses)
    category_totals = {}
    
    for expense in expenses:
        if expense.category not in category_totals:
            category_totals[expense.category] = 0
        category_totals[expense.category] += expense.amount
    
    # Get expenses by month
    monthly_expenses = {}
    for expense in expenses:
        month_key = expense.date.strftime('%Y-%m')
        if month_key not in monthly_expenses:
            monthly_expenses[month_key] = 0
        monthly_expenses[month_key] += expense.amount
    
    # Get today's expenses
    today = date.today()
    today_expenses = sum(exp.amount for exp in expenses if exp.date == today)
    
    # Get this month's expenses
    this_month = today.strftime('%Y-%m')
    this_month_expenses = monthly_expenses.get(this_month, 0)
    
    return jsonify({
        'total_expenses': total_expenses,
        'category_totals': category_totals,
        'monthly_expenses': monthly_expenses,
        'today_expenses': today_expenses,
        'this_month_expenses': this_month_expenses,
        'total_count': len(expenses)
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    print("\n" + "="*60)
    print("Simple Expense Tracker - Server Starting")
    print("="*60)
    print("\n✓ Database initialized")
    print("✓ Server is starting...")
    print("\n" + "-"*60)
    print("Application is available at:")
    print("  → http://localhost:5000")
    print("  → http://127.0.0.1:5000")
    print("-"*60)
    print("\nPress CTRL+C to stop the server\n")
    
    try:
        app.run(debug=True, host='127.0.0.1', port=5000)
    except OSError as e:
        if "Address already in use" in str(e) or "WinError 10048" in str(e):
            print("\n" + "!"*60)
            print("ERROR: Port 5000 is already in use!")
            print("!"*60)
            print("\nTry one of these solutions:")
            print("1. Close any other Flask applications")
            print("2. Restart your computer")
            print("3. Use a different port by modifying app.py")
            print("\nTo use port 5001 instead, change the last line to:")
            print("  app.run(debug=True, host='127.0.0.1', port=5001)")
        else:
            print(f"\nERROR: {e}")

