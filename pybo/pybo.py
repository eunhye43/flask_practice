from flask import Flask, Blueprint, render_template, request, redirect
from database import Database

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route("/question", methods=['GET'])
def question_get():
    db = Database()
    question = db.get_question()
    return question

@bp.route("/answer", methods=['GET'])
def answer_get():
    db = Database()
    answer = db.get_answer()
    return answer

@bp.route('/question/<int:id>', methods=['POST'])
def question_post():

    subject = request.form['subject']
    content = request.form['content']

    db = Database()
    db.insert_post(subject, content)

    return redirect('/question')

@bp.route('/question/<int:question_id>', methods=['POST'])
def aswner_post():

    question = request.form['question_id']
    content = request.form['content']

    db = Database()
    db.insert_post(question, content)

    return redirect('/answer')

# @app.route('/post', methods=['GET'])
# def post_get():
#     post = request.args.get('post')
#     print(post) #none이라고 뜸
#     return jsonify({'result':'success', 'msg':'get 요청'})

# @app.route('/post', methods=['POST'])
# def post_post():
#     post = request.form['post']
#     print(post) #405 error..
#     return jsonify({'result':'success', 'msg':'post 요청'})

# @app.route('/memo', methods=['GET'])
# def listing():
#     memo = 