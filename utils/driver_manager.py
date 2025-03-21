from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import platform

def get_driver():
    options = Options()
    # options.add_argument("--headless")  # Descomenta para ejecutar en modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")

    # Crear un directorio temporal único para los datos del usuario
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # Usar webdriver-manager para instalar ChromeDriver automáticamente
    chromedriver_path = ChromeDriverManager().install()

    # Configurar el servicio de ChromeDriver
    service = Service(chromedriver_path)

    # Crear la instancia del driver
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver