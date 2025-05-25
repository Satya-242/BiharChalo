# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Customer:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, name, acc_no, balance=0):
        self.customers[acc_no] = Customer(name, acc_no, balance)

    def get_customer(self, acc_no):
        return self.customers.get(acc_no)

class BankSystem:
    def __init__(self):
        self.banks = {}

    def create_bank(self, name):
        self.banks[name] = Bank(name)

    def get_bank(self, name):
        return self.banks.get(name)

    def transfer(self, from_bank, from_acc, to_bank, to_acc, amount):
        sender = self.banks[from_bank].get_customer(from_acc)
        receiver = self.banks[to_bank].get_customer(to_acc)

        if sender and receiver and sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            return True
        return False

system = BankSystem()

@app.route('/')
def home():
    return render_template('index.html', banks=system.banks)

@app.route('/create_bank', methods=['GET', 'POST'])
def create_bank():
    if request.method == 'POST':
        name = request.form['name']
        system.create_bank(name)
        return redirect(url_for('home'))
    return render_template('create_bank.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        bank = request.form['bank']
        name = request.form['name']
        acc = request.form['acc']
        bal = float(request.form['balance'])
        system.get_bank(bank).add_customer(name, acc, bal)
        return redirect(url_for('home'))
    return render_template('add_customer.html', banks=system.banks)

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    msg = ''
    if request.method == 'POST':
        from_bank = request.form['from_bank']
        from_acc = request.form['from_acc']
        to_bank = request.form['to_bank']
        to_acc = request.form['to_acc']
        amount = float(request.form['amount'])

        if system.transfer(from_bank, from_acc, to_bank, to_acc, amount):
            msg = 'Transfer Successful'
        else:
            msg = 'Transfer Failed (Check details or balance)'
    return render_template('transfer.html', banks=system.banks, message=msg)

@app.route('/balance')
def balance():
    return render_template('balance.html', banks=system.banks)

if __name__ == '__main__':
    app.run(debug=True)
