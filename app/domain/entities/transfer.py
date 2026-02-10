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

    def __str__(self):
        return f"\n[TRANSFER INFORMATION]\nUser: {self.user}\nTransfer ID: {self.trf_id}\nType: {self.trf_type}\nFrom: {self.origin_location}\nTo: {self.destination_location}\nQuantity: {self.quantity}\nDate: {self.timestamp}"
    
    def __repr__(self):
        return f"\n[TRANSFER INFORMATION]\nUser: {self.user}\nTransfer ID: {self.trf_id}\nType: {self.trf_type}\nFrom: {self.origin_location}\nTo: {self.destination_location}\nQuantity: {self.quantity}\nDate: {self.timestamp}"
