from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:
	def __init__(self,driver):
		self.driver = driver

		self.FINISH_BUTTON = (By.ID,"finish")
		self.CANCEL_BUTTON = (By.ID,"cancel")
		self.SUMMARY_CONTAINER = (By.ID,"checkout_summary_container")

	def click_finish(self):
		self.driver.find_element(*self.FINISH_BUTTON).click()

	def click_cancel(self):
		self.driver.find_element(*self.CANCEL_BUTTON).click()

	def get_success_message(self):
		return self.driver.find_element(By.CLASS_NAME,"complete-header").text
