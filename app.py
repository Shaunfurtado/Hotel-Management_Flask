from flask import Flask, render_template, request, session, redirect, flash, url_for
import pymysql
app = Flask(__name__)

app.secret_key = "your_secret_key"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "123456"
app.config['MYSQL_DB'] = "hotel"

mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Dashboard', methods=['GET', 'POST'])
def dashboard():

    return render_template('Dashboard.html')

# Tables


@app.route('/Rooms', methods=['GET', 'POST'])
def Rooms():
    cursor = mysql.cursor()
    cursor.execute("SELECT r.room_number, r.room_type, r.ac, r.wifi, re.check_in_date, re.check_out_date,r.room_price  FROM rooms r, reservations re WHERE r.room_number = re.room_number")
    data = cursor.fetchall()
    cursor.close()
    return render_template('Rooms.html', data=data)


@app.route('/customertable', methods=['GET', 'POST'])
def customertable():
    cursor = mysql.cursor()
    cursor.execute("SELECT re.room_number, re.first_name, re.room_type, re.check_in_date, re.check_out_date, re.num_of_people,re.payment, r.room_price  FROM reservations re,rooms r WHERE re.room_number = r.room_number")
    data = cursor.fetchall()
    cursor.close()
    return render_template('customertable.html', data=data)
# Form Entry


@app.route('/roombook', methods=['GET', 'POST'])
def roombook():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_number = request.form['contact_number']
        address = request.form['address']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        num_of_people = request.form['num_of_people']
        wifi = request.form['wifi']
        ac = request.form['ac']
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO reservations (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac) VALUES (%s, %s, %s,  %s, %s, %s, %s, %s, %s,%s,%s)",
                       (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac))
        mysql.commit()
        cursor.close()
        flash("Your room has been booked successfully", "success")
    return render_template('roombook.html')


@app.route('/addroom', methods=['GET', 'POST'])
def addroom():
    if request.method == 'POST':
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        room_price = request.form['room_price']
        wifi = request.form['wifi']
        ac = request.form['ac']
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO rooms (room_number, room_type, room_price, wifi, ac) VALUES (%s, %s, %s, %s, %s)",
                       (room_number, room_type, room_price, wifi, ac))
        mysql.commit()
        cursor.close()
        flash("Your room has been added successfully", "success")
    return render_template('addroom.html')


if __name__ == '__main__':
    app.run(debug=True)
