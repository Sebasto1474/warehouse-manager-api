from flask import Blueprint, jsonify, current_app, request

materials_bp = Blueprint("materials", __name__, url_prefix="/materials")


@materials_bp.route("/", methods=["GET"])
def get_materials():
    material_repo = current_app.material_repo
    materials = material_repo.get_all()
    material_list = [
        {
            "material_id" : material.material_id,
            "description" : material.description
        }
        for material in materials
    ]
    return jsonify(material_list), 200

@materials_bp.route("/<int:material_id>", methods=["GET"])
def get_material_by_id(material_id):
    material_repo = current_app.material_repo
    material_tgt = material_repo.get_by_id(material_id)
    if material_tgt is None:
        return jsonify({"error" : "Material not found"}), 404
    material_dict = {"material_id" : material_tgt.material_id,
                    "description" : material_tgt.description}
    return jsonify(material_dict), 200

@materials_bp.route("/", methods=["POST"])
def create_material():
    data = request.get_json()
    if not data:
        return jsonify({"error" : "Invalid JSON"}), 400
    description = data.get("description", "").strip()
    if not description:
        return jsonify({"error": "Description is required"}), 400
    material_repo = current_app.material_repo
    try:  
        new_material = material_repo.create_material(description)
    except ValueError as e:
        return jsonify({"error" : str(e)}), 409
    return jsonify({"material_id" : new_material.material_id,
                    "description" : new_material.description}), 201