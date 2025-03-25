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

    # Detección de entorno CI (SOLO para CircleCI)
    is_circleci = os.environ.get('CIRCLECI') == 'true'

    if is_circleci:
        # Configuración EXCLUSIVA para CircleCI
        chromedriver_path = "/usr/local/bin/chromedriver"
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    else:
        # Configuración ORIGINAL para local
        user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={user_data_dir}")
        chromedriver_path = ChromeDriverManager().install()
        
        if platform.system() == 'Windows' and not chromedriver_path.endswith(".exe"):
            chromedriver_path = os.path.join(os.path.dirname(chromedriver_path), "chromedriver.exe")

    print(f"Using ChromeDriver at path: {chromedriver_path}")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver