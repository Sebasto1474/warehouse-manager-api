class Location:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number
        self.is_occupied = False

    @property
    def code(self):
        return f"{self.letter}{self.number}"

    @property
    def status(self):
        return "OCCUPIED" if self.is_occupied else "AVAILABLE"

    def __str__(self):
        return self.code

    def __repr__(self):
        return f"Location(code={self.code}, status={self.status})"

    def available(self):
        return not self.is_occupied

    def occupy(self):
        if self.is_occupied:
            raise ValueError("Location is already occupied.")
        self.is_occupied = True

    def free(self):
        if not self.is_occupied:
            raise ValueError("Location is already free.")
        self.is_occupied = False