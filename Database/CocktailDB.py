#12.42.205.8
import mysql.connector
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] ='remotemysql.com'
app.config['MYSQL_USER'] ='GQ7oHUjvYc'
app.config['MYSQL_PASSWORD'] ='hpLN89qQdb'
app.config['MYSQL_DB'] ='GQ7oHUjvYc'

mysql = MySQL(app)

#conn = mysql.connector.connect(user='root', password='Matter1332*', host='127.0.0.1', database='cocktail')
#conn = mysql.connector.connect(user='GQ7oHUjvYc', password='hpLN89qQdb', host='remotemysql.com', database='GQ7oHUjvYc')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        #fetch form data
        userDetails = request.form
        cockName = userDetails['cocktail']
        cockIngredient = userDetails['ingredient']
        # Creating a cursor object using the cursor() method
        cursor = mysql.connection.cursor()

        # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            "INSERT INTO cocktails(cocktailName,ingredients)"
            "VALUES(%s, %s)"
        )
        data_input = (cockName, cockIngredient)
        cursor.execute(insert_stmt, data_input)
        mysql.connection.commit()
        # Closing the connection
        cursor.close()
        #return 'success'
        return redirect('/cocktails')
    return render_template('index.html')


@app.route('/cocktails')
def cocktails():
    # Creating a cursor object using the cursor() method
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cocktails")
    userDetails = cursor.fetchall()
    return render_template('cocktails.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
