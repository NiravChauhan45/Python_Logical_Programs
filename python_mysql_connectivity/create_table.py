import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
    database = 'cnp'
)

db_cursor = mydb.cursor()
db_cursor.execute("create table emp(Roll int,name varchar(20))")
print(db_cursor) 