import yfinance as yf
import sqlite3
import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
# Replace with your actual API key
API_KEY = "your_alpha_vantage_api_key"
BASE_URL = "https://www.alphavantage.co/query"

def get_stocks_from_database():
    # Connect to the SQLite database
    connection = sqlite3.connect('portfolio.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Fetch all stock records from the database
    cursor.execute("SELECT * FROM stocks")
    stocks = [dict(row) for row in cursor.fetchall()]

    # Close the connection
    connection.close()

    return stocks

@app.route('/')
def home():
    stocks = get_stocks_from_database()  # Fetch stocks from the database
    return render_template('index.html',stocks=stocks)  # Return the stocks as a response
@app.route('/update_prices', methods=['POST'])
def update_prices():
    try:
        conn = sqlite3.connect('portfolio.db')
        cursor = conn.cursor()

        # Fetch all stock names from the database
        cursor.execute("SELECT id, name FROM stocks")
        stocks = cursor.fetchall()

        for stock in stocks:
            stock_id, stock_name = stock

            # Fetch the real-time price from Alpha Vantage
            params = {
                "function": "TIME_SERIES_INTRADAY",
                "symbol": stock_name,
                "interval": "1min",
                "apikey": API_KEY
            }
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            # Extract the latest price
            try:
                latest_time = list(data["Time Series (1min)"].keys())[0]
                latest_price = float(data["Time Series (1min)"][latest_time]["1. open"])

                # Update the stock price in the database
                cursor.execute(
                    "UPDATE stocks SET current_price = ? WHERE id = ?",
                    (latest_price, stock_id)
                )
            except KeyError:
                print(f"Error fetching data for {stock_name}")

        conn.commit()
        conn.close()
        return render_template("index.html", message="Stock prices updated successfully!")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500
    except Exception as e:
        return f"An error occurred: {e}", 500

       

@app.route('/add', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        quantity = request.form['quantity']
        current_price = request.form['current_price']
        
        # Insert into the database
        try:
            conn = sqlite3.connect('portfolio.db')  # Ensure correct path to database
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stocks (name, quantity, current_price) VALUES (?, ?, ?)",
                           (name, quantity, current_price))
            conn.commit()
            conn.close()
            return redirect('/')  # Redirect to the homepage after adding stock
        except Exception as e:
            return f"Error: {e}"
    return render_template('add_stock.html')


if __name__ == "__main__":
    app.run(debug=True)    