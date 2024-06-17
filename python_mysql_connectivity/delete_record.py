import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
    database = 'cnp'
)

db_cursor = mydb.cursor()

delete_query = "delete from emp where roll=%s"

set_value=(45,)

db_cursor.execute(delete_query,set_value)
mydb.commit()
print(db_cursor.rowcount,"Data deleted")