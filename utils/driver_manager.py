from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import platform
import shutil
import os

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    cache_dir = os.path.expanduser("~/.wdm")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print(f"Eliminada la caché de webdriver-manager en: {cache_dir}")

    # Usar webdriver-manager para instalar ChromeDriver automáticamente
    chromedriver_path = ChromeDriverManager().install()
    print(f"ChromeDriver descargado en: {chromedriver_path}")  # Imprimir la ruta

    os.chmod(chromedriver_path, stat.S_IRWXU)
    print(f"Permisos de ejecución dados a: {chromedriver_path}")

    # Configurar el servicio de ChromeDriver
    service = Service(chromedriver_path)

    # Crear la instancia del driver
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver