from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import pytest

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        CURRENT_URL = self.browser.current_url
        assert "login" in CURRENT_URL, "Current URL does not contain 'Login' substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present (*LoginPageLocators.LOG_IN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present (*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        password_field_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_FIRST).send_keys(password)
        password_field_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_SECOND).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        result_message = self.browser.find_element(*LoginPageLocators.REGISTRATION_MESSAGE)
        result_message_text = result_message.text
        assert result_message_text == "Thanks for registering!", "No message about successful registration"