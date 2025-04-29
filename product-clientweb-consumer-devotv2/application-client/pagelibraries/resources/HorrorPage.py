import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from selenium.common.exceptions import NoSuchElementException
from modules.custom_keywords import *
from BasePage import *
from selenium.webdriver.common.by import By
from robot.api.deco import library, keyword


class HorrorPage(BasePage):
    """
    A Page Object class for interacting with the Horror Page.

    This class defines locators and methods specific to the Horror genre page. It allows verification
    of the page state, interaction with genre elements, carousel videos, and validation of displayed shows.
    """
    _locators = {
        "Flex_control_paging": "//ol[@class='flex-control-nav flex-control-paging']/li/a[text()='{}']",
        "carousal_video": "//div[@class='p-carousel-items-content']//div[2]//img[@title='Ghost Dimension']",
        "video_play_button": "//div[@class='p-carousel-items-content']//div[2]//div[@class='play-btn']//a//*[name()='svg']",
        "flex_direction_next_button": "//button[@class='p-ripple p-element p-carousel-next p-link']",
        "genere_button": "//a[contains(@class, 'active')][contains(text(),'Horror')]",
        "watch_on_demand_header": "//div[@id='watchonDemandId']",
        "cache": "//div[@class='cookie-container']/button[@class='close']",
        # "shows_list_div": "//div[@class='row show-bundle-row profile-project-bundle']",
        "shows_list_div": "//div[@class='row show-bundle-row profile-project-bundle clearfix']",
        "SciFi_Genre_button": "//a[normalize-space()='Sci-Fi']",
        "Horror_Genre_button": "//a[normalize-space()='Horror']",
        "All_Genres": "//a[normalize-space()='All']",
        "landingPage_available_shows": "//div[@class='show-col']//figure//img",
        "bottom_card_list": "(//div[contains(@class,'row show-bundle-row profile-project-bundle')]/descendant::div[@class='show-col'])",
        "bottom_card_container": "//div[contains(@class,'row show-bundle-row profile-project-bundle')]//div[@class='show-col']//figure//img",

    }

    def _is_current_page(self):

        """
        Checks if the current page is the HorrorLanding page by verifying key UI elements.

        :return:
            - *`bool`* — Returns `True` if both the video play button and genre button are present,
            indicating the HorrorLanding page is correctly loaded; otherwise `False`.
        """
        time.sleep(2)
        Scroll_to_element(self.locator.watch_on_demand_header, 100)
        # carousal_video = verify_element_on_load(self.locator.carousal_video, time=0)
        video_play_button = verify_element_on_load(self.locator.video_play_button, time=0)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)
        if video_play_button and genere_button is True:
            print("On HorrorLanding Page")
        else:
            print("Horror page is not loaded correctly")
            return False
        return True

    def validate_user_is_on_HorrorPage(self):
        """
        Validates whether the user is currently on the Horror page by checking for essential page elements.

        Checks for the presence of the video play button and genre button. Fails the test if any of these elements are not found.

        Possible Errors:
            - *AssertionError*: Raised via `BuiltIn().fail()` if the expected elements are not loaded,
            indicating the Horror page did not load correctly.
        """
        time.sleep(3)
        Scroll_to_element(self.locator.watch_on_demand_header, 100)
        video_play_button = verify_element_on_load(self.locator.video_play_button, time=0)
        Scroll_to_element(self.locator.watch_on_demand_header)
        genere_button = verify_element_on_load(self.locator.genere_button, time=0)
        if (video_play_button and genere_button) is not True:
            BuiltIn().fail("Incorrect Page")

    def verify_shows_In_Landing_Page(self):
        """
        Verifies and retrieves the list of available shows on the landing page.

        This function scrolls to the section containing the shows, waits for elements to load,
        and then extracts the titles of the available shows. Special handling is provided for the show
        'William Shatners A Twist in the Tale', where the title is split before being added to the list.

        :return:
            - A list of show titles that are available on the landing page. The title of
            'William Shatners A Twist in the Tale' is processed differently, splitting and appending only
            the portion after 'A'.
        """
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        # Scroll_to_element(self.locator.shows_list_div)
        time.sleep(5)
        shows = se2lib.driver.find_elements(By.XPATH, self.locator.landingPage_available_shows)
        actual_shows = []
        for x in shows:
            if x.get_attribute('title') == 'William Shatner’s A Twist in the Tale':
                title = x.get_attribute('title').split('A')
                print(title)
                actual_shows.append(title[1])
            else:
                actual_shows.append(x.get_attribute('title'))
        print(actual_shows)
        return actual_shows

    def user_clicks_on_Horror(self):
        """This function clicks on the Horror genre button after verifying the header and scrolling to the
        element.
        """
        verify_element_on_load(self.locator.watch_on_demand_header)
        Scroll_to_element(self.locator.watch_on_demand_header)
        verify_element_and_click(self.locator.Horror_Genre_button)

    def click_any_video_card_on_horror_page(self):
        """This function clicks on any video card on a horror page.
        """
        self.click_any_video_card_on_page(self._locators['bottom_card_container'], self._locators["bottom_card_list"])

    def user_close_cookies_popup(self, time=15):
        """
        Closes the cookies popup by clicking on the "cache" element.

        This keyword contains 1 argument(s):
        - `time` (*int*): The time in seconds to wait for the "cache" element to be loaded. Default is 15 seconds (optional).
        """
        verify_element_and_click(self.locator.cache, time)
