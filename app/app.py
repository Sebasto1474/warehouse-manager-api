from domain.entities.location import Location
from infrastructure.repositories.material_repository import MaterialRepository
from infrastructure.repositories.stock_repository import StockRepository
from infrastructure.repositories.transfer_repository import TransferRepository
from services.transfer_services import TransferServices

def main():
    #Repositories
    material_repo = MaterialRepository()
    stock_repo = StockRepository()
    transfer_repo = TransferRepository()
    
    #Servicios
    transfer_service = TransferServices(material_repo=material_repo, stock_repo=stock_repo, transfer_repo=transfer_repo)
    
    #Locations
    location_1 = Location("A", 1)
    location_2 = Location("B", 1)
    location_3 = Location("C",1)
    
    #User
    
    user = "Sebastian"
    
    
    print("------TRANSFER IN------")
    transfer_service.transfer_in(user=user,destination_location=location_1,material_id=1001,quantity=50,description="Azucar")

    
    print("------TRANSFER IN------")
    transfer_service.transfer_in(user=user,destination_location=location_2,material_id=1002,quantity=200,description="Gelatina")

    
    print("------TRANSFER MOVE------")
    transfer_service.transfer_move(user=user, origin_location=location_2, destination_location=location_3,material_id=1002, quantity=100)

    
    print("------TRANSFER OUT------")
    transfer_service.transfer_out(user=user, origin_location=location_1, material_id=1001, quantity=20)

    print("------TRANSFER OUT------")
    transfer_service.transfer_out(user=user, origin_location=location_3, material_id=1002, quantity=100)


    print("\n------ TRANSFERS HISTORY ------")
    for trf in transfer_repo.list_all().values():
        print(trf)
    
    print("\n------ LOCATIONS DISPLAY ------")
    for location, stock in stock_repo.stock_locations.items():
        print(f"{location} - {stock}")

if __name__ == "__main__":
        main()