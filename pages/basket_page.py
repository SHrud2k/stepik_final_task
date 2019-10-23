from .base_page import BasePage
from .base_page import BasePageLocators


class BasketPage(BasePage):

    def is_items_not_present(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
            "Basket is not empty by default"

    def is_message_present(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), "Basker message is not present"
