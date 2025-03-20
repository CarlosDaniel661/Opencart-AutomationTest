from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product = (By.CSS_SELECTOR, "div.product-layout:first-child")

    def select_first_product(self):
        self.driver.find_element(*self.search_button).click()
        
    def select_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_product)
        ).click()