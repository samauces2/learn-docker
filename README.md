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



explicacion de Dockerfile:

FROM python:3.10 → Indica que la imagen base será Python 3.10.
Las imágenes base ya tienen Python instalado, por lo que no necesitas instalarlo manualmente.

WORKDIR /app → Establece /app como el directorio de trabajo dentro del contenedor.
Todos los archivos y comandos que ejecutemos estarán dentro de /app.


COPY . . → Copia todos los archivos del directorio actual del host al contenedor en /app.

RUN pip install --no-cache-dir -r requirements.txt → Instala las dependencias especificadas en requirements.txt.
--no-cache-dir evita que se almacenen archivos temporales, reduciendo el tamaño de la imagen.

EXPOSE 5000 → Indica que la aplicación usará el puerto 5000.
Esto NO mapea el puerto a la máquina host, solo documenta qué puerto usará el contenedor.

CMD ["python", "app.py"] → Ejecuta el comando python app.py cuando el contenedor inicie.
CMD define el comando predeterminado que se ejecutará dentro del contenedor.

