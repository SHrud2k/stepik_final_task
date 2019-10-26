from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import allure


@allure.feature("Корзина")
@allure.title("Работа авторизованного юзера с корзиной")
@allure.severity(allure.severity_level.CRITICAL)
class TestUserAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        '''JTREWRTYUILIUIYTRYUIIYKJTHRTG'''
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

        with allure.step("Переход по ссылке " + link):
            page = ProductPage(driver, link)
            page.open()

        with allure.step("Переход на страницу авторизации"):
            page.go_to_login_page()

        with allure.step("Регистрация пользователя"):
            register_page = LoginPage(driver, driver.current_url)
            register_page.setup_user()

        with allure.step("Возврат на главную страницу"):
            page.open()

        with allure.step("Добавление товара в корзину"):
            page.click_on_basket()

        with allure.step("Решение секретного кода"):
            page.solve_quiz_and_get_code()

        with allure.step("Проверка совпадения имен"):
            page.prices_do_match()

        with allure.step("Проверка совпаления цен"):
            page.names_do_match()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(driver, link)
        page.open()
        page.go_to_login_page()
        register_page = LoginPage(driver, driver.current_url)
        register_page.setup_user()
        page.open()
        page.click_on_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.click_on_basket()
    page.solve_quiz_and_get_code()
    page.prices_do_match()
    page.names_do_match()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.click_on_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
    new_page = LoginPage(driver, driver.current_url)
    new_page.should_be_login_form()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.click_on_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_from_button()
    new_page = BasketPage(driver, driver.current_url)
    new_page.is_items_not_present()
    new_page.is_message_present()
