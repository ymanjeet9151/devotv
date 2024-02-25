import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from selenium.common.exceptions import NoSuchElementException
from modules.custom_keywords import *
from BasePage import *
from selenium.webdriver.common.by import By


class MyFanPage(BasePage):
    """
    WebElements and keywords for MyFanPage.
    """
    _locators = {
        "follow_button": "//button[text()=' Follow ']",
        "share_link": "//app-view-profile//a[@title='Share']//span[text()='Share']",
        "MyfanPage": "//*[@id='stickyHeader']/div/div[2]/div/ul/li[1]/span/a/img",
        "coin_bank": "//strong[text()='Coin Bank ']",
        "coin_balance": "//strong[text()='Devotv Coin Balance']/..",

    }

    def _is_current_page(self):
        """
         Validate the Current Page is in My FanPage
        """
        follow_button = verify_element_on_load(self.locator.follow_button, time=0)
        share_link = verify_element_on_load(self.locator.share_link, time=0)

        if follow_button and share_link is True:
            print("On MyFanPage")
        else:
            print("MyFan page is not loaded correctly")
            return False
        return True

    def user_clicks_on_profile_tab(self):
        """This function clicks on the Horror genre button after verifying the header and scrolling to the
        element.
        """
        verify_element_and_click(self.locator.MyfanPage)

    def user_clicks_on_coinbank_tab(self):
        """This function clicks on the Horror genre button after verifying the header and scrolling to the
        element.
        """
        verify_element_and_click(self.locator.coin_bank)
        time.sleep(10)

    def get_the_coin_balance(self):
        """
        get the coin balance
        """
        time.sleep(2)
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.coins = se2lib.driver.find_element(By.XPATH, self.locator.coin_balance).text
        self.total_coins = self.coins[20:22]
        return self.total_coins

    def validate_user_is_on_MyFanPage(self):
        """
        this method is validating the user is on MyFanPage page or not
        """
        follow_button = verify_element_on_load(self.locator.follow_button, time=0)
        share_link = verify_element_on_load(self.locator.share_link, time=0)
        if (follow_button and share_link) is not True:
            BuiltIn().fail("Incorrect Page")
