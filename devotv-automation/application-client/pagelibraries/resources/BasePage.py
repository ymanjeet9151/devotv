import random
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *


class BasePage(PageObject):
    common_locators = {
        "cache": "//div[@class='cookie-container']/button[@class='close']",
    }

    def click_any_video_card_on_page(self, card_container, card_list):
        """This function clicks on a randomly selected video card from a list of video cards on a web page.
        :param card_container: The container element that holds all the video cards on the page
        :param card_list: The XPath or CSS selector for the list of video cards on the page
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
        """This function closes a cookies popup if it is present on the webpage.
        """
        if verify_element(self.common_locators["cache"]):
            verify_element_and_click(self.common_locators["cache"])
