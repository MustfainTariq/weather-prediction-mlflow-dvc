import "./AuthForm.css";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

const SignUpAuth = () => {
  const [fullname, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Form validation (e.g., check for empty fields)
    if (!fullname || !email || !password) {
      setError("All fields are required");
      return;
    }

    // Prepare credentials to send to the backend
    const credentials = { fullname, email, password };

    try {
      const response = await fetch("http://localhost:5000/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      });

      if (response.ok) {
        // On successful signup, navigate to the weather prediction page
        const data = await response.json();
        localStorage.setItem("access_token", data.access_token); // Store the token
        navigate("/prediction"); // Navigate to the prediction page
      } else {
        // Handle error from backend (e.g., user already exists)
        const errorData = await response.json();
        console.log("Error data:", errorData);
        setError(errorData.message || "An error occurred");
      }
    } catch (err) {
      setError("Network error, please try again.");
      console.log(err);
    }
  };

  return (
    <div className="container">
      {/* Sign Up Form */}
      <div className="form-container sign-up-container">
        <h1>Sign Up</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Full Name"
            value={fullname}
            onChange={(e) => setFullName(e.target.value)}
            required
          />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Sign Up</button>
          {error && <p className="error">{error}</p>}{" "}
          {/* Display error message if any */}
          <p className="signin-link">
            Already have an account? <Link to="/">Sign In</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default SignUpAuth;
