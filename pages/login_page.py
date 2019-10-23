from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.driver.current_url()
        assert current_link == "http://selenium1py.pythonanywhere.com/ru/accounts/login/",\
            "Current page is not Login page"

    def should_be_login_form(self):
        assert self.is_element_present(self, *LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(self, *LoginPageLocators.REGISTER_FORM), "Register form is not present"