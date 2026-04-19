from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open_site()
    login.login("standard_user", "secret_sauce")

    assert len(inventory.get_products()) > 0

    inventory.add_first_product()

    assert inventory.get_cart_badge_text() == "1"


def test_cart_badge_updates_after_adding_product(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open_site()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product()

    assert inventory.get_cart_badge_text() == "1"


def test_remove_product_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open_site()
    login.login("standard_user", "secret_sauce")

    # ADD PRODUCT
    inventory.add_first_product()
    assert inventory.get_cart_badge_text() == "1"

    # REMOVE PRODUCT
    inventory.remove_product("Sauce Labs Backpack")

    # ASSERT BADGE DISAPPEARS
    assert inventory.is_cart_badge_displayed() is False

def test_add_multiple_products_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.open_site()
    login.login("standard_user", "secret_sauce")
    inventory.add_multiple_products(2)
    assert inventory.get_cart_badge_text() == "2"

def test_remove_another_product_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.open_site()
    login.login("standard_user", "secret_sauce")
    added = inventory.add_multiple_products(2)
    inventory.remove_product(added[0])
    assert inventory.get_cart_badge_text() == "1"






