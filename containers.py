from dependency_injector import containers, providers
from .core.business.product_business import ProductBusiness
from .api.controllers.product_controller import ProductController


class Container(containers.DeclarativeContainer):
    product_business = providers.Singleton(ProductBusiness, conn="MYSQL")
    product_controller = providers.Singleton(ProductController)
    wiring_config = containers.WiringConfiguration(packages=[".api", ".core"])
