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

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    chrome_version = os.popen("google-chrome --version").read().strip().split()[-1]
    chrome_major_version = chrome_version.split(".")[0]

    chromedriver_url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_major_version}"
    chromedriver_version = requests.get(chromedriver_url).text.strip()

    chromedriver_zip_url = f"https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_linux64.zip"
    chromedriver_zip_path = "/tmp/chromedriver.zip"
    with requests.get(chromedriver_zip_url, stream=True) as r:
        r.raise_for_status()
        with open(chromedriver_zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Extraer el archivo ZIP
    chromedriver_dir = "/tmp/chromedriver"
    os.makedirs(chromedriver_dir, exist_ok=True)
    with zipfile.ZipFile(chromedriver_zip_path, "r") as zip_ref:
        zip_ref.extractall(chromedriver_dir)

    # Obtener la ruta del binario de ChromeDriver
    chromedriver_path = os.path.join(chromedriver_dir, "chromedriver")

    # Dar permisos de ejecución al ChromeDriver
    os.chmod(chromedriver_path, stat.S_IRWXU)
    print(f"ChromeDriver descargado en: {chromedriver_path}")

    # Configurar el servicio de ChromeDriver
    service = Service(chromedriver_path)

    # Crear la instancia del driver
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver