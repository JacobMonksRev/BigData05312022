import mysql.connector

mydb = mysql.connector.connect(
    user = "root",
    password = "password",
    host = "localhost",
    database = "demo2"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO example VALUES (1, 'Jacob')")
mydb.commit()   # Use this when you make Insert, Update, or Delete statements
# documentation for mysql connector/python: https://dev.mysql.com/doc/connector-python/en/