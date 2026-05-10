from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sort_prices(driver):
	login = LoginPage(driver)
	inventory = InventoryPage(driver)

	login.open_site()
	login.login("standard_user","secret_sauce")

	inventory.select_sort_option("lohi")
	prices = inventory.get_product_prices()
	assert prices == sorted(prices)