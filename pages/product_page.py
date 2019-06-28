from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

        BasePage.solve_quiz_and_get_code(self)

        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_STRONG)
        success_message_text = success_message.text

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text

        assert product_name_text == success_message_text

        price_field = self.browser.find_element(*ProductPageLocators.PRICE_FIELD)
        price_field_text = price_field.text

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print(product_price)
        product_price_text = product_price.text

        assert product_price_text == price_field_text