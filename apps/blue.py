from flask import Blueprint

bp = Blueprint('blue', __name__)

@bp.route("/blue")
def print_blue():
    return "hello, Blue!"

if __name__ == '__main__':
    bp.run()

