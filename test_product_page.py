from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_go_to_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_button()
    page.add_item_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


