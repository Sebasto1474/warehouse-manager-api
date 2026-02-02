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