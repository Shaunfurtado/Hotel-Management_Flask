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
def index():
    return render_template('index.html')


@app.route('/Dashboard', methods=['GET', 'POST'])
def dashboard():
    cursor = mysql.cursor()
    cursor.execute(
        "SELECT COUNT(*) AS total_rooms, SUM(CASE WHEN r.room_number NOT IN (SELECT room_number FROM reservations) THEN 1 ELSE 0 END) AS available_rooms, SUM(CASE WHEN r.room_number IN (SELECT room_number FROM reservations) THEN 1 ELSE 0 END) AS reserved_rooms, CAST((SELECT SUM(num_of_people) FROM reservations) AS UNSIGNED) AS total_people FROM rooms r;"
    )
    data = cursor.fetchall()
    cursor.close()
    return render_template('Dashboard.html', data=data)

# Tables


@app.route('/Rooms', methods=['GET', 'POST'])
def Rooms():
    cursor = mysql.cursor()
    cursor.execute(
        "SELECT r.room_number, r.room_type, r.ac, r.wifi, r.room_price FROM rooms r LEFT JOIN reservations re ON r.room_number = re.room_number WHERE re.room_number IS NULL")
    data = cursor.fetchall()
    cursor.execute(
        "SELECT r.room_number, r.room_type, r.ac, r.wifi, re.check_in_date, re.check_out_date,re.num_of_people, r.room_price FROM rooms r, reservations re WHERE r.room_number = re.room_number")
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('Rooms.html', data=data, data1=data1)


@app.route('/customertable', methods=['GET', 'POST'])
def customertable():
    cursor = mysql.cursor()
    cursor.execute("SELECT re.room_number, re.first_name, re.room_type, re.check_in_date, re.check_out_date, re.num_of_people,re.payment, r.room_price  FROM reservations re,rooms r WHERE re.room_number = r.room_number")
    data = cursor.fetchall()
    cursor.close()
    return render_template('customertable.html', data=data)

# Form Entry


# @app.route('/roombook', methods=['GET', 'POST'])
# def roombook():
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         contact_number = request.form['contact_number']
#         address = request.form['address']
#         check_in_date = request.form['check_in_date']
#         check_out_date = request.form['check_out_date']
#         room_number = request.form['room_number']
#         room_type = request.form['room_type']
#         num_of_people = request.form['num_of_people']
#         wifi = request.form['wifi']
#         ac = request.form['ac']
#         payment = request.form['payment']
#         cursor = mysql.cursor()
#         cursor.execute("INSERT INTO reservations (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac,payment) VALUES (%s,%s, %s, %s,  %s, %s, %s, %s, %s, %s,%s,%s)",
#                        (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac, payment))
#         mysql.commit()
#         cursor.close()
#         flash("Your room has been booked successfully", "success")
#     return render_template('roombook.html')

@app.route('/roombook', methods=['GET', 'POST'])
def roombook():
    if request.method == 'POST':
        # ... (Your existing code to retrieve form data)
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
        payment = request.form['payment']
        # Check if the room_number exists in the rooms table
        cursor = mysql.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM rooms WHERE room_number = %s", (room_number,))
        room_exists = cursor.fetchone()[0]

        if room_exists:
            cursor.execute("INSERT INTO reservations (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac, payment) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, contact_number, address, check_in_date, check_out_date, room_number, room_type, num_of_people, wifi, ac, payment))
            mysql.commit()
            cursor.close()
            flash("Your room has been booked successfully", "success")
        else:
            flash("Invalid room number. Please enter a valid room number.", "error")

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
