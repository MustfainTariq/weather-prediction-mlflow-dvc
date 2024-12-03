import "./AuthForm.css";
import { Link, useNavigate } from "react-router-dom";

const AuthForm = () => {
  const navigate = useNavigate();
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validation or signup logic here (e.g., send to API)

    // On successful sign-up, navigate to the weather prediction page
    navigate("/prediction");
  };
  return (
    <div className="container">
      {/* Sign In Form */}

      <div className="form-container sign-in-container">
        <h1>Sign In to Weather Pred.</h1>
        <form onSubmit={handleSubmit}>
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Password" required />
          <button type="submit">Sign In</button>
          <p className="signup-link">
            Don't have an account? <Link to="/sign-up">Sign Up</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default AuthForm;
