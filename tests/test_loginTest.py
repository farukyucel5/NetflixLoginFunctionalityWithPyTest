import pytest
import unittest

from ddt import data, unpack, ddt

from pages.login import LoginPage


@pytest.mark.usefixtures("setup")
@ddt
class TestLoginFunctionality(unittest.TestCase):

    @data(("ab@gmail.com", "123"), ("aws@gmail.com", "q"), ("asd@gmail.com", "as"),("asd@gmail.com", "as125"))
    @unpack
    def test_login(self, username, password):
        if "@" in username and len(password) < 4:
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr-en/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_password_field_error().text == "Parolanız 4 ila 60 karakter olmalıdır."

        if "@" in username and len(password) >= 4:
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr-en/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_wrong_password().text == "Parola yanlış."
