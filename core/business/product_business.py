class ProductBusiness():
    def __init__(self, conn: str):
        self.connection = conn

    def create(self, product_data):
        print(f"connecting to {self.conn}")
        return 'product successfully created'
