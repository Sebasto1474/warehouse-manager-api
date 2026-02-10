from flask import Flask

def create_app():
    app = Flask(__name__)
    
    #basic config
    app.config["JSON_SORT_KEYS"]= False
    
    #blueprints
    #from api.routes.transfers import transfers_bp
    #app.register_blueprint(transfers_bp, url_prefix="/transfers")
    return app