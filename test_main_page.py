from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest


class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_from_button()
    new_page = BasketPage(driver, driver.current_url)
    new_page.is_items_not_present()
    new_page.is_message_present()

