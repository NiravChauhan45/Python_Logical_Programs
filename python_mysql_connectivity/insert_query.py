import mysql.connector as mycnn

mydb = mycnn.connect(
    host='localhost',
    user='root',
    password='2004',
    database = 'cnp'
)

db_cursor = mydb.cursor()
insert_query=("insert into emp(Roll,name) values(%s,%s)")
# insert_value=(20,"Nirav")
insert_values = [(21,'kalpo'),(22,'indra'),(23,'kiran')]
db_cursor.executemany(insert_query,insert_values)
mydb.commit()
print(db_cursor) 