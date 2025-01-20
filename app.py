import yfinance as yf
import sqlite3
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def get_stocks_from_database():
    # Connect to the SQLite database
    connection = sqlite3.connect('portfolio.db')
    cursor = connection.cursor()

    # Fetch all stock records from the database
    cursor.execute("SELECT * FROM stocks")
    stocks = cursor.fetchall()

    # Close the connection
    connection.close()

    return stocks

@app.route('/')
def home():
    stocks = get_stocks_from_database()  # Fetch stocks from the database
    return {'stocks': stocks}  # Return the stocks as a response
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
    app.run(host="0.0.0.0",
port=5005)    