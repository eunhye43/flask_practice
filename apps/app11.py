from flask import Flask
import blue

app = Flask(__name__)
app.register_blueprint(blue.bp)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return "Hello, World!"


app.run()
=======
    return 'Hello, World!'

# app.run()
if __name__ == '__main__':
    app.run(debug = True)
>>>>>>> d67acb7b1fe04b4166da23e719800845e663fd49
