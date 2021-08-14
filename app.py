#!/usr/bin/env python3

from flask import Flask

app= Flask(__name__)
print(app)

@app.route('/')
def index():
    return "Hello World"
