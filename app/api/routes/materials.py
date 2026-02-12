from flask import Blueprint, jsonify, current_app

materials_bp = Blueprint("materials", __name__, url_prefix="/materials")


@materials_bp.route("/", methods=["GET"])
def get_materials():
    material_repo = current_app.material_repo
    material_list = []
    for material in material_repo.materials:
        material_list.append(material)
    return jsonify(material_list), 200