from flask import Blueprint

bp = Blueprint('blue', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/eunhye')
def hello_eunhye():
    return 'Hello, eunhye!'

@bp.route('/')
def index():
    return 'Pybo index!'