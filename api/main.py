from .controllers.product_controller import ProductController
from dependency_injector.providers import Injection
from flask import Flask
from .controllers import *
from ..containers import Container
from dependency_injector.wiring import inject, Provide


@inject
def create_app(product_controller: ProductController = Provide[Container.product_controller]) -> Flask:
    app = Flask(__name__)
    container = Container()
    app.container = container

    app.add_url_rule(
        '/', view_func=product_controller.create)
    return app
