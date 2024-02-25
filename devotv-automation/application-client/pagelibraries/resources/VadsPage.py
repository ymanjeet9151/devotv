from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time


class VadsPage(PageObject):

    """WebElements and keywords for VadsPage.
    """
    _locators = {

        "Vads_SignIn_header_text": "//div[contains(text(),'Sign In to Stream')]",
        "Vads_SignUp_header_text": "//*[contains(text(),'Sign Up to Stream')]",
        "agree_signin_button": "//button[text()=' Agree & Sign In ']",
        "email_textbox_signin": "//div[contains(@class,'signIn')]//input[@id='email']",
        "password_textbox_signin": "//div[contains(@class,'signIn')]//input[@id='password']",
        "agree_signup_button": "//button[text()=' Agree & Sign Up ']",
        "no_iwant_commercials": "//a[text()='No, I want commercials']",
        "brads_makes_vanish_24hr": "//div[text()=' Brands make ads vanish for 24 hours! ']",
        "yes_makes_ads_vanish": "//button[text()=' Yes, Make Ads Vanish  ']",
        "signin_button": "//div[@class='sign-in']//a[text()='Sign In']",
        "signup_email_textbox": "//div[contains(@class,'signUp')]//input[@id='email']",
        "signup_passoword_textbox": "//div[contains(@class,'signUp')]//input[@id='password']",
        "signup_first_name": "//div[contains(@class,'signUp')]//input[@id='firstname']",
        "signup_last_name": "//div[contains(@class,'signUp')]//input[@id='lastname']",
        "email_already_in_use": "//span[contains(text(),' This email address is already in use')]",
        "text_sign_in": "//div[contains(@class,'sign-in')]//a[text()='Sign In']",
        "text_sign_up": "//div[contains(@class,'sign-in')]//a[text()='Create Account']",
        "bottom_card_container": "(//div[contains(@class,'row show-bundle-row profile-project-bundle')]/descendant::div[@class='show-col'])",
        "bottom_card_list": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]//div[@class='show-col']//figure//img",
        "text_popup_title": "//div[@class='heading d-flex flex-md-column']",
        "valid_email_address_error": "//div[@class='error-msg']",
        "user_profile_pic": "//div[@class='avtar-ico']//li[contains(@class,'profile-image position')][1]",
        "Home_carousel_section": "//div[@class='p-carousel-items-content']",
        "devotv_text": "//div[@class='devotvd-logo']",
        "carousal_play_button_locator0": "//div[contains(@class,'p-carousel-items-container')]/div[2]//figure[@class='featured-project-image']/img",
        "carousal_play_button_locator1": "//div[contains(@class,'p-carousel-items-container')]/div[3]//figure[@class='featured-project-image']/img",
        "carousal_play_button_locator2": "//div[contains(@class,'p-carousel-items-container')]/div[4]//figure[@class='featured-project-image']/img",
        "noThanks_commericials": "//a[contains(text(),'No thanks')]",
        "carousal_flex0": "//ul[@class='p-carousel-indicators p-reset']/li[1]/button",
        "carousal_flex1": "//ul[@class='p-carousel-indicators p-reset']/li[2]/button",
        "carousal_flex2": "//ul[@class='p-carousel-indicators p-reset']/li[3]/button",
        "signin_facebook_button": "//div[contains(@class,'signIn')]/../..//button[@class='facebook d-flex']",
        "signup_facebook_button": "//div[contains(@class,'signUp')]/../..//button[@class='facebook d-flex']",
        "signup_fb_button": "//button[@class='fb-btn']",
        "vads_signin_apple_button": "//div[contains(@class,'signIn')]//../..//button[@class='apple d-flex']",
        "vads_signin_google_button": "//button[@class='google google-btn d-flex']//..",
        "vads_signup_google_button": "//button[@class='google google-btn d-flex']//..",
        "signin_google_link": "//form[contains(@class,'ng-pristine ng-invalid')]/../..//div[@class='login-buttons']//div[@id='buttonDivLogin']",
        "signup_google_link": "//form[contains(@class,'ng-pristine ng-invalid')]/../..//div[@class='login-buttons']//div[@id='buttonDivSignUp']",
        "google_input_username": "//input[@id='identifierId']",
        "google_input_password": "//input[@type='password']",
        "google_next_button": "//span[text()='Next']",
        "horror_carousel_playbutton": "//div[@class='p-carousel-items-content']//div[2]//div[@class='play-btn']/../..//img[@title='Ghost Dimension']",
        "scifi_carousel_playbutton": "//div[@class='p-carousel-items-content']//div[2]//div[@class='play-btn']/../..//img[@title='Firefly']",
        "fantasy_carousel_playbutton": "//div[@class='p-carousel-items-content']//div[2]//div[@class='play-btn']/../..//img[contains(@title,'A Twist in the Tale')]",
        "facebook_username": "//input[@name='email']",
        "facebook_password": "//input[@name='pass']",
        "facebook_login_button": "//button[@name='login']",
        "facebook_continue": "//button[@value='Continue']",
        "login_popup_close_btn": "//div[@class='vanish-combo-modal']//button[@class='close']",
        "already_have_an_account": "//div[@class='create-acc']//a[text()=' Sign In']",
        "input_user_name_homePage": "//form[contains(@class,'login-form')]//input[@id='email']",
        "input_password_homePage": "//form[contains(@class,'login-form')]//input[@id='password']",
        "button_signin_homePage": "//button[text()=' Sign In ']",
        "google_create_account_button": "//span[text()='Create account']",
        "google_personal_use": "//span[text()='For my personal use']",
        "google_first_name": "//input[@name='firstName']",
        "google_last_name": "//input[@name='lastName']",
        "google_user_name": "//input[@name='Username']",
        "google_user_password": "//input[@name='Passwd']",
        "google_confirm_password": "//input[@name='ConfirmPasswd']",
        "google_signup_month": "//select[@id='month']/option[text()='January']",
        "google_signup_day": "//input[@id='day']",
        "google_signup_year": "//input[@id='year']",
        "google_signup_gender": "//select[@id='gender']/option[text()='Male']",
        "span_Iagree": "//span[text()='I agree']",
        "goolge_signup_mobile_number": "//input[@id='phoneNumberId']",
        "vanish_ad_btn": "//div[@class='vanishing-container']//button[text()=' Yes, Make Ads Vanish  ']",
        "vanish_ad_title": "//div[@class='vanishing-container']//h4",
        "refuse_vanishing_ads": "//div[@class='vanishing-container']//div[@class ='not-required']",
        "right_top_profile_button": "//div[@class='avtar-ico']//ul",
        "sign_out_button": "//a[text()='Sign Out']",
        "signin_tab": "//div[@id='stickyHeader']//a[@class='btn-signup']",
        "hedder_title_SignIn_Stream_Episode": "//div[text()='Sign In to Stream Episode ']",
        "SignIn_to_Stream": "//div[text()='Sign In to Stream Ad-Free']",
        "action_page_signin_popup_title": "//h6[contains(text(),'Sign Up to Add Shows to Your Watchlist')]",
        "action_page_signin_popup_title2": "//h6[contains(text(),'Sign Up to Like This Show')]",
        "action_page_signin_popup_title3": "//h6[contains(text(),'Sign Up to Cheer For This Comment')]",
        "image_path": "//div[@class='p-carousel-items-container']/div[2]//figure[@class='featured-project-image']/img/../../div[@class='play-btn']//a//*[name()='svg']",
        "header": "//h2[text()=' Stream Free TV ']"
    }

    def _is_current_page(self):
        """
        The function checks if the user is on a vanishing ads page and returns True if they are, False
        otherwise.
        :return: a boolean value, either True or False.
        """
        vads_signin_text = verify_element_on_load(self.locator.Vads_SignIn_header_text, 15)
        vads_signup_text = verify_element_on_load(self.locator.Vads_SignUp_header_text, 5)
        sign_in_button = verify_element_on_load(self.locator.agree_signin_button, 5)
        signup_button = verify_element_on_load(self.locator.agree_signup_button, 5)
        commercials = verify_element_on_load(self.locator.no_iwant_commercials, 5)

        if vads_signin_text and sign_in_button is True:
            print("signin popup displayed")
        elif vads_signup_text and signup_button is True:
            print("signup popup displayed")
        elif commercials is True:
            print("user is already signed in , Popup was displayed")
        else:
            print("user is not on a vanishing adds page")
            return False
        return True

    def check_VadsPage(self):
        """
        This function checks if a certain element exists on a webpage and returns a boolean value based on
        whether or not the element exists.
        :return: a boolean value. It returns True if the "vanish_ad_title" and "vanish_ad_btn" elements are
        present on the page and the text "Stream Free Episode" is found in the "vanish_ad_title" element.
        Otherwise, it returns False.
        """
        if verify_element(self._locators["vanish_ad_title"]) and verify_element(self._locators["vanish_ad_btn"]):
            subscription_title = self.se2lib.get_text(self._locators["vanish_ad_title"])
            return "Stream Free Episode" in subscription_title
        return False

    def refuse_vanishing_ads_if_visible(self):
        """This function checks if a vanishing ads popup is visible and clicks on the "refuse" button if it is.
        """
        is_current_page = self.check_VadsPage()
        print(f"Check if vanishing ads popup is visible {is_current_page}")
        if is_current_page:
            verify_element_and_click(self._locators["refuse_vanishing_ads"])

    def vanishing_ads_signin_popup_status(self):
        """
        This function returns the text of the header element of a sign-in popup on a webpage.
        :return: the text of the header element of the "Vanishing Ads" sign-in popup.
        """
        vads_signin_text = verify_element_on_load(self.locator.Vads_SignIn_header_text, 10)
        return vads_signin_text

    def vanishing_ads_signup_popup_status(self):
        """
        This function returns the text of a header element on a webpage related to a vanishing ads signup
        popup status.
        :return: the text of the header element of the vanishing ads sign-up popup.
        """
        vads_signup_text = verify_element_on_load(self.locator.Vads_SignUp_header_text, 15)
        return vads_signup_text

    def sign_in_NoThanks_Commercials_link(self):
        """
        This function clicks on the "no thanks" button for commercials during a sign-in process.
        """
        verify_element_and_click(self.locator.noThanks_commericials)

    def showpage_action_popup_status(self):
        """
        This function checks if any of three specific elements are present on a page and returns True if any
        are found, otherwise False.
        :return: a boolean value (True or False) depending on whether any of the three specified elements
        are found on the page.
        """
        if verify_element_on_load(self._locators["action_page_signin_popup_title"], 10):
            return True
        elif verify_element_on_load(self._locators["action_page_signin_popup_title2"], 10):
            return True
        elif verify_element_on_load(self._locators["action_page_signin_popup_title3"], 10):
            return True
        else:
            return False

    def Yes_makeAds_vanish_button(self):
        """
        This function clicks on a "yes" button to make ads vanish.
        """
        verify_element_and_click(self.locator.yes_makes_ads_vanish)

    def launch_the_signin_or_sign_up_popup_through_given_element(self, locator_type, video_name):
        """
        This function launches a sign-in or sign-up popup through a given element.
        :param locator_type: The type of locator used to identify the element to be clicked. It could be
        "card" or "carousel_play_btn".
        :param video_name: The name of the video for which the sign-in or sign-up popup needs to be launched
        :return: a boolean value which is determined by the expression `video_name is None`. If `video_name`
        is None, then the function will return True, otherwise it will return False.
        """
        element_to_be_clicked = self.get_element_to_be_clicked(locator_type, video_name)
        if element_to_be_clicked is None:
            print(f"No element found with given details with the locator type {locator_type}")
            return video_name is None
        self.videoTitle = video_name
        # verify_element_and_click(element_to_be_clicked)
        # Scroll_to_element("//h2[text()=' Stream Free TV ']",-200)
        # verify_element_and_click("//img[@title='Ghost Dimension: Lockdown']/ancestor::figure//following-sibling::div[@class='play-btn']/a")
        # verify_element_and_click("//div[@class='p-carousel-items-container']//div[2]//img[@title='Firefly']/ancestor::figure//following-sibling::div[@class='play-btn']/a")
        # verify_element_and_click("//div[@id='pr_id_1']//div[3]//img[contains(@title,'A Twist in the Tale')]/ancestor::figure//following-sibling::div[@class='play-btn']/a")
        # mouse_over_to_element(self.locator.image_path)
        Scroll_to_element(element_to_be_clicked, 200)
        time.sleep(5)
        element_by_javascript(element_to_be_clicked)

    def user_click_on_horror_carousal(self, locator_type, video_name):
        """
        This function launches a sign-in or sign-up popup through a given element.

        :param locator_type: The type of locator used to identify the element to be clicked. It could be
        "card" or "carousel_play_btn".
        :param video_name: The name of the video for which the sign-in or sign-up popup needs to be launched
        :return: a boolean value which is determined by the expression `video_name is None`. If `video_name`
        is None, then the function will return True, otherwise it will return False.
        """
        # Scroll_to_element("//h2[text()=' Stream Free TV ']",-400)
        element_to_be_clicked = self.get_element_to_be_clicked(locator_type, video_name)
        if element_to_be_clicked is None:
            print(f"No element found with given details with the locator type {locator_type}")
            return video_name is None
        self.videoTitle = video_name
        # element_by_javascript(element_to_be_clicked)
        element_by_javascript("//img[@title='Ghost Dimension: Lockdown']/ancestor::figure//following-sibling::div[@class='play-btn']/a")

    def user_click_on_scifi_carousal(self, locator_type, video_name):
        """
        This function launches a sign-in or sign-up popup through a given element.

        :param locator_type: The type of locator used to identify the element to be clicked. It could be
        "card" or "carousel_play_btn".
        :param video_name: The name of the video for which the sign-in or sign-up popup needs to be launched
        :return: a boolean value which is determined by the expression `video_name is None`. If `video_name`
        is None, then the function will return True, otherwise it will return False.
        """
        element_to_be_clicked = self.get_element_to_be_clicked(locator_type, video_name)
        if element_to_be_clicked is None:
            print(f"No element found with given details with the locator type {locator_type}")
            return video_name is None
        self.videoTitle = video_name
        # element_by_javascript(element_to_be_clicked)
        element_by_javascript("//img[@title='Firefly']/ancestor::figure//following-sibling::div[@class='play-btn']/a")

    def user_click_on_fantasy_carousal(self):
        """
        user clicks on fantasy carousal show play icon
        """
        Scroll_to_element(self.locator.Home_carousel_section)
        mouse_over_to_element(self.locator.Home_carousel_section)
        time.sleep(2)
        verify_element_and_click("//html/body/app-root/div[2]/app-genre/main/div[2]/p-carousel/div/div/div/div/div/div[3]/div/div[2]/a")
        time.sleep(5)

    def set_the_popup_on_given_mode(self, popup_mode):
        """
        This function sets a popup on a given mode and checks if it is already on that mode.
        :param popup_mode: A string representing the mode in which the popup should be set
        """
        time.sleep(5)
        popup_title = self.se2lib.get_text(self._locators["text_popup_title"])
        if popup_mode in popup_title:
            print("Already on given mode")
        else:
            verify_element_and_click(self.get_redirection_locator(popup_mode), 20)

    def get_redirection_locator(self, popup_mode):
        """
        This function returns the locator for either the "Sign In" or "Sign Up" text based on the input
        popup mode.
        :param popup_mode: A string parameter that specifies the type of popup mode. It can be either
        "SignIn" or "SignUp"
        :return: a locator based on the value of the `popup_mode` parameter. If `popup_mode` is "SignIn",
        the locator for the "text_sign_in" element is returned. If `popup_mode` is "SignUp", the locator for
        the "text_sign_up" element is returned.
        """
        if popup_mode == "Sign In":
            return self._locators["text_sign_in"]
        elif popup_mode == "Sign Up":
            return self._locators["text_sign_up"]

    def user_click_on_google_link(self):
        """This function clicks on a Google link based on the availability of different elements.
        """
        Vads_signin_google = verify_element_on_load(self.locator.vads_signin_google_button)
        vads_signup_google = verify_element_on_load(self.locator.vads_signup_google_button)
        signin_google = verify_element_on_load(self.locator.signin_google_link)
        signup_google = verify_element_on_load(self.locator.signup_google_link)
        if Vads_signin_google is True:
            verify_element_and_click(self.locator.vads_signin_google_button)
            print("element clicked successfully")
        elif vads_signup_google is True:
            self.se2lib.click_element(self.locator.vads_signup_google_button)
        elif signin_google is True:
            self.se2lib.click_element("//button[@class='google-btn']")
        elif signup_google is True:
            self.se2lib.click_element("//button[@class='google-btn']")
            # self.se2lib.click_element(self.locator.signup_google_link)
        else:
            print("unable to click on google link")

    def user_click_on_create_account_link(self):
        """
        This function clicks on a "create account" link, selects a "personal use" option if available, and
        prints a message if the option is not available.
        """
        verify_element_and_click(self.locator.google_create_account_button)
        personal_use = verify_element_on_load(self.locator.google_personal_use)
        if personal_use is True:
            verify_element_and_click(self.locator.google_personal_use)
        else:
            print("no drop down value with personal use")

    def user_signup_first_name(self, first_name):
        """
        This function inputs the user's first name into a text field on a webpage.
        :param first_name: The first name of the user who is signing up
        """
        self.se2lib.input_text(self.locator.google_first_name, first_name)

    def user_signup_last_name(self, last_name):
        """
        This function inputs the user's last name into a text field on a Google sign-up page using the
        Selenium WebDriver library.
        :param last_name: The last name of the user who is signing up. This parameter is passed to the
        function `user_signup_last_name` as an argument and is used to input the last name into a text field
        """
        self.se2lib.input_text(self.locator.google_last_name, last_name)

    def user_signup_user_name(self, user_name):
        """
        This function inputs a user's name into a text field on a website using the Selenium library.
        :param user_name: The parameter "user_name" is a string that represents the username that the user
        wants to sign up with.
        """
        self.se2lib.input_text(self.locator.google_user_name, user_name)

    def user_signup_password(self, password):
        """This function inputs a user's password and confirms it in a Google sign-up form.
        :param password: The parameter "password" is a string that represents the user's desired password
        for signing up on a website or application. The function "user_signup_password" takes this password
        as input and uses it to fill in the password and confirm password fields on the sign-up page
        """
        self.se2lib.input_text(self.locator.google_user_password, password)
        self.se2lib.input_text(self.locator.google_confirm_password, password)

    def user_signup_DOB_details(self):
        """
        This function inputs the user's date of birth details during a Google signup process.
        """
        self.se2lib.input_text(self.locator.google_signup_month)
        self.se2lib.input_text(self.locator.google_signup_day)
        self.se2lib.input_text(self.locator.google_signup_year)

    def user_enters_mobile_number(self, mobile_num):
        """
        This function takes a mobile number input from the user and enters it into a specific field on a
        webpage using Selenium.
        :param mobile_num: The mobile number that the user wants to enter in the Google sign-up form
        """
        self.se2lib.input_text(self.locator.goolge_signup_mobile_number, mobile_num)

    def user_signup_gender_selection(self):
        """
        This function inputs text into a gender selection field for a user sign-up process.
        """
        self.se2lib.input_text(self.locator.google_signup_gender)

    def user_clicks_agree_button(self):
        """
        This function clicks on the "I agree" button if it is present on the webpage.
        """
        verify_element_and_click(self.locator.span_Iagree)

    def user_clicks_on_google(self):
        """
        This function simulates a user clicking on a Google button.
        """
        verify_element_and_click(self._locators["vads_signin_google_button"])

    def user_enter_email_address(self, user_name):
        """
        User verify element and enter the email address
        """
        verify_element_on_load(self._locators["google_input_username"])
        self.se2lib.input_text(self._locators["google_input_username"], user_name)

    def user_clicks_on_next(self):
        """This function clicks on the "next" button on a Google page after verifying its presence.
        """
        verify_element_and_click(self._locators["google_next_button"])

    def user_enter_password(self, password):
        """
        This function inputs a user's password into a Google login page.
        :param password: The password parameter is a string that represents the user's password input. It is
        passed as an argument to the user_enter_password method
        """
        verify_element_on_load(self._locators["google_input_password"])
        self.se2lib.input_text(self._locators["google_input_password"], password)

    def tag_verify(self, result, timeout):
        """This function verifies if a tag is present on a webpage and returns a boolean value based on the
        result.
        :param result: A string that indicates whether the test case is expected to pass or fail.
        :param timeout: The timeout parameter is the maximum amount of time (in seconds) that the code will
        wait for a certain element to appear on the page before timing out and throwing an error
        :return: The method returns a boolean value indicating whether the video title is present in the
        text of the "next page" element.
        """
        if result == 'should_fail':
            self.se2lib.element_should_be_visible(self._locators["valid_email_address_error"])
        else:
            self.se2lib.wait_until_page_contains_element(self._locators["user_profile_pic"], timeout)
            return self.videoTitle in self.se2lib.get_text(self._locators["user_profile_pic"])

    def user_clicks_on_facebook(self):
        """This function clicks on the Facebook button.
        """
        verify_element_and_click(self._locators["signin_facebook_button"])

    def user_click_on_facebook_link(self):
        """
        This function clicks on a Facebook link based on the availability of different Facebook buttons.
        """
        vads_signin = verify_element_on_load(self.locator.signin_facebook_button)
        vads_signup = verify_element_on_load(self.locator.signup_facebook_button)
        signin_fb = verify_element_on_load(self.locator.signin_facebook_button)
        signup_fb = verify_element_on_load(self.locator.signup_facebook_button)
        signup_fb_login = verify_element_on_load(self.locator.signup_fb_button)
        if vads_signin is True:
            self.se2lib.click_element(self.locator.signin_facebook_button)
        elif vads_signup is True:
            self.se2lib.click_element(self.locator.signup_facebook_button)
        elif signin_fb is True:
            self.se2lib.click_element(self.locator.signin_facebook_button)
        elif signup_fb is True:
            self.se2lib.click_element(self.locator.signup_facebook_button)
        elif signup_fb_login is True:
            self.se2lib.click_element(self.locator.signup_fb_button)
        else:
            print("user unable to click on facebook icon")

    def user_enter_facebook_email(self, user_name):
        """
        This function inputs the user's Facebook email into a specified field.
        :param user_name: The parameter "user_name" is a string that represents the email address associated
        with the user's Facebook account.
        """
        verify_element_on_load(self._locators["facebook_username"])
        self.se2lib.input_text(self._locators["facebook_username"], user_name)

    def user_enter_facebook_password(self, password):
        """User enter Password for the Facebook
        """
        verify_element_on_load(self._locators["facebook_password"])
        self.se2lib.input_text(self._locators["facebook_password"], password)

    def clicks_on_login(self):
        """This function clicks on the Facebook login button after verifying its presence on the page.
        """
        verify_element_and_click(self._locators["facebook_login_button"])

    def facebook_continue_button(self):
        """ The function checks if the "facebook_continue" button is present and clicks on it if it is,
        otherwise it prints a message.
        """
        if verify_element_on_load(self._locators["facebook_continue"], 25):
            verify_element_and_click(self._locators["facebook_continue"], 2)
        else:
            print('facebook_continue button not found')

    def check_the_after_result(self, result, timeout):
        """
        The function is used to check after sign-in condition whether the sign-in was successful or not.
        Args:
        result: the parameter signifies whether the sign-in will be successful or not after entering
        the given user details. Possible values are: should_pass/should_fail
        timeout: Waiting time for the next page to be loaded after successful sign-in.
        """
        if result == 'should_fail':
            self.se2lib.element_should_be_visible(self._locators["valid_email_address_error"])
        else:
            self.se2lib.wait_until_page_contains_element(self._locators["user_profile_pic"], timeout)
            # return self.videoTitle in self.se2lib.get_text(self._locators["user_profile_pic"])

    def get_element_to_be_clicked(self, locator_type, video_name):
        """
        This function is used to get the element to launch the sign-in/sign-up popup depending on the given
        locator_type.
        Args: locator_type: Type of element to be clicked. Possible values card/ carousel_play_btn
        video_name: Name of the video. Returns: The element depending on the type of locator_type if found. None
        otherwise.
        """
        match locator_type:
            case "card":
                return self.get_card_element(video_name)
            case "carousel_play_btn":
                return self.get_carousel_play_btn(video_name)
        return None

    def get_card_element(self, video_name):
        """
        This function is used to get the locator of video cards present at the bottom of screen.
        Args:
        video_name: video_name: Name of the video
        Returns: the locator of video card if found, None otherwise.
        """
        print('get_card_element')
        cards = self.se2lib.get_webelements(self._locators["bottom_card_list"])
        index = 1
        for card in cards:
            print("card.text " + card.get_attribute('title'))
            if card.get_attribute('title') == video_name:
                return self._locators["bottom_card_container"] + "[" + str(index) + "]//figure"
            index = index + 1
        return None

    def get_carousel_play_btn(self, video_name):
        """
        This function is used to get the locator of carousal play button with given video name.
        Args:
        video_name: Name of the video
        Returns: the locator of carousal play button if found, None otherwise.
        """
        for index in range(3):
            Scroll_to_element(self.locator.Home_carousel_section)
            mouse_over_to_element(self.locator.Home_carousel_section)
            time.sleep(2)
            mouse_over_to_element(self.locator.devotv_text)
            carousal_play_button_locator = self.locator["carousal_play_button_locator"+str(index)]
            # verify_element_and_click(self.locator["carousal_flex"+str(index)])
            time.sleep(2)
            carousal_play_button_title = self.se2lib.get_webelement(carousal_play_button_locator).get_attribute('title')
            print(carousal_play_button_title)
            if "A Twist in the Tale" in carousal_play_button_title:
                carousal_play_button_title = "A Twist in the Tale"
                print(carousal_play_button_title)
            if carousal_play_button_title == video_name:
                return carousal_play_button_locator + "/../../div[@class='play-btn']//a"
        return None

    def Click_Iwant_Commercials(self):
        """
        User clicks on I want commercials link, Without signin
        """
        time.sleep(2)
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        Iwant_commercial = verify_text("No, I want commercials")
        if Iwant_commercial is True:
            verify_element_and_click(self.locator.no_iwant_commercials)
        else:
            verify_element_and_click(self.locator.noThanks_commericials)

    def direct_sign_in_with_given_details(self, user_name, password, result, video_name=None, timeout=25, locator_type='card',
                                          popup_mode='SignIn', signin_mode='default'):
        """
        user signin with given details
        """
        self.launch_the_signin_or_sign_up_popup_through_given_element(locator_type, video_name)
        if self.validate_current_page():
            self.set_the_popup_on_given_mode(popup_mode)
            self.sign_in_with_following_details(signin_mode, user_name, password, result, timeout)
        else:
            print("Some error occurred in Signing In")
            return False

    def sign_in_with_following_details(self, mode_of_signin, user_name, password, result, timeout=15):
        """
        Sign in the user with given details
        Args:
       :param mode_of_signin: This defines the way of sign in, possible values: default, facebook, apple, google
       :param user_name: Username to proceed with sign-in
       :param password: Password to proceed with the sign-in
       :param result: To check the result whether the function should pass or fail the scenario.Possible values should_fail and should_pass.
       :param timeout: if user wants to define a timeout for this case, default value is 15.
       """
        match mode_of_signin:
            case "default":
                self.default_sign_in(user_name, password, result, timeout)

    def default_sign_in(self, user_name, password, result, timeout):
        """
        This function is used to sign in the user using username and password.
        Args:
        user_name: Username of the user
        password: Password to login
        result: the parameter signifies whether the sign-in will be successful or not after entering
        the given user details. Possible values are: should_pass/should_fail
        timeout: Waiting time for the next page to be loaded after successful sign-in.
        """
        self.se2lib.input_text(self._locators["email_textbox_signin"], user_name)
        self.se2lib.input_text(self._locators["password_textbox_signin"], password)
        self.se2lib.click_element(self._locators["agree_signin_button"])
        self.check_the_after_result(result, timeout)

    def ad_free_login_pop_appear(self):
        """
        this function verify the AD-free! popup where the popup page name will be
        "Devotv - Stream Free TV - No Ads"
        """
        if verify_element_on_load(self._locators["noThanks_commericials"]):
            if verify_element_on_load(self._locators["agree_signup_button"]):
                return True
        return False

    def login_pop_appear(self):
        """
        This function checks if the login popup appears on page load and returns a boolean value.
        :return: a boolean value. If the login popup element is verified to be present on the page, the
        function returns True. Otherwise, it returns False.
        """
        if verify_element_on_load(self._locators["login_popup_close_btn"], 12):
            return True
        return False

    def click_already_have_account(self):
        """
        This function clicks on the "already have an account" button.
        """
        verify_element_and_click(self._locators["already_have_an_account"])

    def user_enter_email_for_homePage(self, user_name):
        """
        This function inputs a user's email into a text field on the homepage.
        :param user_name: The parameter "user_name" is a string that represents the email address entered by
        the user on the homepage.
        """
        self.se2lib.input_text(self._locators["input_user_name_homePage"], user_name)

    def user_enter_Password_for_homePage(self, password):
        """
        This function inputs a password on the home page of a website.
        :param password: The password parameter is a string that represents the password that the user wants
        to enter on the input field for the home page
        """
        verify_element_on_load(self._locators["input_password_homePage"])
        self.se2lib.input_text(self._locators["input_password_homePage"], password)

    def user_clicks_on_signin_for_homePage(self):
        """
        This function clicks on the "signin" button on the homepage.
        """
        verify_element_and_click(self._locators["button_signin_homePage"])

    def user_clicks_on_watch_with_commercials(self):
        """
        This function simulates a user clicking on a "watch with commercials" button.
        """
        verify_element_and_click(self._locators["noThanks_commericials"])

    def watch_with_commercials_appear(self):
        """
        This function checks if a specific element is present on the page and returns a boolean value
        accordingly.return: a boolean value. If the element with the locator "noThanks_commericials" is verified to be
        present on the page, the function returns True. Otherwise, it returns False.
        """
        if verify_element_on_load(self._locators["noThanks_commericials"]):
            return True
        return False

    def signin_mode(self):
        """
        This function clicks on the "signin" element after scrolling to it.
        """
        Scroll_to_element(self._locators["button_signin_homePage"])
        verify_element_and_click(self._locators["button_signin_homePage"])

    def sign_out_with_current_user(self):
        """This function clicks on the profile button, verifies the sign out button, scrolls to it, and clicks
        on it to sign out the current user.
        """
        verify_element_and_click(self._locators["right_top_profile_button"])
        verify_element_on_load(self._locators["sign_out_button"])
        Scroll_to_element(self._locators["sign_out_button"])
        self.se2lib.click_element(self._locators["sign_out_button"])
        time.sleep(2)

    def click_on_sigin_top_header(self):
        """ This function is used to click on sign in button at top header in right corner.
        """
        verify_element_and_click(self._locators["signin_tab"])
