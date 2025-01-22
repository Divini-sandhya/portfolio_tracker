import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('portfolio.db')
cursor = connection.cursor()

# Create the 'stocks' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Insert sample data (optional)
cursor.execute("INSERT INTO stocks (name, price) VALUES ('AAPL', 150.75)")
cursor.execute("INSERT INTO stocks (name, price) VALUES ('GOOGL', 2800.50)")
cursor.execute("INSERT INTO stocks (name, price) VALUES ('MSFT', 299.99)")

# Commit changes and close connection
connection.commit()
connection.close()
print("Database and table initialized successfully.")