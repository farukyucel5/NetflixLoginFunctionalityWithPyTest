import pytest

from pages.login import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginFunctionality:

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.click_sign_in_btn()
        login_page.enter_username("frk@gmail.com")
        login_page.enter_password("123456")
        login_page.click_login_btn()







