from flask import Blueprint, jsonify, request, Flask, redirect
from database import Database
import bcrypt
import sqlite3

bp = Blueprint('user', __name__, url_prefix='/user')
# 순환참조를 확인해보기 import가 서로서로 되어있는 것은 아닌가? (구조)
# 대부분 main에서 가져온다 import한다
@bp.route("/signup", methods=['GET'])
def get_user():
    db = Database()
    user = db.check_user_email()
    print(user)
    return {"answer":user}

@bp.route('/signup', methods=['POST'])
def SignUp():
    try:
        input_data = request.get_json()
        email      = input_data['email']
        password   = input_data['password']

        db = Database()
        print(email)
        user = db.check_user_email(email)
        print(user)
        # conn = sqlite3.connect("database.db")
        # cur = conn.cursor()
        # query = """select email from user where email = ?"""
        # cur.execute(query, (email))
        # user = cur.fetchall()
        # print("-----------------")
        # print(user)
        # print(type(user))
        # print("-----------------")
        # print(query)
        # print(user['email'])
        if email in user:

            # print(email in db.get_user) #false
            # select query 구현 하나 더 
            return jsonify({'result':'failed', 'msg':'중복된 유저입니다!'})
    
        if password:
            password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        db.SignUp(email, password)
        return redirect('/user/signup')

    except KeyError:
        return jsonify({'result':'key_error', 'msg':'오류입니다!'})

@bp.route('/signin', methods=['POST'])
def SignIn():

    input_data = request.get_json()

    db = Database()
    login = db.SignIn()

    admin_id = "qwer"
    admin_pw = 1234

    user_id    = input_data['user_id']
    user_pw    = input_data['user_pw']
    print(user_id, user_pw)
    if user_id == admin_id and user_pw == admin_pw:
        return jsonify({"message" : "success", 
                    "access_token" : create_access_token(identity = user_id, expires_delta = False)})
    
    return jsonify({"message" : "Invalid_user"})

    # def question_get():
    # db = Database()
    # question = db.get_question()
    # # print(question[1]) -> (2, 'sqlite3', '값넣기', None, None)
    # # question type은 list
    # print(question)
    # return {'question':question}
    #return jsonify(
    #    message = "success", access_token = create_access_token(identity = user_id, expires_delta = False)
    #)

# @bp.route('/signin', methods=['POST'])
# def SignIn():

#     input_data = request.get_json()
    
#     admin_id = "qwer"
#     admin_pw = 1234

#     user_id    = input_data['user_id']
#     user_pw    = input_data['user_pw']
#     print(user_id, user_pw)
#     if user_id == admin_id and user_pw == admin_pw:
#         return jsonify({"message" : "success", 
#                     "access_token" : create_access_token(identity = user_id, expires_delta = False)})
    
#     return jsonify({"message" : "Invalid_user"})