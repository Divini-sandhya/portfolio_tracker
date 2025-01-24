# -- coding: utf-8 --

import sqlite3

print("Starting database setup...")

# Connect to the database (will create the file if it doesn't exist)
connection = sqlite3.connect('portfolio.db')
cursor = connection.cursor()

# Create the 'stocks' table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

connection.commit()
connection.close()

print("Database initialized successfully.")