# module
import cx_Oracle

# establish connection
connection = cx_Oracle.connect(
    user="USER", 
    password="PASS",
    dsn="HOST:PORT"
)

# create cursor
cursor = connection.cursor()
qry = '''SELECT TOP (1000) * FROM view_apt'''
cursor.execute(qry)

# fetch all the rows 
res = cursor.fetchall()
for row in res:
    print(row)