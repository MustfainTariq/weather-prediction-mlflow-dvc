import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Notice the update here
import AuthForm from "./components/AuthForm";
import SignUpAuth from "./components/SignUpAuth";
import "./App.css";
import WeatherPrediction from "./components/WeatherPrediction";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/sign-up" element={<SignUpAuth />} />
          <Route path="/" element={<AuthForm />} />
          <Route path="/prediction" element={<WeatherPrediction />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
