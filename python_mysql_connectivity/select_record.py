import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
    database = 'cnp'
)

db_cursor = mydb.cursor()

db_cursor.execute("select * from emp")

for db_data in db_cursor.fetchall():

    print(db_data) 