class Material:
    def __init__(self, material_id, description, quantity):
        self.material_id = material_id
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"Material code : {self.material_id} - {self.description}"

    def increase_quantity(self, value):
        if value <= 0:
            raise ValueError("Value must be greater than 0.")
        self.quantity += value

    def decrease_quantity(self, value):
        if value <= 0:
            raise ValueError("Value must be greater than 0.")
        if value > self.quantity:
            raise ValueError("Value cannot be greater than current stock.")
        self.quantity -= value