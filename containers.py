from dependency_injector import containers, providers
from .core.business.product_business import ProductBusiness
from .api.controllers.product_controller import ProductController


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=[".api"])

    product_business = providers.Singleton(ProductBusiness, "MYSQL")

    product_controller = providers.Singleton(ProductController)
