class Material:
    def __init__(self, material_id, description):
        self.material_id = material_id
        self.description = description

    def __str__(self):
        return f"{self.description}"
