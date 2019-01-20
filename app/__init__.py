from flask import Flask
from app.demo import demo


def init_app():
    app = Flask(__name__)
    app.register_blueprint(demo)

    return app
