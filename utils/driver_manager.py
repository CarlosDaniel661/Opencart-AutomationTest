from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import platform
import tempfile

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--remote-debugging-port=9222")


    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    if platform.system() == 'Linux':
        chromedriver_path = "/usr/bin/chromedriver"
    elif platform.system() == 'Windows':
        chromedriver_path = ChromeDriverManager().install()
       
        if not chromedriver_path.endswith("chromedriver.exe"):
            chromedriver_path = os.path.join(os.path.dirname(chromedriver_path), "chromedriver.exe")
    else:
        raise Exception("Sistema operativo no soportado para WebDriver")

    if not os.path.isfile(chromedriver_path):
        raise Exception(f"Chromedriver no se ha encontrado en la ruta especificada: {chromedriver_path}")

    print(f"Using ChromeDriver at path: {chromedriver_path}")

    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    return driver
