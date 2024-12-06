# auth.py

from flask import Blueprint, request, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    full_name = data.get('fullname')
    email = data.get('email')
    password = data.get('password')
    
    if not full_name or not email or not password:
        return jsonify({"msg": "Please provide all required fields"}), 400

    hashed_password = generate_password_hash(password)
    
    # Create user in the database
    User.create_user(full_name, email, hashed_password)
    
    return jsonify({"msg": "User created successfully!"}), 201


@auth.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"msg": "Please provide both email and password"}), 400
    
    user = User.get_user_by_email(email)
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid email or password"}), 401
    
    # Create JWT Token
    access_token = create_access_token(identity=user.id)
    
    return jsonify({"msg": "Login successful", "access_token": access_token}), 200
