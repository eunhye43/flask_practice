from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from database import Database
from flask_jwt_extended import *

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route("/question", methods=['GET'])
def question_get():
    db = Database()
    question = db.get_question()
    # print(question[1]) -> (2, 'sqlite3', '값넣기', None, None)
    # question type은 list
    print(question)
    return {'question':question}
    # TypeError: The view function did not return a valid response. 
    # The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list.

@bp.route("/answer", methods=['GET'])
def answer_get():
    db = Database()
    answer = db.get_answer()
    print(type(answer))
    # 마찬가지
    return {"answer":answer}

@bp.route('/question', methods=['POST'])
def question_post():

    subject = request.form['subject']
    content = request.form['content']

    db = Database()
    db.insert_question(subject, content)

    return redirect('/board/question')

@bp.route('/answer', methods=['POST'])
def answer_post():

    question_id = request.form['question_id']
    content = request.form['content']

    db = Database()
    db.insert_answer(question_id, content)

    return redirect('/board/answer')

@bp.route('/post', methods=['GET'])
def post_get():
    post = request.args.get('post')
    print(post) #none이라고 뜸
    return jsonify({'result':'success', 'msg':'get 요청'})

# @app.route('/post', methods=['POST'])
# def post_post():
#     post = request.form['post']
#     print(post) #405 error..
#     return jsonify({'result':'success', 'msg':'post 요청'})

# @app.route('/memo', methods=['GET'])
# def listing():
#     memo = 