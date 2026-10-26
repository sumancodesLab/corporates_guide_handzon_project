
import React, { useState } from "react";
import "./App.css";

function App() {
  const [color, setColor] = useState("white");

  return (
    <div className="container">
      <h2>Color Changer App</h2>

      <div
        className="color-box"
        style={{ backgroundColor: color }}
      >
        <h3>{color.toUpperCase()}</h3>
      </div>

      <div className="buttons">
        <button
          style={{ backgroundColor: "red" }}
          onClick={() => setColor("red")}
        >
          Red
        </button>

        <button
          style={{ backgroundColor: "green" }}
          onClick={() => setColor("green")}
        >
          Green
        </button>

        <button
          style={{ backgroundColor: "blue" }}
          onClick={() => setColor("blue")}
        >
          Blue
        </button>
      </div>
    </div>
  );
}

export default App;
