import React from 'react';

function StockTable({ stocks, onEdit }) {
  return (
    <table border="1" style={{ width: "100%", textAlign: "left" }}>
      <thead>
        <tr>
          <th>Name</th>
          <th>Ticker</th>
          <th>Quantity</th>
          <th>Buy Price</th>
          <th>Current Price</th>
          <th>Total Value</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {stocks.map((stock, index) => (
          <tr key={index}>
            <td>{stock.name}</td>
            <td>{stock.ticker}</td>
            <td>{stock.quantity}</td>
            <td>{stock.buyPrice}</td>
            <td>{stock.currentPrice}</td>
            <td>{(stock.quantity * stock.currentPrice).toFixed(2)}</td>
            <td>
              <button onClick={() => onEdit(index)}>Update</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default StockTable;