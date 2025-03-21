# Usar una imagen base con Python y Chrome preinstalados
FROM selenium/standalone-chrome:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar python3-venv
RUN sudo apt-get update && \
    sudo apt-get install -y python3-venv

# Crear un entorno virtual en /home/seluser/venv
RUN python3 -m venv /home/seluser/venv

# Activar el entorno virtual e instalar las dependencias
RUN . /home/seluser/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Crear la carpeta reports en /home/seluser/reports
RUN mkdir -p /home/seluser/reports && \
    chmod -R 777 /home/seluser/reports

# Comando por defecto para ejecutar las pruebas
CMD ["/home/seluser/venv/bin/pytest", "tests/", "--html=/home/seluser/reports/report.html", "--self-contained-html"]