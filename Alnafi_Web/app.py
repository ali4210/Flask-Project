from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from datetime import datetime
import time as t


app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.0.150'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8601'
app.config['MYSQL_DB'] = 'alnafi'
mysql = MySQL(app)

myhome = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@HOME PAGE!!!!!!!!!!!!!!!!!!!!!!!!!!!"
mycontact = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!CONTACT US PAGE!!!!!!!!!!!!!!!!!!!!!!!!"

@app.get("/")
def get_home():
    return  myhome

@app.get("/contacts")
def get_contact():
    return mycontact

@app.route("/trainer")
def trainer():
    return render_template('trainer_details.html')

@app.route("/trainer_create",methods=['GET','POST'])
def trainer_create():
    if request.method == "POST":
        fname_data = request.form['fname']
        lname_data = request.form['lname']
        desig_data = request.form['desig']
        username_data = request.form['username']
        password_data = request.form['password']
        #cdate_data = request.form['cdate']
        sql = "INSERT INTO trainer_details (fname,lname,desig,username,password) VALUES (%s,%s,%s,%s,%s)"
        val = (fname_data, lname_data,desig_data,username_data,password_data)

        #connection
        cursor = mysql.connection.cursor()

        #execution sql querry
        cursor.execute(sql,val)

        #commit
        mysql.connection.commit()

        cursor.close()
        return render_template('trainer_details.html')
        return "DONE , Data has been stored successfully!!!!!!"


# === app.py (Rectified trainer_data function) ===

@app.route("/trainer_data", methods=['GET', 'POST'])
def trainer_data():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM trainer_details"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    # FIX 1: Change output_data=rows to trainers=rows
    return render_template('display_trainer.html', trainers=rows)





if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0" ,port=9000 )
    app.run(debug=True, host="0.0.0.0")