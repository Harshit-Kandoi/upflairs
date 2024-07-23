import sqlite3

connection=sqlite3.connect('insurance.db')

query = """
create table project
(age integer,gender integer,bmi integer,children integer, region varchar(5),smoker integer,health integer,predicton varchar(10))"""


cur = connection.cursor()     # cursor sql
cur.execute(query)
print("your database and your table is created")
cur.close()
connection.close()