import sqlite3  # Import the sqlite3 module

# Connect to the database
connection = sqlite3.connect('portfolio.db')  # Use 'backend/portfolio.db' if the database is inside the 'backend' folder
cursor = connection.cursor()

# Check if the 'stocks' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stocks';")
result = cursor.fetchone()

if result:
    print("Table 'stocks' exists.")
else:
    print("Table 'stocks' does not exist.")

connection.close()