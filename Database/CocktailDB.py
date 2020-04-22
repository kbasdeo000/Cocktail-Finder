#12.42.205.8


# This should be connected to the "Get Recipe" button
#select distinct r1.RecipeName, r1.Spirit, r1.SpiritAmount,  r1.Syrup, r1.SyrupAmount,  r1.Juice, r1.JuiceAmount,  r1.Fruit, r1.FruitAmount
#from Ingredients r1
#join UserIngredients u1
#on  r1.Spirit like u1.Ingredient
#or  r1.Syrup like u1.Ingredient
#or  r1.Juice like u1.Ingredient
#or  r1.Fruit like u1.Ingredient;

# This should be connected to the "New Recipe" button
#delete from UserIngredients;

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
        # This should be connected to the "Done" button.
        insert_stmt = (
            "INSERT INTO UserIngredients(UserID,Ingredient)"
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
