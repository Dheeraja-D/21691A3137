from flask import Flask
from .config import Config
from .routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(routes_bp)
    return app
