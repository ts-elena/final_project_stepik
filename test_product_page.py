from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time

class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "QwERTY1!!!"
        login_page = LoginPage(browser, link)
        login_page.register_new_user(email, password)
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.parametrize('link',
                                 ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_button()
        page.add_item_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_go_to_login_page_from_product_page()
