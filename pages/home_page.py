from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn-default")

    def open(self):
        self.driver.get("http://opencart.abstracta.us/")

    def search_product(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_box)
        ).clear()  
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_box)
        ).send_keys(product_name)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()
