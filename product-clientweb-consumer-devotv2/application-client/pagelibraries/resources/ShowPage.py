from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class ShowPage(PageObject):
    """
    A Page Object class for interacting with the Show Page.

    This class defines locators and methods specific to the Show Page. It allows verification
    of the page state, interaction with page elements, validates show page with show name,
    get video playing status, and others.
    """
    _locators = {
        "page_title": "//title[text()='Devotv - {}']",
        "show_play_icon_area": "//div[text()=' Now Playing ']",
        "close_video": "//a[text()='Close Video']",
        "video_load": "//div[@class='video-container opacity']",
        "watch_free_now_text": "//span[text()=' WATCH FREE NOW ']",
        "show_video_header": "//div[@class='episode-title']/h6",
        "vanish_ad_title": "//div[@class='vanishing-container']//h4[text()='Stream Free Episode - ']",
        "show_video_play_icon": "//div[@class='play-video']//a",
        "video_play_area": "//video[@id='my-player_html5_api']",
        "video_current_time": "//span[@class='vjs-current-time-display']",
        "ad_duration": "//div[@id='adDurationTimerVal']",
        "play_or_pause_video_button": "//button[@title='Play' or @title='Pause']",
        "action_bar": "//div[@class='detail-container panelHeight']",
        "action_row": "//div[@class='detail-container']",
        "action_btn_like": "//div[contains(@class,'action-btn-col bottom')]//div[@class='like']",
        "action_btn_already_like": "//div[contains(@class,'action-btn-col bottom')]//div[contains(@class,'liked_show')]",
        "action_btn_like_count": "//span",
        "login_user_name": "//div[@class='comments-section-scroll']//input[@id='email']",
        "login_password": "//div[@class='comments-section-scroll']//input[@id='password']",
        "btn_sign_in": "//div[@class='comments-section-scroll']//button[text()=' Sign In ']",
        "watchlist_add_btn": "//div[contains(@class,'action-btn-col bottom')]//div[@class='watchlist']",
        "watchlist_add_btn_ress": "//div[@class='action-btn-col']//div[@class='watchlist']",
        "watchlist_added_btn": "//div[contains(@class,'action-btn-col bottom')]//div[@class='watchlist watchlist-added']",
        "watchlist_added_btn_ress": "//div[@class='action-btn-col']//div[@class='watchlist watchlist-added']",
        "my_shows": "//div[contains(@class,'ml-auto nav-menu')]//a[text()='My Shows']",
        "my_shows_ress": "//ul[contains(@class,'mobile-nav')]//a[text()='My Shows']",
        "remove_watchlist_button": "//button[text()=' Yes, Remove ']",
        "watchlist_header": "//h6[@class='watchlist-heading']",
        "show_title_header": "//div[@class='episode-title']/h6",
        "popup_added_to_watchlist": "//h4[text()=' Show Added to Watchlist ']",
        "ok_button_on_popup": "//div[@class='modal-footer']//button[text()=' OK ']",
        "watchlist_frist_added_show": "(//div[@class='watchlist-bg']/..//../img)[1]",
        "watchlist_frist_show_more_btn": "(//div[@class='more'])[1]",
        "remove_from_watchlist_btn": "//a[@class='remove-watchlist btn-opacity']/..//a[contains(text(),'Remove from Watchlist')]",
        "remove_yes": "//button[text()=' Yes ']",
        "sortby": "//button[@class='dropdown-toggle']",
        "sortby_newest_most_cheered": "//ul[@class='dropdown-menu show']//a[text()='Most Cheered']",
        "sortby_newest_option": "//ul[@class='dropdown-menu show']//a[text()='Newest']",
        "sortby_hot_option": "//ul[@class='dropdown-menu show']//a[text()='Hot']",
        "first_commenter_name": "//div[@class='comment-section show-comment']/div[4]//div[contains(@class,'donor-')]",
        "Most_Cheered_count1": "//div[@class='comment-section show-comment']/div[4]//a[@class='upvote']",
        "Most_Cheered_count4": "//div[@class='comment-section show-comment']/div[7]//a[@class='upvote']",
        "comment_time1": "//div[@class='comment-section show-comment']/div[4]//time[@class='msg-time']",
        "comment_time4": "//div[@class='comment-section show-comment']/div[7]//time[@class='msg-time']",
        "Hot_verify_element1": "//div[@class='comment-section show-comment']/div[4]//div[@class='action-col d-flex']//span",
        "Hot_verify_element4": "//div[@class='comment-section show-comment']/div[7]//div[@class='action-col d-flex']//span",
        "clapped_element": "(//*[@id='clapped'])[1]",
        "upvote_comment_btn": "//div[@class='comment-section show-comment']/div[4]//a[@class='upvote']",
        "first_user_comment": "//div[@class='comment-section show-comment']/div[4]",
        "show_replies_btn": "//a[text()='Show Replies ']",
        "first_reply_first_comment": "//div[contains(@class,'comment-reply-row')]//div[@class='global-comment-view'][1]",
        "clap_btn_show_replies": "//a[@class='upvote']",
        "clapped_btn_show_replies": "//*[@id='clapped']",
        "vote_count_replies": "//a[@class='upvote']",
        "share_icon": "//div[@class='action-btn-col bottom']//div[@class='share']",
        "share_icon_ress": "//div[@class='action-btn-col']//div[@class='share']",
    }

    def _is_current_page(self):
        """
        Checks if the current page is a show page by verifying the presence of a specific UI element.

        This function verifies whether the show page has loaded correctly by checking the visibility of
        the show title header. If the header is present, the page is considered a show page
        :Returns:
            - *bool*: Indicates whether both the show title header and share icon are present on the page.
        """
        # video_icon = verify_element_on_load(self.locator.show_title_header, time=5)
        # # share_icon = verify_element_on_load(self.locator.share_icon, time=5)
        # #
        # if video_icon is True:
        #     print("On Show Page")
        # else:
        #     print("Show page is not loaded correctly")
        #     return False
        # return True
        return True

    def validate_user_is_on_ShowPage(self):
        """
        this method is validating the user is on showpage page or not
        """
        video_icon = verify_element_on_load(self.locator.show_video_play_icon, time=25)
        share_icon = verify_element_on_load(self.locator.share_icon, time=25)
        if (video_icon and share_icon) is not True:
            BuiltIn().fail("Incorrect Page")

    def validate_show_page_with_show_name(self, video_name):
        """
        Validate if the user is on the correct show page by matching the title and video header.

        This keyword contains 1 argument(s):
        - `video_name` (*str*): The expected name of the show to validate against the page content.

        Returns:
        - *`bool`*: Asserts True if both the page title and header match the given show name, otherwise asserts False.
        """
        time.sleep(15)
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        # Scroll_to_element(self.locator.watch_on_demand_header, 100)
        page_title = verify_element(self.locator.page_title.format(video_name))
        video_header_name = se2lib.driver.find_element(By.XPATH, self.locator.show_video_header).text
        if page_title is True and video_header_name == video_name:
            print("On Show Page")
            assert True
        else:
            print("Not on Show Page")
            assert False

    def is_not_signed_in(self):
        """
        Checks if the user is not signed in and returns a tuple with a log message and a boolean value.

        Returns:
        - *tuple*: A tuple containing the result of the visiablity of the 'login_user_name' locator on the page
        and the boolean value `True`.
        """
        log_method("ShowPage", "is not signed in")
        time.sleep(5)
        return verify_element_on_load(self._locators['login_user_name'], 15), True

    def log_in_user(self, user_name, password):
        """
        This function Logs in a user by inputting their username and password and clicking the sign-in button.

        This keyword contains 2 argument(s):
            - `user_name` (*str*): The username of the user trying to log in.
            - `password` (*str*): The password the user is using to log in.
        """
        log_method("ShowPage", "Logging in user")
        try:
            Scroll_to_element(self._locators['login_user_name'])
            self.se2lib.input_text(self._locators['login_user_name'], user_name)
            self.se2lib.input_text(self._locators['login_password'], password)
            Scroll_to_element(self._locators['login_user_name'], 300)
            self.se2lib.click_element(self._locators['btn_sign_in'])
            time.sleep(7)
        except Exception as e:
            log_method("ShowPage", "Error in log in")

    def click_and_play_video_show(self):
        """This function clicks on the play icon from the showpage
        """
        verify_element_and_click(self.locator.show_video_play_icon)

    def get_video_playing_status(self):
        """
        The function Checks whether a video is playing by detecting ads and tracking time differences.

        Returns:
            - *tuple*: Contains two elements:
            - `vtime_list` (*list*): A list of video timestamps collected during playback.
            - `play_time` (*int*): The difference in seconds between the first and last
            detected video times, indicating playback duration.
        """
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        time.sleep(15)
        vtime_list = []
        try:
            mouse_over_to_element(self.locator.video_play_area)
            if se2lib.driver.find_element(By.XPATH, self.locator.ad_duration).is_displayed():
                verify_element_and_click(self.locator.ad_duration)
                vtime = se2lib.driver.find_element(By.XPATH, self.locator.ad_duration).text
                add_time = Get_Seconds_From_Time(vtime)
                time.sleep(add_time+5)
                print("video contains adds")
        except Exception:
            raise Exception("video playback error")
        try:
            for x in range(5):
                action = ActionChains(se2lib.driver)
                self.video = se2lib.driver.find_element(By.XPATH, self.locator.video_play_area)
                action.click_and_hold(self.video).perform()
                time.sleep(2)
                if se2lib.driver.find_element(By.XPATH, self.locator.video_current_time).is_displayed():
                    verify_element_and_click(self.locator.video_current_time)
                    vtime = se2lib.driver.find_element(By.XPATH, self.locator.video_current_time).text
                    vtime_list.append(vtime)
                else:
                    continue
                continue
        except Exception:
            raise Exception("video playback error")
        play_time = Get_Seconds_From_Time(vtime_list[-1]) - Get_Seconds_From_Time(vtime_list[0])
        if play_time != 0:
            print("video is playing")
            assert True
        else:
            print("video is not playing ")
            assert False
        return vtime_list, play_time

    def current_favour_status(self):
        """
        Checks whether the user has already marked an item as liked (favourited).

        Returns:
            - *bool*: `True` if the "already liked" button exists, indicating the
            item is favourited; otherwise `False`.
        """
        if verify_element(self._locators["action_btn_already_like"]):
            return True
        return False

    def get_favour_count(self):
        """
        This function returns the favour count text from either the home page or landing page if the element
        is found, otherwise it prints an error message.

        Return:
        - the text of the "favour count" element on either the home page or the landing page,
        depending on which one is found. If neither element is found, the function prints a message saying
        that the element was not found.
        """
        time.sleep(5)
        if verify_element_on_load(self._locators["action_btn_like"] + self._locators["action_btn_like_count"]):
            return self.se2lib.get_text(self._locators["action_btn_like"] + self._locators["action_btn_like_count"])
        elif verify_element_on_load(self._locators["action_btn_already_like"] + self._locators["action_btn_like_count"]):
            return self.se2lib.get_text(self._locators["action_btn_already_like"] + self._locators["action_btn_like_count"])
        else:
            print("favour count element not found")

    def action_on_favour(self):
        """
        This function performs an action on a "favour" button on a webpage, either clicking it on the
        homepage or on the landing page.
        """
        favour = verify_element_on_load(self._locators["action_btn_like"], 10)
        if favour is True:
            verify_element_and_click(self._locators["action_btn_like"], 10)
        else:
            print("To perform action favour button not found")
        time.sleep(7)

    def user_clicks_on_watchlist(self):
        """
        This function simulates a user clicking on a watchlist button and handles potential errors.
        """
        try:
            if verify_element_on_load(self._locators["watchlist_add_btn"], 25):
                verify_element_on_load(self._locators["watchlist_add_btn"], 25)
                Scroll_to_element(self._locators["watchlist_add_btn"])
                verify_element_and_click(self._locators["watchlist_add_btn"], 10)
            elif verify_element_on_load(self._locators["watchlist_add_btn_ress"], 10):
                Scroll_to_element(self._locators["watchlist_add_btn_ress"])
                verify_element_and_click(self._locators["watchlist_add_btn_ress"], 10)
        except Exception as e:
            print("watchlist button not found")

    def verify_watchlist_icon_and_get_show_name(self):
        """
        This function verifies the watchlist icon change and retrieves the current show name.

        Returns:
        - *`str`*: The title of the show currently displayed if the watchlist icon is present
        """
        Scroll_to_element(self._locators["show_title_header"])
        if verify_element_on_load(self._locators["watchlist_added_btn"], 20) or verify_element_on_load(self._locators["watchlist_added_btn_ress"], 20):
            showname = self.se2lib.driver.find_element(By.XPATH, self._locators["show_title_header"]).text
        return showname

    def validate_show_added_to_watchlist_and_remove(self):
        """
        This function validates that a show has been added to the watchlist and then removes it.
        """
        verify_element_on_load(self._locators["watchlist_header"])
        Scroll_to_element(self._locators["watchlist_header"])
        verify_element(self._locators["watchlist_frist_added_show"])
        verify_element_and_click(self._locators["watchlist_frist_show_more_btn"])
        verify_element_and_click(self._locators["remove_from_watchlist_btn"])
        verify_element_and_click(self._locators["remove_yes"])
        time.sleep(3)

    def user_clicks_on_my_shows(self):
        """
        This function verify and clicks on "My Shows" button on show page
        """
        if verify_element_on_load(self._locators["my_shows"], 25):
            verify_element_and_click(self._locators["my_shows"], 15)
        else:
            verify_element_and_click(self._locators["my_shows_ress"], 15)

    def verify_show_added_to_watchlist_popup(self):
        """
        This function Returns whether the "show added to watchlist" popup is displayed.

        Returns:
        - *`bool`*: `True` if the confirmation popup appears, otherwise `False`.
        """
        if verify_element_on_load(self._locators["popup_added_to_watchlist"], 10):
            return True
        return False

    def handle_show_added_to_watchlist_popup(self):
        """
        This function handles the popup after clicking on watchlist icon by clicking on Ok button
        """
        try:
            verify_element_and_click(self._locators["ok_button_on_popup"], 5)
        except Exception as e:
            print("No Ok button found on popup")

    def user_gets_username_and_actionvalue(self, sortby):
        """
        This function Retrieves the username and action values of commenters based on the selected sorting method.

        This keyword contains 1 argument(s):
        - `sortby` (*str*): Sorting criteria selected by the user. Can be "Most Cheered", "Newest", or "Hot".

        Returns:
        - *`str`*: Username of the first commenter.
        - *`str`*: Action value of the first commenter based on the sorting type.
        - *`str`*: Action value of the fourth commenter based on the sorting type.
        """
        self.user_selects_sortby(sortby)
        first_commenter_name = self.se2lib.driver.find_element(By.XPATH, self._locators["first_commenter_name"]).text
        if sortby == 'Most Cheered':
            action_element_value1 = self.se2lib.driver.find_element(By.XPATH, self._locators["Most_Cheered_count1"]).text
            action_element_value2 = self.se2lib.driver.find_element(By.XPATH, self._locators["Most_Cheered_count4"]).text
        elif sortby == 'Newest':
            action_element_value1 = self.se2lib.driver.find_element(By.XPATH, self._locators["comment_time1"]).text
            action_element_value2 = self.se2lib.driver.find_element(By.XPATH, self._locators["comment_time4"]).text
        elif sortby == 'Hot':
            action_element_value1 = self.se2lib.driver.find_element(By.XPATH, self._locators["Hot_verify_element1"]).text
            action_element_value2 = self.se2lib.driver.find_element(By.XPATH, self._locators["Hot_verify_element4"]).text
        else:
            print("error while getting verification text")
        log_method("ShowPage", first_commenter_name)
        log_method("ShowPage", action_element_value1)
        log_method("ShowPage", action_element_value2)
        return first_commenter_name, action_element_value1, action_element_value2

    def user_selects_sortby(self, sortby):
        """
        Selects a sorting option based on user input and interacts with the respective UI element.

        This keyword contains 1 argument(s):
        - `sortby` (*str*): Sorting option selected by the user. Valid values are "Most Cheered", "Newest",
        or "Hot".
        """
        verify_element_on_load(self._locators["sortby"])
        Scroll_to_element(self._locators["sortby"], 300)
        self.se2lib.click_element(self._locators["sortby"])
        verify_element_on_load(self._locators["sortby_newest_most_cheered"])
        if sortby == 'Most Cheered':
            self.se2lib.click_element(self._locators["sortby_newest_most_cheered"])
        elif sortby == 'Newest':
            self.se2lib.click_element(self._locators["sortby_newest_option"])
        elif sortby == 'Hot':
            self.se2lib.click_element(self._locators["sortby_hot_option"])
        else:
            raise Exception("error while selecting sortby")
        time.sleep(5)

    def get_time_of_update(self, loc, attribute):
        """
        This function Returns the value of a specified attribute from a web element located using XPath.

        This keyword contains 2 argument(s):
        - `loc` (*str*): The XPath locator of the element whose attribute value is to be retrieved.
        This should be a valid XPath expression pointing to the desired web element.
        - `attribute` (*str*): The name of the HTML attribute whose value needs to be fetched.

        Returns:
            - *str*: The value of the specified attribute from the located element, or an empty string if the attribute is not found.
        """
        se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
        ele = se2lib.driver.find_element(By.XPATH, loc)
        return ele.get_attribute(attribute)

    def current_clap_status_comment(self):
        """
        This function Checks the presence of the "clapped" element on the page and returns its status.

        Returns:
        - *bool*: Returns `True` if the "clapped_element" is present on the page, otherwise returns `False`.
        """
        time.sleep(3)
        if verify_element_on_load(self._locators["clapped_element"], 20):
            return True
        return False

    def user_click_on_clap_comment(self):
        """
        This function simulates a user clicking on an upvote button for a comment and includes verification
        and scrolling functions.
        """
        time.sleep(5)
        verify_element_on_load(self._locators["upvote_comment_btn"], 20)
        time.sleep(3)
        Scroll_to_element(self._locators["upvote_comment_btn"], 400)
        verify_element_and_click(self._locators["upvote_comment_btn"])
        time.sleep(2)

    def get_upvote_count_for_comments(self):
        """
        This function retrieves the upvote count for comments if the element is found on the page.

        Returns:
            - *str*: The upvote count for comments as text if the element with the locator "Most_Cheered_count1" is found.
            If the element is not found, prints a message indicating no upvote count was found.
        """
        if verify_element_on_load(self._locators["Most_Cheered_count1"]):
            return self.se2lib.driver.find_element(By.XPATH, self._locators["Most_Cheered_count1"]).text
        else:
            print("no upvote count found")

    def set_window_to_show_replies(self):
        """
        This function sets the window to show replies to the first user comment and scrolls to the first
        reply of the first comment.
        """
        verify_element_on_load(self._locators["first_user_comment"] + self._locators["show_replies_btn"])
        Scroll_to_element(self._locators["first_user_comment"] + self._locators["show_replies_btn"], 300)
        verify_element_and_click(self._locators["first_user_comment"] + self._locators["show_replies_btn"])
        verify_element_on_load(self._locators["first_user_comment"] + self._locators["first_reply_first_comment"])
        Scroll_to_element(self._locators["first_user_comment"] + self._locators["first_reply_first_comment"], 350)

    def current_clap_status_replies(self):
        """
        This function Checks if the "clapped" button is present on the page for replies.

        Returns:
        - *bool*: Returns `True` if the element with the locator "clapped_btn_show_replies" is present on the page for replies,
        otherwise returns `False`.
        """
        self.set_window_to_show_replies()
        if verify_element_on_load(self._locators["first_reply_first_comment"] + self._locators["clapped_btn_show_replies"]):
            return True
        return False

    def user_click_on_clap_replies(self):
        """
        This function scrolls to the first reply and clicks on the clap button to show replies.
        """
        Scroll_to_element(self._locators["first_user_comment"] + self._locators["first_reply_first_comment"], 350)
        verify_element_and_click(self._locators["first_user_comment"] + self._locators["first_reply_first_comment"] + self._locators["clap_btn_show_replies"])

    def get_upvote_count_for_replies(self):
        """
        This function returns the upvote count for replies on a comment if it exists, otherwise it
        prints a message indicating that no upvote count was found.
        Returns:
            - *str*: The upvote count for replies on a comment if found, otherwise prints a message saying "no upvote count found for replies on comment".
        """
        xpath = (
                self._locators["first_user_comment"]
                + self._locators["first_reply_first_comment"]
                + self._locators["vote_count_replies"]
            )
        if verify_element_on_load(xpath):
            return self.se2lib.driver.find_element(By.XPATH, xpath).text
        else:
            print("no upvote count found for replies on comment")

    def user_verify_show_replies_button(self):
        """
        This function verify the visibility of element 'Show_replies_button'
        """
        if verify_element_on_load(self._locators["first_user_comment"] + self._locators["show_replies_btn"]):
            raise Exception("show replies button is visible")
        log_method("CommentAction.py", "show replies button is not visible")
