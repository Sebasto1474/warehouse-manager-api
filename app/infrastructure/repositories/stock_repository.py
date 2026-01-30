class StockRepository:
    def __init__(self):
        pass

    def get_stock(self, location, material_id):
        pass

    def get_stock_by_location(self, location):
        pass

    def create_stock(self, location, material_id):
        new_stock = Stock(location, material_id)
        return new_stock