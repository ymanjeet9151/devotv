import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from BasePage import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import json


class HomePage(BasePage):
    """
    A Page Object class for interacting with the Home Page.

    This class encapsulates the locators and functions specific to the Home Page of the web application.
    It provides utilities to verify that the user is on the correct page, interact with genre and navigation tabs,
    retrieve logged-in user details, and work with video content cards.
    """
    _locators = {
        "show_more": "//a[text()='Show More']",
        # "show_moreDiv": "//div[contains(@class,'show-bundle-row')]",
        "show_moreDiv": "//div[contains(@class,'row show-bundle-row profile-project-bundle clearfix')]",
        "watch_on_demand_header": "//div[@id='watchonDemandId']",
        "genre_button": "//a[normalize-space()='{}']",
        "All_Genres": "//a[contains(@class, 'active')][contains(text(),'All')]",
        "tv_room_watch_header": "//h4[text()='TV Room • Watch Free Now']",
        "My_shows": "//div[@id='stickyHeader']//div[@class='ml-auto nav-menu flex-row d-lg-flex']//a[text()='My Shows']",
        "my_fan_page": "//div[@id='stickyHeader']//div[@class='ml-auto nav-menu flex-row d-lg-flex']//a[text()='My Fan Page']",
        "Live_tv": "//div[@id='stickyHeader']//div[@class='ml-auto nav-menu flex-row d-lg-flex']//a[text()='Live TV']",
        "onDemand_tab": "//div[@class='ml-auto nav-menu flex-row d-lg-flex']//*[text()='On Demand']",
        "signin_tab": "//div[@id='stickyHeader']//a[@class='btn-signup']",
        "liveTv_viewers": "//a[contains(text(),'Live TV')][1]",
        "liveTv_viewers_ress": "//ul[contains(@class,'main-nav mobile-nav')]//a[contains(text(),'Live TV')]",
        "playFromStart": "//a[text()='Play From Start']",
        "home_page_video_paly_icon": "//a[@class='video-play-icon-active']",
        "cache": "//div[@class='cookie-container']/button[@class='close']",
        "user_profile_img": "//div[@class='avtar-ico']//li[1]",
        "view_FanPage": "//a[text()='View Fan Page']",
        "bottom_card_container": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]//div[@class='show-col']//figure//img",
        "bottom_card_list": "(//div[contains(@class,'row show-bundle-row profile-project-bundle')]/descendant::div[@class='show-col'])"

    }

    def _is_current_page(self):
        """
        This function checks whether the current page is the Home Page by verifying the presence of key UI elements.

        :return:
            - *`bool`* — Returns `True` if the Home Page is loaded correctly (i.e., expected elements like headers,
            viewer stats, and controls are present), otherwise `False`.
        """
        tv_room = verify_element_on_load(self.locator.tv_room_watch_header, time=0)
        # sign_in = verify_element_on_load(self.locator.signin_tab, time=0)
        if verify_element_on_load(self.locator.liveTv_viewers, time=20):
            liveTvView = verify_element_on_load(self.locator.liveTv_viewers, time=20)
        else:
            liveTvView = verify_element_on_load(self.locator.liveTv_viewers_ress, time=20)
        playfromStart = verify_element_on_load(self.locator.playFromStart, time=20)

        if tv_room and liveTvView and playfromStart is True:
            print("On HomePage")
        else:
            print("Home page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_HomePage(self):
        """
        This method validates whether the user is on the home page by checking the presence of key elements.

        Raises:
            BuiltIn().fail: If any of the required elements (`tv_room`, `liveTvView`, or `playfromStart`) are not found,
                            this function will raise an error, indicating that the user is not on the correct page.
        """
        tv_room = verify_element_on_load(self.locator.tv_room_watch_header, time=0)
        liveTvView = verify_element_on_load(self.locator.liveTv_viewers, time=0)
        playfromStart = verify_element_on_load(self.locator.playFromStart, time=0)

        if (tv_room and liveTvView and playfromStart) is not True:
            BuiltIn().fail("Incorrect Page")

    def user_click_on_genre_button(self, genre_name):
        """
        This function clicks on a genre button on a webpage, based on the provided genre name.

        Args:
            genre_name (str): The name of the genre that the user wants to click on. This is used to format the locator string
                            to locate the specific genre button element on the page.

        Raises:
            BuiltIn().fail: If the genre button element cannot be found or clicked, the function will raise an error,
                            indicating that the user could not interact with the button.
        """
        verify_element_on_load(self.locator.watch_on_demand_header)
        Scroll_to_element(self.locator.watch_on_demand_header)
        verify_element_and_click(self.locator.genre_button.format(genre_name))

    def click_on_show_more_option(self):

        """The function waits for 10 seconds, checks if a certain element is loaded, and then clicks on it if
        it is, before scrolling to another element and clicking on it.
        """
        time.sleep(10)
        if verify_element_on_load(self.locator.cache):
            verify_element_and_click(self.locator.cache)
            pass
        Scroll_to_element(self.locator.show_more, 200)
        verify_element_and_click(self.locator.show_more)

    def get_logged_in_user_Id(self):
        """This function retrieves the user ID of the currently logged in user by extracting it from the URL of
        their fan page.
        :return:
            - the user ID of the logged-in user.
        """
        verify_element_and_click(self.locator.user_profile_img)
        time.sleep(6)
        verify_element_and_click(self.locator.view_FanPage)
        url = self.se2lib.driver.current_url
        user_id = url.split("fanpage/")[1]
        return user_id

    def click_any_video_card_on_home_page(self):
        """
        This function clicks on any available video card from the home page by locating the card container and list elements.

        -Steps:
        - Identifies the video card section using predefined locators.
        - Performs a click action on one of the available cards.
        """
        self.click_any_video_card_on_page(self._locators['bottom_card_container'], self._locators["bottom_card_list"])
