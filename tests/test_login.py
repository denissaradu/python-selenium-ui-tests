from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username,password,expected_result",
                         [
                        ("standard_user","secret_sauce","succes"),
                        ("wrong_user","wrong_password","error"),
                        ("locked_out_user", "secret_sauce", "locked")
                         ])

def test_login(driver,username,password,expected_result):
    login = LoginPage(driver)
    login.open_site()
    login.login(username, password)
    if expected_result == "succes":
        assert "inventory.html" in driver.current_url
    elif expected_result == "error":
        assert "Epic sadface" in login.get_error_message()
    elif expected_result == "locked":
        assert "locked out" in login.get_error_message()