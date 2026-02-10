from domain.entities.transfer import Transfer
from infrastructure.repositories.material_repository import MaterialRepository
from infrastructure.repositories.stock_repository import StockRepository
from infrastructure.repositories.transfer_repository import TransferRepository

class TransferServices:
    def __init__(self, material_repo : MaterialRepository, stock_repo : StockRepository, transfer_repo : TransferRepository):
        self.material_repo = material_repo
        self.stock_repo = stock_repo
        self.transfer_repo = transfer_repo

    def transfer_in(self, user, destination_location, material_id, quantity, description=None):
        trf_type = "In"
        if not self.material_repo.get_by_id(material_id):
            if description is None:
                raise ValueError("Material does not exist and no description was provided.")
            self.material_repo.create(material_id, description)
        stock_in = self.stock_repo.get_stock_by_location(destination_location)
        if stock_in and stock_in.material_id != material_id:
            raise ValueError("Destination location is occupied by another material.")
        if not stock_in:
            stock_in = self.stock_repo.create_stock(destination_location, material_id)
        stock_in.increase_stock(quantity)
        new_transfer = Transfer(user=user,trf_type=trf_type, origin_location=None, destination_location=destination_location, quantity=quantity)
        self.transfer_repo.save_transfer(new_transfer)
        return new_transfer


    def transfer_out(self, user, origin_location, material_id, quantity):
        trf_type = "Out"
        stock_out = self.stock_repo.get_stock_by_location(origin_location)
        if stock_out and stock_out.material_id != material_id:
            raise ValueError("Origin location is occupied by another material.")
        if not stock_out:
            raise ValueError("Stock does not exist.")
        stock_out.decrease_stock(quantity)
        new_transfer = Transfer(user=user, trf_type=trf_type, origin_location=origin_location, destination_location=None, quantity=quantity)
        self.transfer_repo.save_transfer(new_transfer)
        return new_transfer

    def transfer_move(self, user, origin_location, destination_location, material_id, quantity):
        trf_type = "Move"
        origin_stock = self.stock_repo.get_stock_by_location(origin_location)
        if origin_stock and origin_stock.material_id != material_id:
            raise ValueError("Origin location is occupied by another material.")
        if not origin_stock:
            raise ValueError("Stock does not exist.")
        destination_stock = self.stock_repo.get_stock_by_location(destination_location)
        if destination_stock and destination_stock.material_id != material_id:
            raise ValueError("Destination location is occupied by another material.")
        if not destination_stock:
            destination_stock = self.stock_repo.create_stock(destination_location, material_id)
        origin_stock.decrease_stock(quantity)
        destination_stock.increase_stock(quantity)
        new_transfer = Transfer(user=user, trf_type=trf_type, origin_location=origin_location, destination_location=destination_location, quantity=quantity)
        self.transfer_repo.save_transfer(new_transfer)
        return new_transfer
