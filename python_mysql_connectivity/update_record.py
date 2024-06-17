import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
    database = 'cnp'
)

db_cursor = mydb.cursor()

update_query = "update emp set roll=%s where name=%s"

set_value=(45,'Nirav')

db_cursor.execute(update_query,set_value)
mydb.commit()
print(db_cursor.rowcount,"Data Updated")