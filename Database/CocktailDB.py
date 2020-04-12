#12.42.205.8
import mysql.connector
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import pymysql

# GCP SQL connection
con = pymysql.connect(host = '35.184.2.237', user = 'root', password = 'Database435', db = 'Recipes')

if con.open:
    print("Open")

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))

print(cur.execute('describe Cocktail'))

app = Flask(__name__)
app.config['MYSQL_HOST'] ='35.184.2.237'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='Database435'
app.config['MYSQL_DB'] ='Recipes'

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
            "INSERT INTO Cocktail(RecipeID,RecipeName)"
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
    cursor.execute("SELECT * FROM Cocktail")
    userDetails = cursor.fetchall()
    return render_template('cocktails.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
