#12.42.205.8

from flask import Flask, render_template, request, redirect, jsonify
from flaskext.mysql import MySQL
import pymysql


app = Flask(__name__)
app.config['MYSQL_HOST'] ='35.184.2.237'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='Database435'
app.config['MYSQL_DB'] ='Recipes'

mysql = MySQL(app)
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

@app.route("/livesearch", methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "SELECT RecipeID from Cocktail where RecipeID LIKE '{}%' order by RecipeID".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)



@app.route('/cocktails')
def cocktails():
    # Creating a cursor object using the cursor() method
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Cocktail")
    userDetails = cursor.fetchall()
    return render_template('cocktails.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
