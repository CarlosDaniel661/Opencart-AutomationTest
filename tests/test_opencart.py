import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.driver_manager import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_opencart_flow(driver):
    screenshots_folder = 'screenshots'
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)

    print(f"Directorio actual: {os.getcwd()}")

    # Consigna 1: Abrir la página de OpenCart
    screenshot_path = os.path.join(screenshots_folder, "captura1_home_page.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    home_page = HomePage(driver)
    home_page.open()

    # Consigna 2: Buscar el iPhone
    screenshot_path = os.path.join(screenshots_folder, "captura2_search_product.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    home_page.search_product("iPhone")

    # Consigna 3: Seleccionar el primer resultado
    screenshot_path = os.path.join(screenshots_folder, "captura3_select_product.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    search_results_page = SearchResultsPage(driver)
    search_results_page.select_first_product()

    # Consigna 4: Agregar el producto al carrito
    screenshot_path = os.path.join(screenshots_folder, "captura4_add_to_cart.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    product_page = ProductPage(driver)
    product_page.add_to_cart()

    # Consigna 5: Abrir el carrito
    screenshot_path = os.path.join(screenshots_folder, "captura5_open_cart.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    cart_page = CartPage(driver)
    cart_page.open_cart()

    # Consigna 6: Validar que la página del carrito se cargó correctamente
    assert cart_page.is_cart_page_loaded(), "La página del carrito no se cargó correctamente"
    screenshot_path = os.path.join(screenshots_folder, "captura6_cart_page_loaded.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)

    # Consigna 7: Verificar que el producto esté en el carrito
    screenshot_path = os.path.join(screenshots_folder, "captura7_producto_en_carrito.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    assert cart_page.is_product_in_cart("iPhone"), "No se encuentra el producto en el carrito"

    # Consigna 8: Eliminar el producto del carrito
    screenshot_path = os.path.join(screenshots_folder, "captura8_producto_eliminado.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    cart_page.remove_product()

    # Consigna 9: Verificar que el iPhone ya no está en el carrito
    screenshot_path = os.path.join(screenshots_folder, "captura9_carrito_vacio.png")
    print(f"Guardando captura en: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    assert not cart_page.is_product_in_cart("iPhone"), "El producto todavía está en el carrito"