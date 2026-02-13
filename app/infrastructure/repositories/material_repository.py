from domain.entities.material import Material
class MaterialRepository:
    def __init__(self):
        self.materials = {}

    def get_by_id(self, material_id):
        return self.materials.get(material_id)

    def validate_description(self, description):
        new_description = description.strip().lower()
        for material in self.materials.values():
            if material.description == new_description:
                return False
        return True

    def create_material(self, description):
        if not description:
            raise ValueError("Description is required.")
        new_description = description.strip().lower()
        for material in self.materials.values():
            if material.description == new_description:
                raise ValueError("Description already exists.")
        new_id = max(self.materials.keys(), default=0) + 1 #ID validation, if there is not any material, default 0.
        new_material = Material(new_id, new_description)
        self.materials[new_id] = new_material # saving material id 
        return new_material

    def get_all(self):
        return [material for material in self.materials.values()]