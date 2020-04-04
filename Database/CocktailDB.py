import mysql.connector

#establishing DB Connection (locally)
connection = mysql.connector.connect(user = 'root', password = 'Database435', host = '127.0.0.1', database = 'Cocktail')

if connection.is_connected():
    print("Connection Established")

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Closing Connection
connection.close()

