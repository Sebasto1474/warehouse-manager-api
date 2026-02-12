from domain.entities.material import Material
class MaterialRepository:
    def __init__(self):
        self.materials = {}

    def get_by_id(self, material_id):
        return self.materials.get(material_id) # improve code

    def create_material(self, material_id, description):
        new_material = Material(material_id, description)
        self.materials[material_id] = new_material # saving material id 
        return new_material

    def get_all(self):
        return [material for material in self.materials.values()]