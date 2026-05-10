from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_open_menu_logout(driver):
	login = LoginPage(driver)
	inventory = InventoryPage(driver)

	login.open_site()
	login.login("standard_user", "secret_sauce")
	assert "inventory.html" in driver.current_url

	inventory.open_menu()
	inventory.click_logout()
	assert driver.current_url == "https://www.saucedemo.com/"