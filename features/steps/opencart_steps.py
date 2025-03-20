from behave import given, when, then
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from automation_opencart.utils.driver_manager import get_driver
import time

@given('Me encuentro en el HomePage de OpenCart {url}')
def step_impl(context, url):
    context.driver = get_driver()
    context.home_page = HomePage(context.driver)
    context.home_page.open()
    time.sleep(2)  # Espera breve para evitar fallos de carga

@when('Busco un "{product}" en el search box')
def step_impl(context, product):
    context.home_page.search_product(product)
    context.search_results_page = SearchResultsPage(context.driver)

@when('Selecciono el primer resultado')
def step_impl(context):
    context.search_results_page = SearchResultsPage(context.driver)
    context.search_results_page.select_first_product()
    context.product_page = ProductPage(context.driver)

@when('Agrego el producto al carrito')
def step_impl(context):
    context.product_page.add_to_cart()

@when('Abro el carrito')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.open_cart()

@then('Debería ver el "{product}" seleccionado en el carrito')
def step_impl(context, product):
    assert context.cart_page.is_product_in_cart(product), f'El producto {product} no se encuentra en el carrito'

@then('Elimino el producto del carrito')
def step_impl(context):
    context.cart_page.remove_product()

@then('El "{product}" ya no debería estar en el carrito')
def step_impl(context, product):
    assert not context.cart_page.is_product_in_cart(product), f'El producto {product} aún está en el carrito'
