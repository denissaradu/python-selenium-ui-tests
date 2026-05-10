from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_elements_present
from utils.wait_utils import wait_for_element_clickable
from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        self.PRODUCTS = (By.CLASS_NAME, "inventory_item")
        self.ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")
        self.CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
        self.OPEN_MENU = (By.ID,"react-burger-menu-btn")
        self.CLICK_LOGOUT =(By.ID, "logout_sidebar_link")
        self.SORT_OPTION =(By.CLASS_NAME, "product_sort_container")
        self.PRICES =(By.CLASS_NAME, "inventory_item_price")

    def get_products(self):
        return self.driver.find_elements(*self.PRODUCTS)

    def add_first_product(self):
        wait_for_elements_present(self.driver, self.PRODUCTS)
        products = self.get_products()
        products[0].find_element(*self.ADD_TO_CART).click()

    def remove_product(self, product_name):
        products = self.get_products()

        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

            if name == product_name:
                product.find_element(By.ID, f"remove-{product_name.lower().replace(' ', '-')}").click()
                break

    def get_cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def is_cart_badge_displayed(self):
        return len(self.driver.find_elements(*self.CART_BADGE)) > 0

    def add_multiple_products(self,n):
        products = self.get_products()
        added_products =[]

        for i in range(n):
            name = products[i].find_element(By.CLASS_NAME, "inventory_item_name").text
            products[i].find_element(*self.ADD_TO_CART).click()
            added_products.append(name)

        return added_products


    def open_menu(self):
        self.driver.find_element(*self.OPEN_MENU).click()


    def click_logout(self):
        wait_for_element_clickable(self.driver, self.CLICK_LOGOUT).click()

    def select_sort_option(self, option_value):
        sort_dropdown = wait_for_element_clickable(self.driver, self.SORT_OPTION)
        Select(sort_dropdown).select_by_value(option_value)


    def get_product_prices(self):
        products = wait_for_elements_present(self.driver, self.PRODUCTS)
        prices = []

        for product in products:
            price = float(
                product.find_element(By.CLASS_NAME, "inventory_item_price")
                .text.replace("$", "")
            )
            prices.append(price)

        return prices





