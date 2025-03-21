from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    # options.add_argument("--headless")  # Descomenta para ejecutar en modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")

    # Usar ChromeDriver preinstalado en la imagen de Docker
    service = Service("/usr/local/bin/chromedriver")

    # Crear la instancia del driver
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver