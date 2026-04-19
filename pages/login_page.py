from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.USERNAME = (By.ID, "user-name")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BTN = (By.ID, "login-button")
        self.ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open_site(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR).text