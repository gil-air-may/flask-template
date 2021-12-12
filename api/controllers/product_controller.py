from ...core.business.product_business import ProductBusiness
from dependency_injector.wiring import Provide


class ProductController():
    product_business: ProductBusiness = Provide["product_business"]

    def create(self, product_data):
        return self.product_business.create(product_data)
