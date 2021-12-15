# from flask import Blueprint

# bp = Blueprint('blue', __name__, url_prefix='/blue')

# @bp.route('/1')
# def print_blue():
#     return "hello Blue!"

# @bp.route('/2')
# def print_blue2():
#     return "hello Blue!2"
    
# @bp.route("/blue")
# def print_blue():
#     return "hello Blue!"

# if __name__ == '__main__':
#     bp.run(debug = True)

from flask import Blueprint

bp = Blueprint('blue', __name__, url_prefix='/blue')

@bp.route("/1")
def print_blue():
	return "hello Blue! :)"

@bp.route("/2")
def print_blue2():
	return "hello Blue!2 :)"
