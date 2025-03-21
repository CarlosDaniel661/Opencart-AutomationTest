# Usar una imagen base con Python y Chrome preinstalados
FROM selenium/standalone-chrome:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Crear un entorno virtual en /home/seluser/venv
RUN python3 -m venv /home/seluser/venv

# Activar el entorno virtual e instalar las dependencias
RUN . /home/seluser/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar las pruebas
CMD ["/home/seluser/venv/bin/pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]