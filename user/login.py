from flask import Blueprint, render_template, jsonify, request, redirect, Flask
# from database import Database

bp = Blueprint('main', __name__)

@bp.route('/signin', methods=['POST'])
def SignIn():

    admin_id = "qwer"
    admin_pw = 1234

    input_data = request.get_json()
    user_id    = input_data['user_id']
    user_pw    = input_data['user_pw']
    
    if user_id != admin_id or user_pw != admin_pw:
        return jsonify(message = "Invalid_user", status=400)
    return jsonify(
        message = "success", access_token = create_access_token(identity = user_id, expires_delta = False)
    )