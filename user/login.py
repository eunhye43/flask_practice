from flask import Blueprint, jsonify, request, Flask
from database import Database
from flask_jwt_extended import *
import apps

bp2 = Blueprint('blue', __name__)
jwt = JWTManager(apps)

@bp2.route('/signin', methods=['POST'])
def SignIn():

    input_data = request.get_json()

    admin_id = "qwer"
    admin_pw = 1234

    user_id    = input_data['user_id']
    user_pw    = input_data['user_pw']

    if user_id == admin_id or user_pw == admin_pw:
        return jsonify({"message" : "success", 
                    "access_token" : create_access_token(identity = user_id, expires_delta = False)})
    # return jsonify({"message" : "Invalid_user"})
    #return jsonify(
    #    message = "success", access_token = create_access_token(identity = user_id, expires_delta = False)
    #)


# if (user_id == admin_id and \
#         user_pw == admin_pw):
#         return jsonify(
#             result = "success",
#             access_token = create_access_token(identity=user_id,
#                                             expires_delta = False)
#         )
#     return jsonify(
#         result = "Invalid Params!"
#    )