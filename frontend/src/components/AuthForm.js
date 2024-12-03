import "./AuthForm.css";
import { Link, useNavigate } from "react-router-dom";
import React, { useState } from "react";

const AuthForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validation or signup logic here (e.g., send to API)
    const credentials = { email, password };

    try {
      const response = await fetch("http://localhost:5000/auth/signin", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      });

      if (response.ok) {
        // On successful login, navigate to the weather prediction page
        const data = await response.json();
        localStorage.setItem("access_token", data.access_token); // store the token
        navigate("/prediction"); // Navigate to the prediction page
      } else {
        // Handle error, display error message
        const errorData = await response.json();
        setError(errorData.message || "An error occurred");
      }
    } catch (err) {
      setError("Network error, please try again.");
      console.log(err);
    }
  };

  return (
    <div className="container">
      {/* Sign In Form */}
      <div className="form-container sign-in-container">
        <h1>Sign In to Weather Pred.</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)} // Bind input to state
          />
          <input
            type="password"
            placeholder="Password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)} // Bind input to state
          />
          <button type="submit">Sign In</button>
          {error && <p className="error">{error}</p>}{" "}
          {/* Display error message if any */}
          <p className="signup-link">
            Don't have an account? <Link to="/sign-up">Sign Up</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default AuthForm;
