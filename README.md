# learn-docker
🚀 Próximos Pasos para Mejorar tu Proyecto

✅ 1️⃣ Agregar Variables de Entorno
✅ 2️⃣ Montar Volúmenes para Desarrollo
✅ 3️⃣ Crear un Dockerfile Multi-Stage


1️⃣ Agregar Variables de Entorno

📌 En lugar de hardcodear valores, usaremos variables de entorno para que el código sea más flexible.
🔹 Modificar app.py para usar variables de entorno

Abre app.py y cambia el código para leer el puerto desde una variable de entorno:


🔹 Modificar docker-compose.yml para usar variables

📌 ¿Por qué esto es útil?

    Puedes cambiar el puerto sin modificar el código.
    Puedes definir variables en .env y mantenerlas fuera del repositorio.

2️⃣ Montar Volúmenes para Desarrollo

📌 Ahora, en lugar de reconstruir el contenedor cada vez que cambies el código, usaremos un volumen para que los cambios se reflejen en tiempo real.
🔹 Modificar docker-compose.yml

Edita docker-compose.yml y agrega el volumen:
volumes:
      - .:/app  # Monta el código fuente dentro del contenedor
📌 ¿Qué hace esto?

    Ahora, cualquier cambio en app.py se reflejará sin necesidad de reconstruir el contenedor.
    Perfecto para desarrollo rápido. 🚀

3️⃣ Crear un Dockerfile Multi-Stage

📌 Un Dockerfile multi-stage reduce el tamaño final de la imagen y hace que la construcción sea más eficiente.
🔹 Modificar Dockerfile

Edita tu Dockerfile y reemplázalo 

📌 ¿Qué mejoras tiene?

    Usa dos etapas:
    1️⃣ Una para instalar dependencias.
    2️⃣ Otra para copiar solo lo necesario.
    Reduce el tamaño de la imagen final.
    Hace la construcción más rápida.


 🚀 ¿Cómo probar los cambios?
📌 Levantar la aplicación con docker-compose


Ahora tu aplicación tiene: ✅ Variables de entorno
✅ Montaje de volúmenes para desarrollo
✅ Dockerfile optimizado con multi-stage


Dockerfile explanation:

FROM python:3.10 AS builder → Esta es la primera etapa, llamada builder.
Aquí instalaremos las dependencias antes de crear la imagen final.

WORKDIR /app → Igual que antes, establecemos /app como directorio de trabajo.

COPY requirements.txt . → Solo copiamos requirements.txt en esta etapa.
Así evitamos copiar archivos innecesarios antes de instalar las dependencias.

RUN pip install --no-cache-dir -r requirements.txt → Instalamos dependencias en la primera etapa.

FROM python:3.10 → Aquí comenzamos una nueva imagen, sin las capas de la anterior.
Esto evita traer archivos temporales o dependencias que no necesitamos.
WORKDIR /app → Igual que antes, establecemos el directorio de trabajo.
COPY --from=builder ... → Copia solo las librerías de Python instaladas en la primera etapa.
Esto evita traer archivos innecesarios.
COPY app.py . → Copiamos solo el archivo app.py a la imagen final.
Esto reduce el tamaño de la imagen porque no copiamos todo el código fuente.

EXPOSE 5000 → Como antes, indica que la aplicación usará el puerto 5000.
CMD ["python", "app.py"] → Ejecuta la aplicación cuando el contenedor inicie.