# learn-docker
📌 Objetivo

📌 Crear una aplicación Flask simple que devuelva "Hola, mundo" en un contenedor Docker.
📌 Usar un Dockerfile para empaquetar la aplicación.
📌 Usar docker-compose.yml para facilitar la ejecución.
1️⃣ Estructura del Proyecto

📁 flask-docker-app/
┣ 📄 app.py → Código de la aplicación Flask
┣ 📄 requirements.txt → Librerías necesarias
┣ 📄 Dockerfile → Imagen para Docker
┣ 📄 docker-compose.yml → Orquestación de contenedores
2️⃣ Crear el Código de Flask

📌 Crea el archivo app.py con el contenido 

3️⃣ Especificar Dependencias

📌 Crea un archivo requirements.txt

4️⃣ Crear el Dockerfile

📌 Crea un archivo Dockerfile

6️⃣ Construir y Correr el Contenedor

📌 Construir la imagen:
docker build -t flask-app .

📌 Ejecutar el contenedor:

docker run -p 5000:5000 flask-app

7️⃣ Probar la Aplicación

📌 Abre tu navegador y ve a:
👉 http://localhost:5000

Deberías ver "Hola, mundo desde Flask en Docker!" 🎉