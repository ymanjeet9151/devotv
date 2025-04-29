import random
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *


class BasePage(PageObject):
    """
    Base class for all page objects, providing shared functionality and locators.

    This class serves as a foundation for interacting with web pages in a test
    framework. It includes reusable methods for interacting with video card
    elements and handling common UI components like cookie popups.
    """
    common_locators = {
        "cache": "//div[@class='cookie-container']/button[@class='close']",
    }

    def click_any_video_card_on_page(self, card_container, card_list):
        """
        This function Clicks a randomly selected video card from a given list on the web page.

        this keyword contains 2 arguments:
            - `card_container` (*`str`*): Locator for the container element that holds all video cards
            on the page.

            - `card_list` (*`str`*): XPath or CSS selector pattern for identifying individual video
            cards in the container.

        Raises:
            - Logs a message if no video cards are present.
        """
        cards = self.se2lib.get_webelements(card_container)
        card_count = len(cards)
        if card_count > 0:
            random_card_index = random.randint(1, card_count - 1)
            print(f"random_card_index {random_card_index}")
            print(f"Random card selected {cards[random_card_index].get_attribute('title')}")
            Scroll_to_element(card_list + "[" + str(random_card_index) + "]")
            verify_element_and_click(card_list + "[" + str(random_card_index) + "]", 15)
        else:
            print("No Video card present in the list")

    def close_cookies_popup(self):
        """
        This functions closes the cookies popup on the webpage if it is present.

        Checks for the presence of the cookies popup using a predefined locator and
        clicks to close it if found.

        Raises:
            - Logs a message if the cookies popup is not found.
        """
        if verify_element(self.common_locators["cache"]):
            verify_element_and_click(self.common_locators["cache"])
