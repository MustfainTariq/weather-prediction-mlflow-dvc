# __init__.py

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    jwt = JWTManager(app)  # Initialize JWT manager
    CORS(app)
    
    app.register_blueprint(auth, url_prefix='/auth')
    
    return app
