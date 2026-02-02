class StockRepository:
    def __init__(self):
        self.stock_locations = {}

    def get_stock_by_location(self, location):
        return self.stock_locations.get(location)

    def create_stock(self, location, material_id):
        new_stock = Stock(location, material_id)
        self.stock_locations[location] = new_stock # saving new stock
        return new_stock