class TransferServices:
    def __init__(self, material_repo, stock_repo, transfer_repo):
        self.material_repo = material_repo
        self.stock_repo = stock_repo
        self.transfer_repo = transfer_repo

    def transfer_in(self, user, destination_location, material_id, quantity):
        trf_type = "In"
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if not destination_location.available():
            raise ValueError("Location must be available")
        if not self.material_repo.get_by_id(material_id):
            new_material = self.material_repo.create(material_id)
        stock_in = self.stock_repo.get_stock(destination_location, material_id)
        if not stock_in:
            stock_in = self.stock_repo.create_stock(destination_location, material_id)
        stock_in.increase_stock(quantity)
        new_transfer = Transfer(user,trf_type,destination_location, quantity )
        self.transfer_repo.save(new_transfer)
        return new_transfer


    def transfer_out(self, user, origin_location, material_id, quantity):
        trf_type = "Out"
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if origin_location.available():
            raise ValueError("Location must be occupied.")
        if not self.material_repo.get_by_id(material_id):
            raise ValueError("The material ID does not exist.")
        stock_out = self.stock_repo.get_stock(origin_location, material_id)
        if not stock_out:
            raise ValueError("Stock does not exist.")
        stock_out.decrease_stock(quantity)
        new_transfer = Transfer(user, trf_type, origin_location, quantity)
        self.transfer_repo.save(new_transfer)
        return new_transfer
