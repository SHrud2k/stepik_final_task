from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(driver, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(driver, link)
    page.open()
    page.click_on_basket()
    page.solve_quiz_and_get_code()
    page.prices_do_match()
    page.names_do_match()
