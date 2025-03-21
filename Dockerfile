# Usar una imagen base con Python y Chrome preinstalados
FROM selenium/standalone-chrome:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Crear un entorno virtual
RUN python3 -m venv /opt/venv

# Activar el entorno virtual e instalar las dependencias
RUN . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar las pruebas
CMD ["/opt/venv/bin/pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]