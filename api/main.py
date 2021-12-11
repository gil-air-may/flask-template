from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.add_url_rule('/', view_func=hello_world)
    return app


def hello_world():
    return "<p>Hello, World!</p>"
