from pages.login_page import LoginPage

def test_login_valid(driver):
    login = LoginPage(driver)

    login.open_site()
    login.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_login_invalid(driver):
    login = LoginPage(driver)

    login.open_site()
    login.login("wrong_user", "wrong_pass")

    assert "Epic sadface" in login.get_error_message()
