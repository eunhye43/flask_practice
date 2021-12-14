from flask import Flask, Blueprint, render_template, request, redirect
from database import Database

pybo = Flask(__name__)
bp = Blueprint('question', __name__)

@bp.route("/question")
# @pybo.route("/")
def question_page():
    db = Database()
    question = db.get_question()
    # return render_template('question.html')
    return question

if __name__ == '__main__':
    pybo.run(debug=True)