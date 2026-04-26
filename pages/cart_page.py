from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_elements_present


class CartPage:
	def __init__(self,driver):
		self.driver = driver

		self.OPEN_CART = (By.CLASS_NAME,"shopping_cart_link")
		self.GET_CART_ITEMS =(By.CLASS_NAME,"cart_item")
		self.FIRST_CART_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")
		self.CLICK_CHECKOUT = (By.ID,"checkout")

	def open_cart(self):
		self.driver.find_element(*self.OPEN_CART).click()

	def get_cart_items(self):
		return wait_for_elements_present(self.driver, self.GET_CART_ITEMS)

	def first_cart_item_name(self):
		return self.driver.find_elements(*self.FIRST_CART_ITEM_NAME)[0].text

	def remove_product_from_cart_page(self, product_name):
		slug = product_name.lower().replace(" ", "-")
		self.driver.find_element(By.ID, f"remove-{slug}").click()

	def click_checkout(self):
		self.driver.find_element(*self.CLICK_CHECKOUT).click()