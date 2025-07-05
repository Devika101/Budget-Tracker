from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = 'budget_data.csv'

@app.route('/')
def index():
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            data = list(reader)
    return render_template('index.html', entries=data)

@app.route('/add', methods=['POST'])
def add():
    income = float(request.form['income'])
    expenses = float(request.form['expenses'])
    remaining = income - expenses

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(CSV_FILE).st_size == 0:
            writer.writerow(["Income", "Expenses", "Remaining"])
        writer.writerow([income, expenses, remaining])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
