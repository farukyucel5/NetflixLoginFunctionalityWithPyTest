import pytest
import unittest

from ddt import data, unpack, ddt

from Utilities.ExcelHelper import ExcelClass
from pages.login import LoginPage


@pytest.mark.usefixtures("setup")
@ddt
class TestLoginFunctionality(unittest.TestCase):

    @data(*ExcelClass.excel_listeler_listesine_cevir("testData/User_info.xlsx", "UserEmailAndPassword"))
    @unpack
    def test_negative_login_with_Wrong_User_Information(self, username, password):
        if "@gmail" in username and len(password) < 4 and password != "":
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_password_field_error().text == "Parolanız 4 ila 60 karakter olmalıdır."

        if "@gmail" in username and len(password) >= 4:
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_wrong_password().text == "Parola yanlış."

        if "@gmail" not in username and username != "" and len(password) >= 4:
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_username_error().text == "Bu e‑posta adresi ile bağlantılı bir hesap bulamadık." \
                                                             " Lütfen yeniden deneyin ya da yeni bir hesap oluşturun."

        if "@gmail" in username and password == "":
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()

            assert login_page.check_password_field_error().text == "Parolanız 4 ila 60 karakter olmalıdır."

        if username == "" and len(password) >= 4:
            login_page = LoginPage(self.driver)
            self.driver.get("https://www.netflix.com/tr/")
            login_page.click_sign_in_btn()
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_btn()
            assert login_page.check_username_field_error().text == "Lütfen geçerli bir telefon numarası veya e‑posta " \
                                                                   "adresi girin."

