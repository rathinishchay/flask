#!/usr/bin/env python3

#set FLASK_APP=app.py
from flask import Flask ,render_template

app= Flask(__name__)
print(app)

@app.route('/')
def index():
    return render_template('home.html')


