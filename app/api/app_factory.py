from flask import Flask
from api.routes.health import health_bp

def create_app():
    app = Flask(__name__)
    
    #basic config
    app.config["JSON_SORT_KEYS"]= False
    
    #blueprints
    app.register_blueprint(health_bp)
    
    return app