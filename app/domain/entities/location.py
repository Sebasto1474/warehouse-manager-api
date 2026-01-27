class Location:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number
        self.code = f"{letter}{number}"
        self.is_occupied = False

    def __str__(self):
        return f"Location: {self.code}"

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