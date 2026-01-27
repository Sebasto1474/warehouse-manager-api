from datetime import datetime
class Transfer:
    def __init__(self, user, trf_type, location, destination, quantity):
        self.user = user
        self.trf_type =  trf_type
        self.location = location
        self.destination = destination
        self.quantity = quantity
        timestamp = datetime.now()
