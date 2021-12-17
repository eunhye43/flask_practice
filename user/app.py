from flask import Flask
from flask_jwt_extended import JWTManager

# from .models import Database
import login

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY = "super-secret-login-key"
)

jwt = JWTManager(app)
app.register_blueprint(login.bp)

@app.route('/')
def hello_pybo():
    return "Hello, pybo!!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)