from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import os
import platform
import stat
import requests
import zipfile
import shutil
import re

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Obtener la versión de Chrome instalada
    chrome_version_output = os.popen("google-chrome --version").read().strip()
    chrome_version = re.search(r"\d+\.\d+\.\d+", chrome_version_output).group()
    chrome_major_version = chrome_version.split(".")[0]

    print(f"Versión de Chrome: {chrome_version}")
    print(f"Versión mayor de Chrome: {chrome_major_version}")

    # Descargar ChromeDriver correspondiente a la versión de Chrome
    chromedriver_url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_major_version}"
    print(f"URL de la versión de ChromeDriver: {chromedriver_url}")

    try:
        chromedriver_version = requests.get(chromedriver_url).text.strip()
        print(f"Versión de ChromeDriver: {chromedriver_version}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al obtener la versión de ChromeDriver: {e}")

    # Descargar el archivo ZIP de ChromeDriver
    chromedriver_zip_url = f"https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_linux64.zip"
    print(f"URL de descarga de ChromeDriver: {chromedriver_zip_url}")

    chromedriver_zip_path = "/tmp/chromedriver.zip"
    try:
        with requests.get(chromedriver_zip_url, stream=True) as r:
            r.raise_for_status()
            with open(chromedriver_zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al descargar ChromeDriver: {e}")

    # Extraer el archivo ZIP
    chromedriver_dir = "/tmp/chromedriver"
    os.makedirs(chromedriver_dir, exist_ok=True)
    try:
        with zipfile.ZipFile(chromedriver_zip_path, "r") as zip_ref:
            zip_ref.extractall(chromedriver_dir)
    except zipfile.BadZipFile as e:
        raise Exception(f"Error al extraer el archivo ZIP de ChromeDriver: {e}")

    # Obtener la ruta del binario de ChromeDriver
    chromedriver_path = os.path.join(chromedriver_dir, "chromedriver")
    if not os.path.isfile(chromedriver_path):
        raise Exception(f"No se encontró el binario de ChromeDriver en: {chromedriver_path}")

    # Dar permisos de ejecución al ChromeDriver
    os.chmod(chromedriver_path, stat.S_IRWXU)
    print(f"ChromeDriver descargado en: {chromedriver_path}")

    # Configurar el servicio de ChromeDriver
    service = Service(chromedriver_path)

    # Crear la instancia del driver
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver