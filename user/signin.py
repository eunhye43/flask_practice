from flask import Blueprint, render_template, request, redirect, Flask
from database import Database

user = Flask(__name__)
bp = Blueprint('main', __name__)

@app.route('/signin', methods=['GET', 'POST'])
def SignIn():
    msg = ''
    return render_template('index.html', msg='')


user.run()