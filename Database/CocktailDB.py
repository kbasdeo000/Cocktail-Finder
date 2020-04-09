import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user = 'ml1774', password = 'ml1774123', host = 'localhost', database = 'ml1774')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    print("Connection Established")
    cnx.close()

#pip install --user mysql-connector-python