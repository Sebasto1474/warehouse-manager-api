class TransferRepository:
    def __init__(self):
        self.transfers = {}
        self.transfer_count = 0

    def save_transfer(self, transfer):
        self.transfer_count += 1
        transfer.trf_id = self.transfer_count
        self.transfers[transfer.trf_id] = transfer

    def list_all(self):
        return self.transfers

    def get_by_id(self, trf_id):
        return self.transfers.get(trf_id)

    def list_by_type(self, trf_type):
        return [t for t in self.transfers.values() if t.trf_type == trf_type]

    def list_by_user(self, user):
        return [t for t in self.transfers.values() if t.user == user]

    def list_by_origin_location(self, origin_location):
        return [t for t in self.transfers.values() if t.origin_location == origin_location]

    def list_by_destination_location(self, destination_location):
        return [t for t in self.transfers.values() if t.destination_location == destination_location]