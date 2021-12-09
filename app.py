from flask import Flask

app = Flask(__name__)

def hello_world():
    return "<p>Hola, eunhye! Hola, flask!</p>"


@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % username


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'Post %d' % post_id

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name):
    return 'hello %s' % name

if __name__ == '__main__':
    app.run()
