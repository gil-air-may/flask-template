import ipdb
from dependency_injector.wiring import inject, Provide
from ..containers import Container
from .controllers import *
from flask import Flask
from dependency_injector.providers import Injection
# from .controllers.product_controller import ProductController


def create_app() -> Flask:
    app = Flask(__name__)

    container = Container()

    app.container = container
    product_controller = container.product_controller()

    # ipdb.set_trace()
    app.add_url_rule(
        '/', view_func=product_controller.create)

    return app
