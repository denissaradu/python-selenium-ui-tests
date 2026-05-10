from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
	def __init__(self,driver):
		self.driver = driver

		self.FIRST_NAME_INPUT = (By.ID,"first-name")
		self.LAST_NAME_INPUT = (By.ID,"last-name")
		self.POSTAL_CODE_INPUT = (By.ID,"postal-code")
		self.CONTINUE_BUTTON = (By.ID,"continue")
		self.ERROR_MESSAGE =(By.CSS_SELECTOR,"h3[data-test='error']")

	def fill_first_name(self,first_name):
		self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

	def fill_last_name(self,last_name):
		self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

	def fill_postal_code(self,postal_code):
		self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

	def click_continue(self):
		self.driver.find_element(*self.CONTINUE_BUTTON).click()

	def get_error_message(self):
		return self.driver.find_element(*self.ERROR_MESSAGE).text

