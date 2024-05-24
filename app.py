from flask import Flask, request, jsonify
from models import db, Expense, Revenue, Inventory, Payroll
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hpi_financials.db'
db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(category=data['category'], amount=data['amount'], date=datetime.strptime(data['date'], '%Y-%m-%d'))
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully!'})

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{'category': e.category, 'amount': e.amount, 'date': e.date.strftime('%Y-%m-%d')} for e in expenses])

@app.route('/revenues', methods=['POST'])
def add_revenue():
    data = request.get_json()
    new_revenue = Revenue(source=data['source'], amount=data['amount'], date=datetime.strptime(data['date'], '%Y-%m-%d'))
    db.session.add(new_revenue)
    db.session.commit()
    return jsonify({'message': 'Revenue added successfully!'})

@app.route('/revenues', methods=['GET'])
def get_revenues():
    revenues = Revenue.query.all()
    return jsonify([{'source': r.source, 'amount': r.amount, 'date': r.date.strftime('%Y-%m-%d')} for r in revenues])

@app.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()
    new_inventory = Inventory(item_name=data['item_name'], quantity=data['quantity'], last_updated=datetime.strptime(data['last_updated'], '%Y-%m-%d'))
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({'message': 'Inventory added successfully!'})

@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = Inventory.query.all()
    return jsonify([{'item_name': i.item_name, 'quantity': i.quantity, 'last_updated': i.last_updated.strftime('%Y-%m-%d')} for i in inventory])

@app.route('/payroll', methods=['POST'])
def add_payroll():
    data = request.get_json()
    new_payroll = Payroll(employee_name=data['employee_name'], salary=data['salary'], pay_date=datetime.strptime(data['pay_date'], '%Y-%m-%d'))
    db.session.add(new_payroll)
    db.session.commit()
    return jsonify({'message': 'Payroll added successfully!'})

@app.route('/payroll', methods=['GET'])
def get_payroll():
    payroll = Payroll.query.all()
    return jsonify([{'employee_name': p.employee_name, 'salary': p.salary, 'pay_date': p.pay_date.strftime('%Y-%m-%d')} for p in payroll])

if __name__ == '__main__':
    app.run(debug=True)
