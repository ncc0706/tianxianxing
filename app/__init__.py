from flask import Flask
from app.demo import demo

from app.post_mp_qq_com import mp_qq


def init_app():
    app = Flask(__name__)
    app.register_blueprint(demo)
    app.register_blueprint(mp_qq)
    return app
