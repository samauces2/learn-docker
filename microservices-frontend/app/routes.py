from flask import Blueprint, render_template
import requests

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route("/")
def home():
    response = requests.get("http://api:5000/anime-characters")  # Conectamos a la API
    data = response.json()
    return render_template("index.html", characters=data)
    #db = current_app.db
    #characters_collection = db["characters"]
    #characters = list(characters_collection.find({}, {"_id": 0}))  # Excluir _id
    #return jsonify(characters)

'''
# Configurar la conexión con MongoDB
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/anime_db")
mongo = PyMongo(app)

# Endpoint para obtener personajes desde MongoDB
@database_bp.route("/characters", methods=["GET"])
def get_characters():
    characters = list(mongo.db.characters.find({}, {"_id": 0}))  # Excluye _id para evitar problemas con JSON
    return jsonify(characters)

'''