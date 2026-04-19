from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_added_product_visible_in_cart(driver):
	login = LoginPage(driver)
	inventory = InventoryPage(driver)
	cart_page = CartPage(driver)

	login.open_site()
	login.login("standard_user", "secret_sauce")

	inventory.add_first_product()
	cart_page.open_cart()

	items = cart_page.get_cart_items()

	assert len(items) == 1
	assert cart_page.first_cart_item_name() == "Sauce Labs Backpack"