#!/usr/bin/python3
"""app to run my application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """Say hello"""
    return "Hello UBagri!"

@app.route('/ubagri')
def ubagri():
    """Render landing page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)