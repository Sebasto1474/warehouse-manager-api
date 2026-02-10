from datetime import datetime
class Transfer:
    def __init__(self, user, trf_type, origin_location, destination_location, quantity):
        self.user = user
        self.trf_type =  trf_type
        self.origin_location = origin_location
        self.destination_location = destination_location
        self.quantity = quantity
        self.timestamp = datetime.now()
        self.trf_id = None
        self.origin_status = (origin_location.status if origin_location else None)
        self.destination_status = (destination_location.status if destination_location else None)

    def __str__(self):
        return f"\n[TRANSFER INFORMATION]\nUser: {self.user}\nTransfer ID: {self.trf_id}\nType: {self.trf_type}\nFrom: {self.origin_location} | Status: {self.origin_status}\nTo: {self.destination_location} | Status: {self.destination_status}\nQuantity: {self.quantity}\nDate: {self.timestamp}"
    
    def __repr__(self):
        return f"\n[TRANSFER INFORMATION]\nUser: {self.user}\nTransfer ID: {self.trf_id}\nType: {self.trf_type}\nFrom: {self.origin_location} | Status: {self.origin_status}\nTo: {self.destination_location} | Status: {self.destination_status}\nQuantity: {self.quantity}\nDate: {self.timestamp}"
