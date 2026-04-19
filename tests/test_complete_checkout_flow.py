from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage

def test_complet_checkout_flow(driver):
	login = LoginPage(driver)
	inventory = InventoryPage(driver)
	cart_page = CartPage(driver)
	checkoutone = CheckoutStepOnePage(driver)
	checkouttwo = CheckoutStepTwoPage(driver)

	login.open_site()
	login.login("standard_user", "secret_sauce")

	inventory.add_first_product()
	cart_page.open_cart()
	assert len(cart_page.get_cart_items()) == 1

	cart_page.click_checkout()

	assert "checkout-step-one" in driver.current_url

	checkoutone.fill_first_name("Denisa")
	checkoutone.fill_last_name("Radu")
	checkoutone.fill_postal_code("077190")
	checkoutone.click_continue()

	assert "checkout-step-two" in driver.current_url

	checkouttwo.click_finish()
	assert "Thank you for your order!" in checkouttwo.get_success_message()



