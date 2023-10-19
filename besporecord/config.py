#  here we are going to create the connection with mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "newuser",
    password = "newuser@123"
)

# prepare a cursor object
mycursor = mydb.cursor()

# create or use a database
mycursor.execute("use besporecord")

print("database connected")
mydb.close()
print("connection closed")