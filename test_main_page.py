from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        base_page = BasePage(browser, browser.current_url)
        base_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        base_page = BasePage(browser, link)
        base_page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    base_page = BasePage(browser,browser.current_url)
    base_page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_cart_opened_from_main_page()
