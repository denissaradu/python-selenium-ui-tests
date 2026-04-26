from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator))

def wait_for_elements_present(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))

def wait_for_element_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))