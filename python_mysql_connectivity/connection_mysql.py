import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
)
print(mydb)