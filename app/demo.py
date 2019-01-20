from flask import Blueprint, render_template

demo = Blueprint('demo', __name__)


@demo.route('/demo')
def hello():
    return "hello"


@demo.route('/msg')
def msg():
    return 'hello msg'


@demo.route('/dh')
def dh():
    return render_template('mp_qq.html')
