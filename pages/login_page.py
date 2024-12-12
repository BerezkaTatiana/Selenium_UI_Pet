from .base_page import BasePage
from .locators import LoginPageLocators
from config import LOGIN_POSITIVE, LOGIN_NEGATIVE, PASSWORD_POSITIVE, PASSWORD_NEGATIVE


class LoginPage(BasePage):
    def go_to_login_positive(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LOGIN_POSITIVE)

    def go_to_login_negative(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LOGIN_NEGATIVE)

    def go_to_password_positive(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(PASSWORD_POSITIVE)

    def go_to_password_negative(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(PASSWORD_NEGATIVE)

    def go_to_submit(self):
        login_submit = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_submit.submit()
