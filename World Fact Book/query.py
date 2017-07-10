import sqlite3 as sql

conn = sql.connect('factbook.db')
cursor = conn.cursor()

query = 'select name from facts order by population asc limit 10;'

cursor.execute(query)

results = cursor.fetchall()

print(results)