from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    ITEM_NAME_EXPECTED = (By.CSS_SELECTOR, "#content_inner  h1")
    ITEM_NAME_GOT = (By.CSS_SELECTOR, "#messages div:nth-child(1) > div > strong")
    PRICE_EXPECTED = (By.CSS_SELECTOR, "#content_inner  p.price_color")
    PRICE_GOT = (By.CSS_SELECTOR, "#messages p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
