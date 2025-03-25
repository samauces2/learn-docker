from flask import Blueprint, jsonify
from faker import Faker
from pymongo import MongoClient




#fake = Faker()
anime_bp = Blueprint('anime', __name__)
# Conectar a MongoDB
client = MongoClient("mongodb://mongodb:27017/")  # Usar credenciales definidas en docker-compose
db = client["dragonball"]  # Acceder a la base de datos dragonball
collection = db["characters"]  # Acceder a la colección characters

@anime_bp.route('/anime-characters', methods=['GET'])
def get_anime_characters():
    '''#data = [{"name": fake.first_name(), "power_level": "100", "anime": "Dragon Ball Z"} for _ in range(10)]
    #print(data)
    data = []
    for _ in range(10):  # Generar 10 personajes ficticios
        data.append({
            "name": fake.first_name(),
            "power_level": fake.random_int(min=1000, max=9000),
            "anime": "Dragon Ball Z"
        })
        print (data)
    return jsonify(data)'''
    # Consultar la base de datos para obtener los personajes
    characters = collection.find()
    # Convertir los resultados a una lista de diccionarios para jsonify
    data = []
    for character in characters:
        data.append({
            "name": character["name"],
            "power_level": character["power_level"],
            "anime": "Dragon Ball Z"  # O cualquier otro dato si lo tienes en la DB
        })
    return jsonify(data)
