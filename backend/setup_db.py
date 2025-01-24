import sqlite3

def setup_db():
    # Connect to the SQLite database
    conn = sqlite3.connect('path/to/your/database.db')  # Use your actual database path
    cursor = conn.cursor()
    
    # Create the 'stocks' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            symbol TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call this function when the app starts
@app.before_first_request
def initialize():
    setup_db()