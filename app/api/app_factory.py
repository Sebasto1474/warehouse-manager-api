from flask import Flask
from api.routes.health import health_bp
from api.routes.materials import materials_bp
from infrastructure.repositories.material_repository import MaterialRepository
from infrastructure.repositories.stock_repository import StockRepository
from infrastructure.repositories.transfer_repository import TransferRepository

def create_app():
    app = Flask(__name__)
    
    #basic config
    app.config["JSON_SORT_KEYS"]= False
    
    #repositories
    app.material_repo = MaterialRepository()
    app.stock_repo = StockRepository()
    app.transfer_repo = TransferRepository()
    
    #blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(materials_bp)
    
    return app