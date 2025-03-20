from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.CSS_SELECTOR, "#button-cart")

    def add_to_cart(self):
        try:
            self.driver.save_screenshot("product_page.png")
            
            print("Esperando a que el botón 'Add to Cart' esté presente...")
            WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(self.add_to_cart_button)
            )
            print("El botón 'Add to Cart' está presente en la página.")

            print("Esperando a que el botón 'Add to Cart' sea clickeable...")
            WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.add_to_cart_button)
            ).click()
            print("Se hizo clic en el botón 'Add to Cart'.")
            
        except Exception as e:
            
            self.driver.save_screenshot("error_add_to_cart.png")
            print(f"Error al hacer clic en 'Add to Cart': {e}")
            raise