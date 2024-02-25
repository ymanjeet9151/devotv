from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time


class SigninPage(PageObject):
    """
    WebElements and keywords for signinsignupPage.
    """

    _locators = {
        "signin_link_button": "//div[@id='stickyHeader']//a[@class='btn-signup']",
        "signin_page_title": "//title[text()='Sign In']",
        "signin_header_title": "//h6[text()=' Sign In to Stream Ad-Free ']",
        "email_textbox": "//div[contains(@class,'inp-wrapper')]//input[@id='email']",
        "password_textbox": "//form[contains(@class,'login-form ng-pristine')]//input[@id='password']",
        "signin_button": "//div[@class='inp-wrapper']//..//button[text()=' Sign In ']",
        "signup_button": "//form[contains(@class,'ng-pristine ng-invalid')]//button[text()=' Agree & Sign Up ']",
        "vads_agree_signin_button": "//button[text()=' Agree & Sign In ']",
        "vads_agree_signup_button": "//button[text()=' Agree & Sign Up ']",
        "signup_page_title": "//title[text()='Create an Account']",
        "signup_header_title": "//div[@class='vanish-combo-modal']//div[text()='Sign Up to Stream Episode ']",
        "vads_email_textbox_signin": "//div[contains(@class,'signIn')]//input[@id='email']",
        "vads_signin_password": "//div[contains(@class,'signIn')]//input[@id='password']",
        "vads_signup_email_textbox": "//div[contains(@class,'signUp')]//input[@id='email']",
        "vads_signup_password": "//div[contains(@class,'signUp')]//input[@id='password']",
        "signup_email_textbox": "//div[@class='inp-wrapper']//input[@id='email']",
        "signup_password_textbox": "//div[contains(@class,'inp-wrapper')]//input[@id='password']",
        "signup_first_name": "//form[@class='ng-pristine ng-invalid ng-touched']//input[@id='firstname']",
        "signup_last_name": "//form[@class='ng-pristine ng-invalid ng-touched']//input[@id='lastname']",
        "vads_signup_first_name": "//div[contains(@class,'signUp')]//input[@id='firstname']",
        "vads_signup_last_name": "//div[contains(@class,'signUp')]//input[@id='lastname']",
        "create_account_button": "//form[contains(@class,'login-form ng-pristine')]//a[text()='Create Account']",
        "vads_create_account": "//div[contains(@class,'sign-in')]//a[text()='Create Account']",
        "vads_signin_link_to_signin": "//div[text()=' Already have an account? ']//a[contains(text(),'Sign In')]",
        "signin_link_to_signinpage": "//div[@class='create-acc']//a[text()=' Sign In']",
    }

    def _is_current_page(self):
        """This function checks if the user is on the sign-in or sign-up page and returns a boolean value.
        :return: a boolean value, either True or False.
        """
        page_title = verify_element_on_load(self.locator.signin_header_title, time=0)
        signin_button = verify_element_on_load(self.locator.signin_button, time=0)

        if page_title and signin_button is True:
            print("On signin Page")
        else:
            print("signin page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_SigninPage(self):
        """
        this method is validating the user is on SigninPage page or not
        """
        page_title = verify_element_on_load(self.locator.signin_header_title, time=0)
        signin_button = verify_element_on_load(self.locator.signin_button, time=0)

        if (page_title and signin_button) is not True:
            BuiltIn().fail("Incorrect Page")

    def user_click_on_signin_link(self):
        """This function clicks on the "signin" link button.
        """
        verify_element_and_click(self.locator.signin_link_button)

    def enter_user_email(self, email):
        """This function enters a user's email address into the appropriate textbox on a webpage, depending on
        which textbox is displayed.
        : param email: The email address that needs to be entered in the email address textbox
        """
        vads_signin = verify_element_on_load(self.locator.vads_email_textbox_signin, 5)
        vads_signup = verify_element_on_load(self.locator.vads_signup_email_textbox, 5)
        email_signin = verify_element_on_load(self.locator.email_textbox, 5)
        email_signup = verify_element_on_load(self.locator.signup_email_textbox, 5)
        if vads_signin is True:
            self.se2lib.input_text(self._locators["vads_email_textbox_signin"], email)
        elif vads_signup is True:
            self.se2lib.input_text(self._locators["vads_signup_email_textbox"], email)
        elif email_signin is True:
            self.se2lib.input_text(self._locators["email_textbox"], email)
        elif email_signup is True:
            self.se2lib.input_text(self._locators["signup_email_textbox"], email)
        else:
            print("email address textbox is not displayed...")

    def enter_user_password(self, password):
        """This function enters a user's password into the appropriate textbox based on which page element is
        displayed.
        :param password: The password that the user wants to enter in the password textbox
        """
        vads_signin_pass = verify_element_on_load(self.locator.vads_signin_password, 5)
        vads_signup_pass = verify_element_on_load(self.locator.vads_signup_password, 3)
        password_signin = verify_element_on_load(self.locator.password_textbox, 3)
        password_signup = verify_element_on_load(self.locator.signup_password_textbox, 3)
        if vads_signin_pass is True:
            self.se2lib.input_text(self._locators["vads_signin_password"], password)
        elif vads_signup_pass is True:
            self.se2lib.input_text(self._locators["vads_signup_password"], password)
        elif password_signin is True:
            self.se2lib.input_text(self._locators["password_textbox"], password)
        elif password_signup is True:
            self.se2lib.input_text(self._locators["signup_password_textbox"], password)
        else:
            print("password textbox is not displayed...")

    def user_click_on_agree_signin_button(self):
        """This function clicks on either the "agree and signin" button or the regular "signin" button on a
        webpage, depending on which one is present.
        """
        vads_signin_button = verify_element_on_load(self.locator.vads_agree_signin_button, 5)
        signin_button = verify_element_on_load(self.locator.signin_button, 5)
        if vads_signin_button is True:
            self.se2lib.click_element(self._locators["vads_agree_signin_button"])
        elif signin_button is True:
            self.se2lib.click_element(self._locators["signin_button"])
        else:
            print("unable to click on the signin button")

    def user_click_on_create_account_button(self):
        """This function clicks on the "create account" button on a webpage if it is present.
        """
        vads_create_account = verify_element_on_load(self.locator.vads_create_account)
        create_account_button = verify_element_on_load(self.locator.create_account_button)
        if vads_create_account is True:
            self.se2lib.click_element(self._locators["vads_create_account"])
        elif create_account_button is True:
            self.se2lib.click_element(self._locators["create_account_button"])
        else:
            print("unable to click on the create account button")

    def user_click_on_signin_button(self):
        """This function clicks on a sign-in button based on the availability of two different locators.
        """
        vads_signin_link_to_signin = verify_element_on_load(self.locator.vads_signin_link_to_signin, 15)
        # signin_in_page = verify_element_on_load(self.locator.signin_link_to_signinpage)
        if vads_signin_link_to_signin is True:
            Scroll_to_element(self._locators["vads_signin_link_to_signin"], 200)
            self.se2lib.click_element(self._locators["vads_signin_link_to_signin"])
        # elif signin_in_page is True:
        #     self.se2lib.click_element(self._locators["signin_link_to_signinpage"])
        else:
            print("unable to click on the signin link button")
