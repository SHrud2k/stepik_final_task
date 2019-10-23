from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def click_on_basket(self):
        try:
            self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        except (NoSuchElementException):
            return False

    def prices_do_match(self):
        price_to_be = self.driver.find_element(*ProductPageLocators.PRICE_EXPECTED).text
        price_actual = self.driver.find_element(*ProductPageLocators.PRICE_GOT).text
        assert price_actual == price_to_be, "Prices does not match"

    def names_do_match(self):
        name_to_be = self.driver.find_element(*ProductPageLocators.ITEM_NAME_EXPECTED).text
        name_actual = self.driver.find_element(*ProductPageLocators.ITEM_NAME_GOT).text
        assert name_actual == name_to_be, "Names does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Should disappear but did not"

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
