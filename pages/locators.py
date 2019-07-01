from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CART = (By.XPATH, "//a[text()='View basket']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators(object):
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD_FIRST = (By.NAME, "registration-password1")
    PASSWORD_FIELD_SECOND = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE_STRONG = (By.CSS_SELECTOR, ".alert-success strong")
    PRICE_FIELD = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CART = (By.XPATH, "//a[text()='View basket']")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")