from flask import Blueprint, render_template, request, redirect, Flask
from database import Database

pybo = Flask(__name__)
bp = Blueprint('question', __name__)

@bp.route("/question")
@bp.route("/question/<int:page>")
def question_page():
    db = Database()
    question = db.get_question()
    return render_template('question.html')