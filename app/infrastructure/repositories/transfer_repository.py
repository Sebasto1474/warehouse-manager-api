class TransferRepository:
    def __init__(self):
        self.transfers = {}

    def save_transfer(self, transfer):
        self.transfers[transfer.id] = transfer

    def list_all(self):
        return self.transfers