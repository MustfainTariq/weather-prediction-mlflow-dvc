# models.py

import mysql.connector
from flask import current_app

class User:
    def __init__(self, id, full_name, email, password):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password

    @staticmethod
    def create_user(full_name, email, password):
        connection = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            database=current_app.config['MYSQL_DATABASE'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD']
        )
        cursor = connection.cursor()
        query = "INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (full_name, email, password))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_user_by_email(email):
        connection = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            database=current_app.config['MYSQL_DATABASE'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD']
        )
        cursor = connection.cursor()
        cursor.execute("SELECT id, full_name, email, password FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return User(result[0], result[1], result[2], result[3])
        return None
