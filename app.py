import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mundo desde Flask en Docker!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Si no hay variable, usa 5000
    app.run(host="0.0.0.0", port=port)
