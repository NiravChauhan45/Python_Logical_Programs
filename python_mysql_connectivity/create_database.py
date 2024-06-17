import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
)

db_cursor = mydb.cursor()
db_cursor.execute("create database CNP")
print(db_cursor)