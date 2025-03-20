'''
Cada microservicio tiene un __init__.py en su carpeta app/.
Ahí es donde creamos la aplicación Flask y registramos los Blueprints.
'''
from flask import Flask
from app.routes import anime_bp  # Importamos el Blueprint de rutas


def create_app():
    app = Flask(__name__)
    app.register_blueprint(anime_bp)  # Registramos el Blueprint
    return app

'''
from flask import Blueprint

# Importamos los Blueprints definidos en otros archivos de la carpeta routes
from .anime_routes import anime_bp
from .index import front_end_bp
# Lista de Blueprints que podríamos registrar en app.py
blueprints = [anime_bp,front_end_bp]'
'''
