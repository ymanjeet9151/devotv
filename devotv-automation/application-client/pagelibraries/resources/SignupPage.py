from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time


class SignupPage(PageObject):
    """WebElements and keywords for signinsignupPage.
    """
    _locators = {
        "signin_link_button": "//div[@id='stickyHeader']//a[@class='btn-signup']",
        "signin_page_title": "//title[text()='Sign In']",
        "signin_header_title": "//div[@class='vanish-combo-modal']//div[text()='Sign In to Stream Episode ']",
        "email_textbox": "//form[contains(@class,'login-form ng-pristine')]//input[@id='email']",
        "password_textbox": "//form[contains(@class,'login-form ng-pristine')]//input[@id='password']",
        "signin_button": "//form[contains(@class,'login-form ng-pristine')]//button[text()=' Sign In ']",
        "signup_button": "//form[contains(@class,'ng-pristine ng-invalid')]//button[text()=' Agree & Sign Up ']",
        "vads_agree_signin_button": "//button[text()=' Agree & Sign In ']",
        "vads_agree_signup_button": "//button[text()=' Agree & Sign Up ']",
        "signup_page_title": "//title[text()='Create an Account']",
        "signup_header_title": "//h6[text()=' Sign Up to Stream Ad-Free ']",
        "vads_email_textbox_signin": "//div[contains(@class,'signIn')]//input[@id='email']",
        "vads_signin_password": "//div[contains(@class,'signIn')]//input[@id='password']",
        "vads_signup_email_textbox": "//div[contains(@class,'signUp')]//input[@id='email']",
        "vads_signup_password": "//div[contains(@class,'signUp')]//input[@id='password']",
        "signup_email_textbox": "//div[@class='inp-wrapper']//input[@id='email']",
        "signup_password_textbox": "//div[contains(@class,'inp-wrapper')]//input[@id='password']",
        "signup_first_name": "//input[@id='firstname']",
        "signup_last_name": "//input[@id='lastname']",
        "vads_signup_first_name": "//div[contains(@class,'signUp')]//input[@id='firstname']",
        "vads_signup_last_name": "//div[contains(@class,'signUp')]//input[@id='lastname']",
        "create_account_button": "//form[contains(@class,'login-form ng-pristine')]//a[text()='Create Account']",
        "vads_create_account": "//div[contains(@class,'sign-in')]//a[text()='Create Account']",
        "vads_signin_link_to_signin": "//div[@class='sign-in']//a[text()='Sign In']",
        "signin_link_to_signinpage": "//div[@class='create-acc']//a[text()=' Sign In']",

    }

    def _is_current_page(self):
        """
        This function checks if the user is on the sign-in or sign-up page and returns a boolean value.
        :return: a boolean value, either True or False.
        """
        signup_button = verify_element_on_load(self.locator.signup_button, time=0)
        signup_title = verify_element_on_load(self.locator.signup_header_title, time=0)

        if signup_button and signup_title is True:
            print("On Signup Page")
        else:
            print("signup page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_SignupPage(self):
        """
        this method is validating the user is on SignupPage page or not
        """
        signup_button = verify_element_on_load(self.locator.signup_button, time=0)
        signup_title = verify_element_on_load(self.locator.signup_header_title, time=0)

        if signup_button and signup_title is False:
            BuiltIn().fail("Incorrect Page")

    def user_enter_firstName_for_signup(self, first_name):
        """
        This function inputs the user's first name for signup if the element is found, otherwise it prints
        an error message.
        :param first_name: The first name that the user wants to enter for signing up
        """
        vads_signup_first_name = verify_element_on_load(self.locator.vads_signup_first_name)
        signup_first_name = verify_element_on_load(self.locator.signup_first_name)
        if vads_signup_first_name is True:
            self.se2lib.input_text(self._locators["vads_signup_first_name"], first_name)
        elif signup_first_name is True:
            self.se2lib.input_text(self._locators["signup_first_name"], first_name)
        else:
            print("unable to enter first name")

    def user_enter_lastName_for_signup(self, last_name):
        """
        This function inputs the user's last name during the signup process, checking for two different
        element locators.
        :param last_name: The last name that the user wants to enter for the signup process
        """
        vads_signup_last_name = verify_element_on_load(self.locator.vads_signup_last_name)
        signup_last_name = verify_element_on_load(self.locator.signup_last_name)
        if vads_signup_last_name is True:
            self.se2lib.input_text(self._locators["vads_signup_last_name"], last_name)
        elif signup_last_name is True:
            self.se2lib.input_text(self._locators["signup_last_name"], last_name)
        else:
            print("unable to enter last name")

    def user_clik_on_agree_signup_button(self):
        """The function clicks on a signup button if it is present on the page.
        """
        vads_signup_button = verify_element_on_load(self.locator.vads_agree_signup_button)
        signup_button = verify_element_on_load(self.locator.signup_button)
        if vads_signup_button is True:
            Scroll_to_element(self.locator.vads_agree_signup_button, 200)
            verify_element_and_click(self.locator.vads_agree_signup_button)
        elif signup_button is True:
            Scroll_to_element(self.locator.signup_button, 200)
            verify_element_and_click(self.locator.signup_button)
        else:
            print("unable to click on the signup button")
