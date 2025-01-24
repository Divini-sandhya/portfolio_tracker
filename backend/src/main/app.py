import yfinance as yf
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_stocks_from_database():
    
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect('portfolio.db')  # Ensure the path is correct
        cursor = connection.cursor()

        # Fetch all stocks from the 'stocks' table
        cursor.execute("SELECT * FROM stocks")
        rows = cursor.fetchall()
        print(rows)

        '''# Convert rows to list of dictionaries
        stocks = []
        for row in rows:
            stock = {
                "id": row[0],
                "name": row[1],
                "price": row[2]
            }
            stocks.append(stock)

        # Close the connection'''
        connection.close()

        return stocks
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


@app.route('/')
def home():
    try:
        # Fetch stocks from the database
        stocks = get_stocks_from_database()

        # Return the stocks as JSON
        return jsonify({"stocks": stocks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/update_prices')
def update_prices():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    # Fetch all stocks
    cursor.execute("SELECT id, ticker FROM stocks")
    stocks = cursor.fetchall()

    for stock in stocks:
        stock_id, ticker = stock
        price = get_stock_price(ticker)
        print(f"Updating {ticker} with price {price}")
        if price:
             cursor.execute("UPDATE stocks SET current_price = ? WHERE id = ?", (price, stock_id))
    
    conn.commit()
    conn.close()
    return redirect('/')
@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        name = request.form['name']
        ticker = request.form['ticker']
        quantity = request.form['quantity']
        buy_price = request.form['buy_price']

        if name and ticker and quantity and buy_price:
            conn = sqlite3.connect('portfolio.db')
            cursor = conn.cursor()

            # Insert the new stock into the database
            cursor.execute("INSERT INTO stocks (name, ticker, quantity, buy_price) VALUES (?, ?, ?, ?)",
                           (name, ticker, quantity, buy_price))
            conn.commit()
            conn.close()

            return redirect('/')

    return render_template('add_stock.html')

if __name__ == "__main__":
    app.run(port=5005)    