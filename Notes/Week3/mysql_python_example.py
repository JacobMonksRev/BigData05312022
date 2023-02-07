import mysql.connector

mydb = mysql.connector.connect(
    user = "root",
    password = "password",
    host = "localhost",
    database = "demo2"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")
for item in mycursor:
    print(item)
mycursor.execute("CREATE TABLE myTable (id int, name varchar(255))")
mydb.commit()   # Use this when you make Insert, Update, or Delete statements
# documentation for mysql connector/python: https://dev.mysql.com/doc/connector-python/en/