# Usar una imagen base con Python y Chrome preinstalados
FROM selenium/standalone-chrome:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar las pruebas
CMD ["pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]