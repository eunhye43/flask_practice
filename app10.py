from flask import Flask, request, jsonify
from flask_jwt_extended import *

application = Flask(import_name = __name__)
application.config.update(
    DEBUG = True,
    JWT_SECRET_KEY = "get some rest"
)

jwt = JWTManager(application)

@application.route("/")
def test1():
    return "<h2>hola, soy Ria!<h2>"


@application.route("/login", methods=['POST'])
def login_proc():

    input_data = request.get_json()
    # 들어오는 값 json형태로 변환해서 input_data 변수에 넣어줄거야
    admin_id = "1234"
    admin_pw = "qwer"
    user_id = input_data['id']
    user_pw = input_data['pw']
    
    if (user_id == admin_id and \
        user_pw == admin_pw):
        return jsonify(
            result = "success",
            access_token = create_access_token(identity=user_id,
                                            expires_delta = False)
        )
    return jsonify(
        result = "Invalid Params!"
    )


@application.route('/user_only', methods=["GET"])
@jwt_required
def user_only():
    cur_user = get_jwt_identity()
    if cur_user is None:
        return "User Only!"
    else:
        return "Hi," + cur_user

if __name__ == '__main__':
    application.run(port = 5000,
                    debug = True)