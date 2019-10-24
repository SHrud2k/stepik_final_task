from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def setup_user(self):
        self.register_new_user(f'{str(time.time())}@gmail.com', str(time.time()))
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESSFUL), "Registration was not completed"
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.driver.current_url
        assert "login" in current_link, "Current page is not Login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def value_input(self, what, how, where):
        self.wait_for(how, what)
        self.driver.find_element(how, where).send_keys(what)

    def register_new_user(self, email, password):
        self.value_input(email, *LoginPageLocators.REGISTER_EMAIL)
        self.value_input(password, *LoginPageLocators.REGISTER_PASSWORD)
        self.value_input(password, *LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
