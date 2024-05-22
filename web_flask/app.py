#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://eric:1016@localhost/ubagri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

db = SQLAlchemy(app)

class User(db.Model):
    """User table"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    

    def __repr__(self):
        return f"User('{self.firstname}' '{self.lastname}' '{self.phone_number}')"


class Address(db.Model):
    """Address table"""
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20), nullable=False)
    province = db.Column(db.String(20), nullable=False)
    district = db.Column(db.String(20), nullable=False)
    sector = db.Column(db.String(20), nullable=False)
    cell = db.Column(db.String(20), nullable=False)
    village = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Address('{self.district}' - '{self.country}')"

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
