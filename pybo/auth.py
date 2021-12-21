from flask import Blueprint, jsonify, request, Flask, redirect
from database import Database
from flask_jwt_extended import create_access_token
import bcrypt
import sqlite3

bp = Blueprint('user', __name__, url_prefix='/user')
# 순환참조를 확인해보기 import가 서로서로 되어있는 것은 아닌가? (구조)
# 대부분 main에서 가져온다 import한다
@bp.route("/signup", methods=['GET'])
def get_user():
    db = Database()
    user = db.get_user()
    return {"result":user}

@bp.route('/signup', methods=['POST'])
def SignUp():
    try:
        input_data = request.get_json()
        email      = input_data['email']
        password   = input_data['password']

        db = Database()
        user = db.check_user_email(email)

        if user != None and email in user:
            return jsonify({'result':'failed', 'msg':'중복된 유저입니다!'})
    
        if password:
            password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        db.SignUp(email, password)
        
        return redirect('/user/signup')

    except KeyError:
        return jsonify({'result':'key_error', 'msg':'오류입니다!'})

@bp.route('/signin', methods=['POST'])
def SignIn():
    try:
        input_data = request.get_json()
        email      = input_data['email']
        password   = input_data['password']

        db = Database()
        login = db.SignIn(email, password)
        
        if email in login[1] and password in login[2]:
            return jsonify({"message" : "success", 
                        "access_token" : create_access_token(identity = email, expires_delta = False)})
    except:
        return jsonify({"message" : "Invalid_user"})

# 해쉬화
# signup : (None, 'parkeunhye@gmail.com', '$2b$12$mpWDDSRiEa1dImbi72R4oe46LQ4V3mB2w097jsc/cd48mvSB.ApNe')
# signin :         parkeunhye@gmail.com $2b$12$Kp44wD.LXAkTYK6XcrjpTu6Fz2VdQUyZcT4gd7YrtJ94kFn39euTS
# -> flask에서 지원하는 w로 시작하는 라이브러리로 사용해보기
