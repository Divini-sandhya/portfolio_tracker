import React, { useState } from 'react';

function EditStock({ stock, onSave }) {
  const [updatedStock, setUpdatedStock] = useState(stock);

  const handleChange = (e) => {
    setUpdatedStock({ ...updatedStock, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    onSave(updatedStock);
  };

  return (
    <div>
      <input name="name" value={updatedStock.name} onChange={handleChange} />
      <input name="ticker" value={updatedStock.ticker} onChange={handleChange} />
      <input name="quantity" value={updatedStock.quantity} onChange={handleChange} />
      <input name="buyPrice" value={updatedStock.buyPrice} onChange={handleChange} />
      <input name="currentPrice" value={updatedStock.currentPrice} onChange={handleChange} />
      <button onClick={handleSave}>Save</button>
    </div>
  );
}

export default EditStock;