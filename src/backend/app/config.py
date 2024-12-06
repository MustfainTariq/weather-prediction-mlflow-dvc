# config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Use a secret key for JWT
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'weather_app')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')  # Change to your password
    print(SECRET_KEY)
    print(MYSQL_HOST)
    print(MYSQL_DATABASE)
    print(MYSQL_USER)
    print(MYSQL_PASSWORD)


