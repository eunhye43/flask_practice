from flask import Flask
import blue

app = Flask(__name__)
app.register_blueprint(blue.bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# app.run()
if __name__ == '__main__':
    app.run(debug = True)
