class MaterialRepository:
    def __init__(self):
        self.materials_id = {}

    def get_by_id(self, material_id):
        if material_id in self.materials_id:
            material_tgt = self.materials_id[material_id]
        else:
            return None
        return material_tgt

    def create(self, material_id, description):
        new_material = Material(material_id, description)
        self.materials_id[material_id] = new_material # saving material id 
        return new_material

