#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect, request
from db import User, session


app = Flask(__name__)

@app.route('/')
def hello():
    """Say hello"""
    return "Hello UBagri!"

@app.route('/ubagri')
def ubagri():
    """Render landing page"""
    return render_template('index.html')


@app.route('/weather')
def weather():
    """Weather Info"""
    return render_template('weather.html')

@app.route('/account', methods=('GET', 'POST'))
def account():
    """New account"""
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        user = User(firstname=firstname, lastname=lastname, email=email, phone_number=phonenumber)
        session.add(user)
        session.commit()
        return redirect(url_for('ubagri'))
    
    return render_template('account.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
