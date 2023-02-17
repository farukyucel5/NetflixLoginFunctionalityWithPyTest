from selenium.webdriver.common.by import By

from pages.pageBase import PageBase


class LoginPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    signInBtn = (By.XPATH, "//a[text()='Sign In']")
    cookies = (By.XPATH, "//button[text()='Reject']")
    usernameBox = (By.ID, "id_userLoginId")
    passwordBox = (By.XPATH, "//*[@id='id_password']")
    loginBtn = (By.XPATH, "//button[text()='Oturum Aç']")

    def click_sign_in_btn(self):
        self.wait_element_visibility(self.cookies)
        self.driver.find_element(*self.cookies).click()
        self.wait_element_visibility(self.signInBtn)
        self.driver.find_element(*self.signInBtn).click()

    def enter_username(self, username):
        self.driver.find_element(*self.usernameBox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.passwordBox).send_keys(password)

    def click_login_btn(self):
        self.wait_element_visibility(self.loginBtn)
        self.driver.find_element(*self.loginBtn).click()
