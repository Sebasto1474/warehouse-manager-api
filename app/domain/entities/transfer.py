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
