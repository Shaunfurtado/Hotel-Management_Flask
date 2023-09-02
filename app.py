from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="123456",
#     database="hotel"
# )
# my_cursor = mydb.cursor()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class reservations(db.Model):
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room_number = db.Column(db.Integer, nullable=False, primary_key=True)
    room_type = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    room_price = db.Column(db.Integer, nullable=False)
    wifi = db.Column(db.String(20), nullable=False)
    ac = db.Column(db.String(20), nullable=False)
    # date = db.Column(db.Datetime, default=datetime.utcnow)

    def __init__(self, first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, desc, room_price, wifi, ac):
        self.first_name = first_name
        self.last_name = last_name
        self.contact_number = contact_number
        self.address = address
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_number = room_number
        self.room_type = room_type
        self.desc = desc
        self.room_price = room_price
        self.wifi = wifi
        self.ac = ac


class rooms(db.Model):
    room_number = db.Column(db.Integer, nullable=False, primary_key=True)
    room_type = db.Column(db.String(20), nullable=False)
    room_price = db.Column(db.Integer, nullable=False)
    wifi = db.Column(db.String(20), nullable=False)
    ac = db.Column(db.String(20), nullable=False)


def __init__(self, room_number, room_type, room_price, wifi, ac):
    self.room_number = room_number
    self.room_type = room_type
    self.room_price = room_price
    self.wifi = wifi
    self.ac = ac


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('Dashboard.html')


@app.route('/Rooms', methods=['GET', 'POST'])
def rooms():
    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        room_price = request.form.get('room_price')
        wifi = request.form.get('wifi')
        ac = request.form.get('ac')
        entry = rooms(room_number=room_number, room_type=room_type,
                      room_price=room_price, wifi=wifi, ac=ac)
        db.session.add(entry)
        db.session.commit()
        flash("Your room has been booked successfully", "success")
    return render_template('Rooms.html')


@app.route('/roombook', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        contact_number = request.form.get('contact_number')
        address = request.form.get('address')
        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        desc = request.form.get('desc')
        room_price = request.form.get('room_price')
        wifi = request.form.get('wifi')
        ac = request.form.get('ac')
        entry = reservations(first_name=first_name, last_name=last_name, contact_number=contact_number, address=address, check_in_date=check_in_date,
                             check_out_date=check_out_date, room_number=room_number, room_type=room_type, desc=desc, room_price=room_price, wifi=wifi, ac=ac)
        db.session.add(entry)
        db.session.commit()
        flash("Your room has been booked successfully", "success")
    return render_template('roombook.html')


@app.route('/customertable', methods=['GET', 'POST'])
def customertable():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        contact_number = request.form.get('contact_number')
        address = request.form.get('address')
        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        desc = request.form.get('desc')
        room_price = request.form.get('room_price')
        wifi = request.form.get('wifi')
        ac = request.form.get('ac')
        entry = reservations(first_name=first_name, last_name=last_name, contact_number=contact_number, address=address, check_in_date=check_in_date,
                             check_out_date=check_out_date, room_number=room_number, room_type=room_type, desc=desc, room_price=room_price, wifi=wifi, ac=ac)
        db.session.add(entry)
        db.session.commit()
        flash("Your room has been booked successfully", "success")
    return render_template('customertable.html')


@app.route('/addroom', methods=['GET', 'POST'])
def addroom():
    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        room_price = request.form.get('room_price')
        wifi = request.form.get('wifi')
        ac = request.form.get('ac')
        entry = rooms(room_number=room_number, room_type=room_type,
                      room_price=room_price, wifi=wifi, ac=ac)
        db.session.add(entry)
        db.session.commit()
        flash("Your room has been booked successfully", "success")
    return render_template('addroom.html')


if __name__ == '__main__':
    app.run(debug=True)
