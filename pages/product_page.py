from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators

class ProductPage(BasePage):
    def click_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def add_item_to_basket(self):
        BasePage.solve_quiz_and_get_code(self)

        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_STRONG)
        success_message_text = success_message.text

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text

        assert product_name_text == success_message_text

        price_field = self.browser.find_element(*ProductPageLocators.PRICE_FIELD)
        price_field_text = price_field.text

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text

        assert product_price_text == price_field_text

    def guest_cant_see_success_message_after_adding_product_to_cart(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_STRONG), \
            " First: Success message is presented"

    def guest_cant_see_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_STRONG), \
            "Second:Success message is presented"

    def message_dissapeared_after_adding_product_to_cart(self):
        assert BasePage.is_disappeared(self, *ProductPageLocators.SUCCESS_MESSAGE_STRONG) == True, \
             "Third: Success message is present"

    def guest_can_go_to_login_page_from_product_page(self):
        login_button = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_button.click()

