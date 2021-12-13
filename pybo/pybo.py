from flask import Flask
from views import blue

app = Flask(__name__)
app.register_blueprint(blue.bp)

@app.route('/')
def hello_world():
    return "Hello, World!"

app.run()
