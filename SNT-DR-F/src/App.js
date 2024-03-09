import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Demandcreating from "./Pages/Demandcreating";
import Example from "./Pages/Table";
import "./index.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/table" element={<Example />} />
        <Route path="/" element={<Demandcreating />} />
      </Routes>
    </Router>
  );
}

export default App;
