from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_remove_product_from_cart_page(driver):
	login = LoginPage(driver)
	inventory = InventoryPage(driver)
	cart_page = CartPage(driver)

	login.open_site()
	login.login("standard_user", "secret_sauce")

	inventory.add_first_product()
	cart_page.open_cart()
	assert len(cart_page.get_cart_items()) == 1
	cart_page.remove_product_from_cart_page("Sauce Labs Backpack")

	assert len(cart_page.get_cart_items()) == 0

