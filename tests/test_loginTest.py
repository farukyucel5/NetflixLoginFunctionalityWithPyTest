import pytest
import unittest

from ddt import data, unpack, ddt

from pages.login import LoginPage


@pytest.mark.usefixtures("setup")
@ddt
class TestLoginFunctionality(unittest.TestCase):

    @data(("ab", "abc"),("aws","qwe"),("asd", "asd"))
    @unpack
    def test_login(self,username,password):
        login_page = LoginPage(self.driver)
        self.driver.get("https://www.netflix.com/tr-en/")
        login_page.click_sign_in_btn()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_btn()
