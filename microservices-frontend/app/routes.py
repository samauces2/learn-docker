from flask import Blueprint, render_template
import requests

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route("/")
def home():
    response = requests.get("http://api:5000/anime-characters")  # Conectamos a la API
    data = response.json()
    return render_template("index.html", characters=data)
