class Stock:
    def __init__(self, location, material_id):
        self.location = location
        self.material_id = material_id
        self.quantity = 0

    def increase_stock(self, value):
        if value <= 0:
            raise ValueError("Value must be greater than 0.")
        if self.quantity == 0:
            self.location.occupy()
        self.quantity += value


    def decrease_stock(self, value):
        if value <= 0:
            raise ValueError("Decrease value must be greater than 0.")
        if value > self.quantity:
            raise ValueError("Decrease value cannot be greater than current stock.")
        self.quantity -= value
        if self.quantity == 0:
            self.location.free()
        