import sqlite3

print("Connecting to database...")
connection = sqlite3.connect('portfolio.db')
cursor = connection.cursor()
print("Connected to database.")

print("Creating table if it doesn't exist...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
''')
print("Table created (or already exists).")

print("Inserting sample data...")
cursor.execute("INSERT OR IGNORE INTO stocks (name, price) VALUES ('AAPL', 150.75)")
cursor.execute("INSERT OR IGNORE INTO stocks (name, price) VALUES ('GOOGL', 2880.50)")
cursor.execute("INSERT OR IGNORE INTO stocks (name, price) VALUES ('MSFT', 299.99)")
print("Sample data inserted.")

connection.commit()
connection.close()
print("Database setup completed.")