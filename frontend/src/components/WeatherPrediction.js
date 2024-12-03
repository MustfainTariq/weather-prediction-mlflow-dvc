import React, { useState } from "react";
import "./WeatherPrediction.css"; // We'll style it as per your requirement

const WeatherPrediction = () => {
  const [temperature, setTemperature] = useState("");
  const [humidity, setHumidity] = useState("");
  const [windSpeed, setWindSpeed] = useState("");
  const [weatherCondition, setWeatherCondition] = useState("");
  const [date, setDate] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(""); // For showing validation message

  const handleSubmit = () => {
    // Validate the input fields
    if (!temperature || !humidity || !windSpeed || !weatherCondition || !date) {
      setError("Please enter the required fields.");
      setPrediction(null); // Reset prediction if error
    } else {
      setError(""); // Clear error message
      // Simulate a prediction
      setPrediction(`Predicted Temperature: ${Math.random() * 30 + 15}°C`); // Random prediction for demo purposes
    }
  };

  return (
    <div className="container">
      <h1>Weather Prediction</h1>
      <div className="form-container">
        <label>
          Temperature:
          <input
            type="text"
            value={temperature}
            onChange={(e) => setTemperature(e.target.value)}
            placeholder="Enter Temperature"
          />
        </label>
        <label>
          Humidity:
          <input
            type="text"
            value={humidity}
            onChange={(e) => setHumidity(e.target.value)}
            placeholder="Enter Humidity"
          />
        </label>
        <label>
          Wind Speed:
          <input
            type="text"
            value={windSpeed}
            onChange={(e) => setWindSpeed(e.target.value)}
            placeholder="Enter Wind Speed"
          />
        </label>
        <label>
          Weather Condition:
          <input
            type="text"
            value={weatherCondition}
            onChange={(e) => setWeatherCondition(e.target.value)}
            placeholder="Enter Weather Condition"
          />
        </label>
        <label>
          Date:
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
        </label>
        {error && <p className="error-message">{error}</p>}{" "}
        {/* Display error message */}
        <button onClick={handleSubmit}>Predict</button>
        {prediction && <p className="prediction-result">{prediction}</p>}{" "}
        {/* Display prediction */}
      </div>
    </div>
  );
};

export default WeatherPrediction;
