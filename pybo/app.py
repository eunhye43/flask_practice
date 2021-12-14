from flask import Flask, request, jsonify
# from .models import Database
from views import blue

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY = "super-secret",
)

app.register_blueprint(blue.bp)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/post', methods=['GET'])
def post_get():
    post = request.args.get('post')
    print(post)
    return jsonify({'result':'success', 'msg':'get 요청'})

@app.route('/post', methods=['POST'])
def post_post():
    post = request.form['post']
    print(post)
    return jsonify({'result':'success', 'msg':'post 요청'})

if __name__ == '__main__':
    app.run(debug=True)