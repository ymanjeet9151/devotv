import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from selenium.common.exceptions import NoSuchElementException
from modules.custom_keywords import *
from BasePage import *
from selenium.webdriver.common.by import By


class SciFiPage(BasePage):
    """
    WebElements and keywords for SciFi Page.
    """
    _locators = {
        "Flex_control_paging": "//ol[@class='flex-control-nav flex-control-paging']/li/a[text()='{}']",
        "carousal_video": "//div[@class='p-carousel-items-content']//div[2]//img[@title='Firefly']",
        "video_play_button": "//img[@title='Firefly']/ancestor::figure//following-sibling::div[@class='play-btn']/a",
        "flex_direction_next_button": "//button[@class='p-ripple p-element p-carousel-next p-link']",
        "genere_button": "//a[contains(@class, 'active')][contains(text(),'Sci-Fi')]",
        "watch_on_demand_header": "//div[@id='watchonDemandId']",
        "SciFi_Genre_button": "//a[normalize-space()='Sci-Fi']",
        "cache": "//div[@class='cookie-container']/button[@class='close']",
        "bottom_card_list": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]/descendant::div[@class='show-col']",
        "bottom_card_container": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]//div[@class='show-col']//figure//img[2]",

    }

    def _is_current_page(self):
        """This function checks if the current page is the SciFiLanding page by verifying the presence of
        specific elements.
        :return: a boolean value, either True or False.
        """
        # Scroll_to_element(self.locator.watch_on_demand_header, 100)
        # carousal_video = verify_element_on_load(self.locator.carousal_video, time=0)
        # print(carousal_video)
        time.sleep(2)
        video_play_button = verify_element_on_load(self.locator.video_play_button, time=0)
        # print(video_play_button)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)

        if video_play_button and genere_button is True:
            print("On SciFiLanding Page")
        else:
            print("SciFi page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_SciFiPage(self):
        """
        this method is validating the user is on SciFiPage page or not
        """
        time.sleep(2)
        video_play_button = verify_element_on_load(self.locator.video_play_button, time=0)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)
        if (video_play_button and genere_button) is not True:
            BuiltIn().fail("Incorrect Page")

    def user_clicks_on_SciFi(self):
        """
        The function clicks on the SciFi genre button after verifying the header and scrolling to it.
        """
        verify_element_on_load(self.locator.watch_on_demand_header)
        Scroll_to_element(self.locator.watch_on_demand_header)
        verify_element_and_click(self.locator.SciFi_Genre_button)

    def click_any_video_card_on_scifi_page(self):
        """This function clicks on any video card on the sci-fi page.
        """
        self.click_any_video_card_on_page(self._locators['bottom_card_container'], self._locators["bottom_card_list"])
