from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "cart")
        self.view_cart_link = (By.LINK_TEXT, "View Cart")  
        self.cart_dropdown = (By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[1]/strong")  
        self.cart_items = (By.CSS_SELECTOR, "table.table tbody tr")
        self.remove_button = (By.CSS_SELECTOR, "button.btn-danger:nth-child(2)")

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_dropdown)
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_cart_link)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive"))
        )

    def is_cart_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive"))
            )
            return True
        except TimeoutException:
            print("Error: La página del carrito no se cargó correctamente.")
            return False

    def is_product_in_cart(self, product_name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive"))
            )

            empty_cart_message = self.driver.find_elements(By.XPATH, "//p[contains(text(), 'Your shopping cart is empty!')]")
            if empty_cart_message:
                return False

            items = self.driver.find_elements(*self.cart_items)
            for item in items:
                if product_name in item.text:
                    return True
            return False

        except TimeoutException:
            print("Error: No se pudo cargar la página del carrito.")
            return False
        
    def remove_product(self):
        try:
            remove_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.remove_button)
        )

            self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
            remove_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.table-responsive tbody tr"))
        )

        except TimeoutException:
            print("Error: No se encontró el botón de eliminar en el tiempo esperado.")
        except Exception as e:
            print(f"Error inesperado: {e}")