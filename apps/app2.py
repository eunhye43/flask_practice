from flask import Flask, flash, redirect, render_template, request
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/user/")
def hello():
 
    users = [ "Frank", "Steve", "Alice", "Bruce" ]
    var = 1
    return render_template(
        'user.html', **locals())
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug = True)
    # app.run()

