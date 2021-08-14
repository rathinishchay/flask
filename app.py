#!/usr/bin/env python3

#set FLASK_APP=app.py
from flask import Flask ,render_template

app= Flask(__name__)
print(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/inventory')
def inventory_page():
    items = [
        {'id': 1, 'list_items': 'Step Ladder', 'issue_date': '11-04-2021', 'received_date':'15-04-2021','price':110},
        {'id': 2, 'list_items': 'Water Container', 'issue_date': '13-04-2021', 'received_date':'14-04-2021','price':20},
        {'id': 3, 'list_items': 'Mandap', 'issue_date': '10-04-2021', 'received_date':'16-04-2021','price':1000}
    ]
    return render_template('inventory.html',items=items)

if __name__ == "__main__":
    app.run(debug=True)


