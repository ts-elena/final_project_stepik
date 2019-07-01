from .base_page import BasePage
from .locators import BasePageLocators
import time

class MainPage(BasePage):
        def guest_cant_see_product_in_cart_opened_from_main_page(self):
            cart_button = self.browser.find_element(*BasePageLocators.CART)
            cart_button.click()
            cart_message =  self.browser.find_element(*BasePageLocators.EMPTY_CART_MESSAGE)
            cart_message_text = cart_message.text
            assert cart_message_text == "Your basket is empty. Continue shopping"