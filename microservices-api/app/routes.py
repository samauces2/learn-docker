from flask import Blueprint, jsonify
from faker import Faker
api_bp = Blueprint("api", __name__)



fake = Faker()
anime_bp = Blueprint('anime', __name__)

@anime_bp.route('/anime-characters', methods=['GET'])
def get_anime_characters():
    #data = [{"name": fake.first_name(), "power_level": "100", "anime": "Dragon Ball Z"} for _ in range(10)]
    #print(data)
    data = []
    for _ in range(10):  # Generar 10 personajes ficticios
        data.append({
            "name": fake.first_name(),
            "power_level": fake.random_int(min=1000, max=9000),
            "anime": "Dragon Ball Z"
        })
        print (data)
    return jsonify(data)
