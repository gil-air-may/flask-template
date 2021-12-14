import ipdb


class ProductBusiness():
    def __init__(self, conn: str):
        self.conn = conn

    def create(self):
        # print(f"connecting to {self.conn}")
        return f"product successfully created on connection {self.conn}"
