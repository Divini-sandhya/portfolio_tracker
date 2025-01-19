import React, { useState } from 'react';
import AddStock from './components/AddStock';
import StockTable from './components/StockTable';
import EditStock from './components/EditStock';

function App() {
  const [stocks, setStocks] = useState([]);
  const [editingIndex, setEditingIndex] = useState(null);

  const handleAdd = (stock) => {
    setStocks([...stocks, stock]);
  };

  const handleEdit = (index) => {
    setEditingIndex(index);
  };

  const handleSave = (updatedStock) => {
    const newStocks = [...stocks];
    newStocks[editingIndex] = updatedStock;
    setStocks(newStocks);
    setEditingIndex(null);
  };

  return (
    <div>
      <h1>Portfolio Tracker</h1>
      <AddStock onAdd={handleAdd} />
      {editingIndex !== null ? (
        <EditStock stock={stocks[editingIndex]} onSave={handleSave} />
      ) : (
        <StockTable stocks={stocks} onEdit={handleEdit} />
      )}
    </div>
  );
}

export default App;