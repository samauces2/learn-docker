# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .


RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la API
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
