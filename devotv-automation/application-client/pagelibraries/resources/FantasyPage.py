import time
import os
import sys

from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from selenium.common.exceptions import NoSuchElementException
from modules.custom_keywords import *
from BasePage import *
from selenium.webdriver.common.by import By


class FantasyPage(BasePage):
    """
    WebElements and keywords for Fantasy Page.
    """
    _locators = {
        "Flex_control_paging": "//ol[@class='flex-control-nav flex-control-paging']/li/a[text()='{}']",
        "carousal_video": "//div[@class='p-carousel-items-content']//div[2]//img[contains(@title,'A Twist in the Tale')]",
        "video_play_button": "//div[@class='p-carousel-items-content']//div[2]//img[contains(@title,'A Twist in the Tale')]/../../div[@class='play-btn']//a//*[name()='svg']",
        "flex_direction_next_button": "//button[@class='p-ripple p-element p-carousel-next p-link']",
        "genere_button": "//a[contains(@class, 'active')][contains(text(),'Fantasy')]",
        "watch_on_demand_header": "//div[@id='watchonDemandId']",
        "Fantasy_Genre_button": "//a[normalize-space()='Fantasy']",
        "cache": "//div[@class='cookie-container']/button[@class='close']",
        "bottom_card_list": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]/descendant::div[@class='show-col']",
        "bottom_card_container": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]//div[@class='show-col']//figure//img[2]",

    }

    def _is_current_page(self):
        """This function checks if the current page is the FantasyLanding page by verifying the presence of
        certain elements.
        :return: a boolean value, either True or False.
        """
        time.sleep(2)
        # Scroll_to_element(self.locator.watch_on_demand_header,500)
        # carousal_video = verify_element_on_load(self.locator.carousal_video, time=15)
        # video_play_button = verify_element_on_load(self.locator.video_play_button, time=15)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)
        # if carousal_video and video_play_button and genere_button is True:
        #     print("On FantasyLanding Page")
        if genere_button is True:
            print("On FantasyLanding Page")
        else:
            print("Fantasy page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_FantasyPage(self):
        """
        this method is validating the user is on fantasy page or not
        """
        time.sleep(2)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)
        if (genere_button) is not True:
            BuiltIn().fail("Incorrect Page")

    def user_clicks_on_Fantasy(self):
        """This function verifies and clicks on the "Fantasy" genre button on a watch on demand page.
        """
        verify_element_on_load(self.locator.watch_on_demand_header)
        Scroll_to_element(self.locator.watch_on_demand_header)
        verify_element_and_click(self.locator.Fantasy_Genre_button)

    def click_any_video_card_on_fantasy_page(self):
        """This function clicks on any video card on a fantasy page.
        """
        self.click_any_video_card_on_page(self._locators['bottom_card_container'], self._locators["bottom_card_list"])
