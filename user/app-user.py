from flask import Flask
# from .models import Database
import blue

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY = "super-secret",
)

app.register_blueprint(blue.bp)

@app.route('/')
def hello_world():
    return "Hello, World!:)"

if __name__ == '__main__':
    app.run(debug=True)