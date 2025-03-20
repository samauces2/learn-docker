'''from flask import Flask, jsonify
from routes import blueprints  # Importamos la lista de Blueprints desde __init__.py

app = Flask(__name__)
fake = Faker()

@app.route('/status', methods=['GET'])
def health_check():
    return jsonify({"status": "API funcionando correctamente 🚀"}), 200
'''
'''
@app.route('/anime-characters', methods=['GET'])
def get_anime_characters():
    """Genera datos ficticios de personajes de anime en formato tabla JSON"""
    data = []
    
    for _ in range(10):  # Generar 10 personajes ficticios
        data.append({
            "name": fake.first_name(),
            "power_level": fake.random_int(min=1000, max=9000),
            "anime": "Dragon Ball Z"
        })
    
    # Convertimos la lista en una tabla con Pandas
    df = pd.DataFrame(data)

    return jsonify(df.to_dict(orient="records"))
'''
'''
# Registramos automáticamente todos los Blueprints en la lista
for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
'''