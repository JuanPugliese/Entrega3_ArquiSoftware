# app/__init__.py

from flask import Flask
from app.config import Config
from app.models import db
from app.views import mostrar_productos

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route('/')
    def index():
        return mostrar_productos()

    return app
