from flask import Blueprint

demo = Blueprint('demo', __name__)


@demo.route('/demo')
def hello():
    return "hello"


@demo.route('/msg')
def msg():
    return 'hello msg'
