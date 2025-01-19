import React, { useState } from 'react';
import './AddStock.css'; // Import the CSS file for styling

function AddStock({ onAdd }) {
  const [stock, setStock] = useState({
    name: '',
    ticker: '',
    quantity: '',
    buyPrice: '',
    currentPrice: '',
  });

  const handleChange = (e) => {
    setStock({ ...stock, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd(stock);
    setStock({ name: '', ticker: '', quantity: '', buyPrice: '', currentPrice: '' });
  };

  return (
    <form className="add-stock-form" onSubmit={handleSubmit}>
      <div className="form-row">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={stock.name}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-row">
        <label htmlFor="ticker">Ticker</label>
        <input
          type="text"
          id="ticker"
          name="ticker"
          value={stock.ticker}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-row">
        <label htmlFor="quantity">Quantity</label>
        <input
          type="number"
          id="quantity"
          name="quantity"
          value={stock.quantity}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-row">
        <label htmlFor="buyPrice">Buy Price</label>
        <input
          type="number"
          id="buyPrice"
          name="buyPrice"
          value={stock.buyPrice}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-row">
        <label htmlFor="currentPrice">Current Price</label>
        <input
          type="number"
          id="currentPrice"
          name="currentPrice"
          value={stock.currentPrice}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit" className="submit-button">Add Stock</button>
    </form>
  );
}

export default AddStock;