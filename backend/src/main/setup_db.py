import sqlite3

conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

cursor.execute("SELECT id, ticker, current_price FROM stocks")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()