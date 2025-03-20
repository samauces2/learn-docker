'''
Cada microservicio tiene un __init__.py en su carpeta app/.
Ahí es donde creamos la aplicación Flask y registramos los Blueprints.
'''

from flask import Flask
from app.routes import frontend_bp  # Importamos el Blueprint del Front-End

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(frontend_bp)  # Registramos el Blueprint
    return app
