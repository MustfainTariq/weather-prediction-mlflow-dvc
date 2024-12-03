import "./AuthForm.css";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const SignUpAuth = () => {
  const navigate = useNavigate();
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validation or signup logic here (e.g., send to API)

    // On successful sign-up, navigate to the weather prediction page
    navigate("/weather-prediction");
  };
  return (
    <div className="container">
      {/* Sign In Form */}
      <div className="form-container sign-up-container">
        <h1>Sign Up</h1>
        <form onSubmit={handleSubmit}>
          <input type="text" placeholder="Full Name" required />
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Password" required />
          <button type="submit">Sign Up</button>
          <p className="signin-link">
            Already have an account? <Link to="/">Sign In</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default SignUpAuth;
