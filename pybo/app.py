from flask import Flask, request, jsonify
from pybo import bp as pybo_bp
from auth import bp as auth_bp
from flask_jwt_extended import *
import sqlite3

# from .models import Database
app = Flask(__name__)
jwt = JWTManager(app)

app.config.update(
    DEBUG=True,
    SECRET_KEY = "super-secret",
)

app.register_blueprint(pybo_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def hello_world():
    return "Hello, World!!"

if __name__ == '__main__':
    app.run(debug=True)

