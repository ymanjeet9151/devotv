import random
import time
from utils.generic_keywords import *
from modules.custom_keywords import *
from PageObjectLibrary import PageObject


class CommentAction(PageObject):
    _locators = {
        "action_btn_comment": "//div[@class='action-btn-col bottom']//following-sibling::div[@class='comment']",
        "comment_list": "//div[@id='commentSectionDiv']",
        "comment_list_header": "//div[contains(@class,'heading d-flex align-items-center')]",
        "total_comment": "//div[contains(@class,'heading d-flex align-items-center')]/span",
        "post_button": "//div[@class='post d-flex align-items-center ml-auto']/button[text()=' Post ']",
        "post_button_reply": "//div[@class='post d-flex align-items-center ml-auto']/button[text()=' Reply ']",
        "post_input": "//div[@id='textAreaDiv']//div[@class='editor']",
        "reply_input": "//div[contains(@id,'comment-textarea')]",
        "show_gif": "//div[@id='dropdownMenuButton']//*[@class='dropdown-toggle']",
        "reply_show_gif": "//*[@class='dropdown-toggle']",
        "show_smilies": "//img[@class='smiley-image']",
        "smily_list": "//section[@*='Smileys & People']//div[2]//span[@class='emoji-mart-emoji']//span",
        "gif_list": "//div[@class='dropdown']/div[@class='dropdown-menu giphy-dropdown show']//img",
        "comment_row": "//div[@class='child-comment']",
        "commentor_user_name": "//div[contains(@class,'custom_comment_margin')]//div[contains(@class,'donor-')]",
        "reply_user_name": "//div[@class='donor-name']",
        "comment_body": "//div[@class='child-comment']//div[contains(@id,'comment-div')]//div[@class='description']",
        "comment_time": "//time[@class='msg-time']//span",
        "comment_delete": "//span[@class='d-flex align-items-center delete']",
        "logged_in_user_name": "//div[@class='avtar-heading']",
        "btn_confirm_delete": "//button[text()=' Yes, Delete ']",
        "comment_reply": "//div[@class='action-col d-flex']/a[@class='reply']",
        "span_reply_count": "//span",
        "reply_comment_row": "//div[@class='comment-reply-row']//div[@class='global-comment-view']",
        "reply_comment": "//div[contains(@id,'comment-textarea')]",
        "flag_report": "//div[@class='global-comment-view']//span[contains(@class,'center report')]",
        "flag_unreport": "//span[@class='d-flex align-items-center reported']",
        "commented_text": "//div[contains(@id,'comment-div')]//div[@class='description']",
        "commented_text_reply": "//div[@class='description']",
        "show_replies": "//div[@class='action-col d-flex']//a[text()='Show Replies ']",
        "hide_replies": "//div[@class='action-col d-flex']//a[text()='Hide Replies ']",
        "first_reply_first_comment": "//div[@class='comment-reply-row']//div[@class='global-comment-view']",
        "first_reply_reported": "//div[@class='comment-reply-row']//div[@class='global-comment-view']//span[contains(@class,'center report')]",
        "show_more_comments_button": "//a[contains(text(),'Show More Comments')]",
        "show_more_comments_replies": "//a[contains(text(),'Show More Replies')]",
      }

    def comment_the_main_video(self, text, add_smily, add_gif, post_type, delete_post):
        """
        This function is used to prepare and post a comment with given text and emoji or GIF as per given details.
        Args:
            text: Text to post
            add_smily: True to add a random smily with comment.
            add_gif: True to add a random GIF with comment.
        """
        log_method("CommentAction", "comment the main video")
        self.go_to_comment_list(text, add_smily, add_gif, post_type, delete_post)

    def go_to_comment_list(self, text, add_smily, add_gif, post_type, delete_post):
        """This function checks if the comment section exists, scrolls to it, calculates the number of replies,
        and prepares and posts a comment with optional smileys and gifs.
        :param text: The text that the user wants to post in the comment section
        :param add_smily: A boolean value indicating whether to add a smiley to the comment or not
        :param add_gif: This parameter is used to determine whether to add a GIF to the comment or not. If
        the value is True, a GIF will be added to the comment. If the value is False, no GIF will be added
        :param post_type: The type of post that the user wants to (eg: comment or reply)
        :param delete_post: A boolean value indicating whether the post should be deleted after the comment
        is posted
        """
        # check if the comment section exists
        if does_element_exist(self._locators["comment_list"]):
            # scorll to the comment section
            Scroll_to_element(self._locators["comment_list"])
            post_index = self.get_post_index(post_type)
            print(f"Calculating replies count")
            self.post_count = self.get_post_count(post_type, post_index)
            print(f"Total comment count is: {self.post_count}")
            self.prepare_and_post(text, add_smily, add_gif, post_type, post_index, delete_post)
        else:
            assert "No defined like button found."

    def get_post_index(self, post_type):
        """The function returns the index of a post based on its type, either "comment" or "reply".
        :param post_type: The type of post being checked, which can be either "comment" or "reply"
        """
        if post_type == "comment":
            return 1
        elif post_type == "reply":
            return 1

    def get_post_count(self, post_type, post_index):
        """
        This function returns the count of either comments or replies based on the input post type and
        index.
        :param post_type: A string indicating the type of post, either "comment" or "reply"
        :param post_index: The index of the post for which the count is being requested
        """
        if post_type == "comment":
            return self.get_current_comment_count()
        elif post_type == "reply":
            return self.get_reply_count(post_index)

    def get_reply_count(self, post_index):
        """This function calculates and returns the number of replies to a post using Selenium web elements.
        :param post_index: The index of the post for which we want to calculate the number of replies
        """
        print(f"Calculating Replies count")
        if verify_element_on_load(self.get_locators("show_replies_count", post_index)):
            reply_count_locator = self.get_locators("show_replies_count", post_index)
        elif verify_element_on_load(self.get_locators("hide_replies_count", post_index)):
            reply_count_locator = self.get_locators("hide_replies_count", post_index)
        else:
            reply_count_locator = "0"
        print(f"reply_count_locator {reply_count_locator}")
        try:
            replies = self.se2lib.get_webelements(reply_count_locator)
            return len(replies)
        except Exception as e:
            return 0

    def get_locators(self, type, index=0, reply_index=0):
        if type == "post_btn":
            return self.get_comment_locator() + self._locators["post_button"]
        elif type == "popup_gif_selector":
            return self.get_comment_locator() + self._locators["show_gif"]
        elif type == "reply_popup_gif_selector":
            return self.get_comment_row(index) + self._locators["reply_show_gif"]
        elif type == "popup_smily_selector":
            return self.get_comment_locator() + self._locators["show_smilies"]
        elif type == "reply_popup_smily_selector":
            return self.get_comment_row(index) + self._locators["show_smilies"]
        elif type == "btn_delete":
            return self.get_comment_row(index)+self._locators["comment_delete"]
        elif type == "reply_btn_delete":
            return self.get_reply_locator(index, reply_index)+self._locators["comment_delete"]
        elif type == "label_reply":
            return self.get_comment_row(index)+self._locators["comment_reply"]
        elif type == "label_time":
            return self.get_comment_row(index)+self._locators["comment_time"]
        elif type == "reply_label_time":
            return self.get_reply_locator(index, reply_index)+self._locators["comment_time"]
        elif type == "label_user_name":
            return self.get_comment_row(index)+self._locators["commentor_user_name"]
        elif type == "reply_label_user_name":
            return self.get_reply_locator(index, reply_index)+self._locators["reply_user_name"]
        elif type == "reply_input":
            return self.get_comment_row(index)+self._locators["reply_input"]
        elif type == "post_btn_reply":
            return self.get_comment_row(index)+self._locators["post_button_reply"]
        elif type == "post_report":
            return self.get_comment_row(index)+self._locators["flag_report"]
        elif type == "post_unreport":
            return self.get_comment_row(index)+self._locators["flag_unreport"]
        elif type == "commented_first_users_name":
            return self.get_comment_row(index)+self._locators["commentor_user_name"]
        elif type == "commented_first_text":
            return self.get_comment_row(index)+self._locators["commented_text"]
        elif type == "show_replies_button":
            return self.get_comment_row(index)+self._locators["show_replies"]
        elif type == "show_replies_count":
            return self.get_comment_row(index)+self._locators["show_replies"]+self._locators["span_reply_count"]
        elif type == "hide_replies_count":
            return self.get_comment_row(index)+self._locators["hide_replies"]+self._locators["span_reply_count"]
        elif type == "reply_label_commented_text":
            return self.get_reply_locator(index, reply_index)+self._locators["commented_text_reply"]

    def get_comment_locator(self):
        """
        This function returns the locator for the comment list.
        """
        return self._locators["comment_list"]

    def get_comment_row(self, index):
        """
        This function returns the locator for a specific comment row based on its index.
        """
        return self._locators["comment_row"] + "["+str(index)+"]"

    def get_reply_locator(self, comment_index, reply_index):
        """
        This function returns the locator for a specific reply comment within a comment thread.
        :param comment_index: The index of the comment row in the page
        :param reply_index: The index of the reply comment within a specific comment thread.
        """
        return self._locators["comment_row"] + "["+str(comment_index)+"]" + self._locators["reply_comment_row"] + "["+str(reply_index)+"]"

    def prepare_and_post(self, text, add_smily, add_gif, post_type, post_index, delete_post):
        """
        This function is used to prepare and post a comment with given text and emoji or GIF as per given details.
        Args:
        text: Text to post
        add_smily: True to add a random smily with comment.
        add_gif: True to add a random GIF with comment.
        """
        log_method("CommentAction", f"Tap on comment icon")
        self.prepare_post(text, add_smily, add_gif, post_type, post_index)
        self.post(post_type, post_index)
        new_post_count = self.get_post_count(post_type, post_index)
        print(f"previous comment count {self.post_count} and new count is: {new_post_count}")
        if new_post_count == self.post_count:
            assert False
        if delete_post is True:
            self.delete_the_recent_post(post_type, post_index)
            time.sleep(10)

    def get_current_comment_count(self):
        """
        This function is used to get the current comment count on show page
        Returns:
        The current comment count
        """
        Scroll_to_element(self._locators["total_comment"], 200)
        log_method("total comment count : ", self.se2lib.get_text(self._locators["total_comment"]))
        return self.se2lib.get_text(self._locators["total_comment"])

    def get_current_replies_count(self):
        """
        This function is used to get the current replies(show_replies) count of first comment on show page
        Returns: The current replies count on comment
        """
        verify_element_on_load(self.get_locators("show_replies_count", 1))
        Scroll_to_element(self.get_locators("show_replies_count", 1))
        return self.se2lib.get_text(self.get_locators("show_replies_count", 1))

    def post(self, post_type, post_index):
        """
        This function is used to post the comment by hitting the post button in post creation container.
        Args: se2lib: Reference to selenium library.
        """
        log_method("CommentAction", f"posting comment")
        locator_post_btn = self.get_post_button(post_type, post_index)
        self.scroll_to_post_reply_button(post_type, post_index)
        verify_element_and_click(locator_post_btn, 15)
        time.sleep(5)

    def get_post_button(self, post_type, post_index):
        """
        This function returns the appropriate locator for a post button based on the post type and index.
        """
        if post_type == "comment":
            return self.get_locators("post_btn")
        elif post_type == "reply":
            return self.get_locators("post_btn_reply", post_index)

    def prepare_post(self, text, add_emoji, add_gif, post_type, post_index):
        """
        This function is used to prepare comment by putting the text, emojis and GIF.
        Args:
        se2lib: The reference to selenium library
        text: Text to post
        add_emoji: True to add a random emoji
        add_gif: True to add a random_gif
        """
        log_method("CommentAction", f"Preparing Comment")
        comment_input_field = self.get_post_input(post_type, post_index)
        log_method("CommentAction", comment_input_field)
        verify_element_on_load(comment_input_field, 20)
        time.sleep(2)
        self.se2lib.input_text(comment_input_field, text)
        if add_emoji:
            self.get_random_emoji(post_type, post_index)
        if add_gif:
            self.get_random_gif(post_type, post_index)
        time.sleep(3)

    def get_post_input(self, post_type, post_index):
        """
        This function returns the input field locator for a post or a reply based on the post type and
        index.
        """
        if post_type == "comment":
            return self._locators["post_input"]
        elif post_type == "reply":
            return self.get_reply_input(post_index)

    def get_reply_input(self, post_index):
        """
        This function returns the locator for the reply input field of a post identified by its index.
        :param post_index: The index of the post for which the reply input is being retrieved
        :return: the locator for the reply input field of a specific post, identified by its index.
        """
        Scroll_to_element(self.get_locators("label_reply", post_index), 200)
        verify_element_and_click(self.get_locators("label_reply", post_index))
        time.sleep(5)
        return self.get_locators("reply_input", post_index)

    def get_random_emoji(self, post_type, post_index):
        """
        The function is used to return a randomly picked emoji.
        Args:
            se2lib: The reference to selenium lib.
        Returns:
        The rendomly picked emoji.
        """
        emoji_selector = "popup_smily_selector" if post_type == "comment" else "reply_popup_smily_selector"
        self.get_random_attachment(emoji_selector, "smily_list", post_type, post_index)

    def get_random_gif(self, post_type, post_index):
        """
        The function is used to return a randomly picked gif.
        Args:
            se2lib: The reference to selenium lib.
        Returns:
        The rendomly picked gif.
        """
        gif_selector = "popup_gif_selector" if post_type == "comment" else "reply_popup_gif_selector"
        self.get_random_attachment(gif_selector, "gif_list", post_type, post_index)

    def get_random_attachment(self, popup_selector, list, post_type, post_index):
        """
        The function is used to return a randomly picked attachement(emoji/gif).
        Args:
        se2lib: The reference to selenium lib.
        pop_selector: The reference to gif/emoji popup to choose attachement from.
        list: The reference to gif/emoji list to choose attachement from.
        Returns:
        The rendomly picked attachement.
        """
        log_method("CommentAction", f"Get random attachments {list}")
        popup_locator = self.get_locators(popup_selector, post_index)
        print(f"Random attachment locator: {popup_locator}")
        Scroll_to_element(popup_locator, 200)
        verify_element_and_click(popup_locator)
        time.sleep(5)
        attachment_list = self.se2lib.get_webelements(self._locators[list])
        list_count = len(attachment_list)
        if list_count > 0:
            random_index = random.randint(1, list_count - 1)
            print(f'got {list_count} smilies and selecting {random_index}')
            attachment = attachment_list[random_index]
            time.sleep(3)
            Scroll_to_element(self._locators["post_input"])
            # self.scroll_to_location(self.se2lib,attachment.location)
            # label_comment_row = self.get_post_label_comment_row(post_type,post_index, reply_index=1)
            # Scroll_to_element(label_comment_row)
            self.se2lib.click_element(attachment)
            time.sleep(4)
        else:
            print(f"Din't pick any {list} attachments")
            self.se2lib.click_element(self.get_locators(popup_selector))

    def delete_the_recent_post(self, post_type, post_index):
        """
        The function is used to delete the most recent comment of logged in user
        This function only can be used wherever time will be "just now"
        Args:
        se2lib: The reference to selenium library
        """
        log_method("CommentAction", "Deleting the most recent comment by this user")
        logged_in_user = self.se2lib.get_text(self._locators["logged_in_user_name"])
        comments = self.se2lib.get_webelements(self._locators["comment_row"])
        self.delete_user_post(post_index, post_type, comments, logged_in_user)
        time.sleep(4)
        new_post_count = self.get_post_count(post_type, post_index)
        print(f"Comment deleted Successfully {new_post_count}")
        if new_post_count != self.post_count:
            assert False

    def delete_user_post(self, post_index, post_type, comments, logged_in_user):
        """This function deletes a user post and its associated comments if the logged-in user is the author of
        the post.
        :param post_index: The index of the post that needs to be deleted
        :param post_type: The type of post, which can be either "comment" or "reply"
        :param comments: a list of dictionaries containing details of comments on a post
        :param logged_in_user: This parameter represents the user who is currently logged in and trying to
        delete their post
        """
        print(f"Deleting user post with details:post_type {post_type}, post_index: {post_index}")
        index = 1
        for comment in comments:
            if self.is_posted_by_logged_in_user(logged_in_user, index, post_type, index) and post_index == index:
                self.confirm_comment_deletion(post_type, post_index, self.get_reply_index(logged_in_user, post_type, post_index))
                break
            index = index + 1

    def get_reply_index(self, logged_in_user, post_type, post_index):
        """
        This function returns the index of a reply to a post or comment made by a logged-in user.
        :param logged_in_user: The username of the user who is currently logged in
        :param post_type: The type of post, which can be either "comment" or "reply"
        :param post_index: The index of the post or comment for which we want to find the reply index
        """
        if post_type == "comment":
            return 0
        replies_locator = self._locators["comment_row"] + "["+str(post_index)+"]" + self._locators["reply_comment_row"]
        replies = self.se2lib.get_webelements(replies_locator)
        index = 1
        for reply in replies:
            if self.is_posted_by_logged_in_user(logged_in_user, post_index, post_type, index):
                return index
            index = index + 1

    def confirm_comment_deletion(self, post_type, post_index, reply_index=0):
        """
        The function is used to confirm the automated user action for the last time to delete the comment.
        Args:
        se2lib: The reference to selenium lib.
        index: The index of comment row to be deleted.
        """
        button_delete = self.get_post_delete_button(post_type, post_index, reply_index)
        label_comment_row = self.get_post_label_comment_row(post_type, post_index, reply_index)
        log_method("commnetAction", label_comment_row)
        Scroll_to_element(label_comment_row, 200)
        mouse_over_to_element(label_comment_row)
        verify_element_and_click(button_delete)
        time.sleep(4)
        if does_element_exist(self._locators["btn_confirm_delete"]):
            self.se2lib.click_element(self._locators["btn_confirm_delete"])

    def get_post_delete_button(self, post_type, post_index, reply_index):
        """
        This function returns the appropriate delete button locator based on the post type, post index, and
        reply index.
        """
        if post_type == "comment":
            return self.get_locators("btn_delete", post_index)
        elif post_type == "reply":
            return self.get_locators("reply_btn_delete", post_index, reply_index)

    def get_post_label_comment_row(self, post_type, post_index, reply_index):
        """
        This function returns the locator for the label comment row of a post or reply based on its type and index.
        """
        if post_type == "comment":
            return self.get_comment_row(post_index)
        elif post_type == "reply":
            return self.get_reply_locator(post_index, reply_index=reply_index)

    def is_posted_by_logged_in_user(self, logged_in_user, index, post_type, reply_index=0):
        """
        This function checks if the logged-in user has posted a certain type of post or reply just now.
        """
        return self.is_current_user(logged_in_user, index, post_type, reply_index) and self.is_posted_just_now(index, post_type, reply_index)

    def is_current_user(self, logged_in_user, index, post_type, reply_index):
        """
        This function checks if the logged-in user is the same as the user who made a comment or reply.
        """
        locator_label = "label_user_name" if post_type == "comment" else "reply_label_user_name"
        return self.se2lib.get_text(self.get_locators(locator_label, index, reply_index)).lower() == logged_in_user.lower()

    def is_posted_just_now(self, index, post_type, reply_index):
        """
        This function checks if a post or comment was posted just now.
        """
        locator_label = "label_time" if post_type == "comment" else "reply_label_time"
        return self.se2lib.get_text(self.get_locators(locator_label, index, reply_index)) == "Just now"

    def replying_on_first_comment(self, text, add_smily, add_gif, post_type, delete_post):
        """
        This function is used to prepare and post a comment with given text and emoji or GIF as per given details.
        Args:
        text: Text to post
        add_smily: True to add a random smily with comment.
        add_gif: True to add a random GIF with comment.
        """
        log_method("CommentAction", "reply to a comment on the main video")
        self.go_to_comment_list(text, add_smily, add_gif, post_type, delete_post)

    def scroll_to_post_reply_button(self, post_type, post_index):
        """This function scrolls to the post reply button based on the post type and index.
        :param post_type: A string indicating the type of post, either "comment" or "reply"
        :param post_index: The index of the post or comment for which the reply button needs to be scrolled
        to
        """
        if post_type == 'comment':
            verify_element_on_load(self._locators["post_button"])
            Scroll_to_element(self._locators["post_button"], 300)
        elif post_type == 'reply':
            verify_element_on_load(self.get_locators("post_btn_reply", post_index))
            Scroll_to_element(self.get_locators("post_btn_reply", post_index), 300)
        else:
            print("post reply button not found")

    def scroll_commentSection_into_view(self):
        """This function scrolls the comment section into view if the first comment row exists.
        """
        if does_element_exist(self.get_comment_row(1)):
            Scroll_to_element(self.get_comment_row(1))

    def click_on_report_flag(self):
        """This function clicks on a report flag for a post and verifies that the post is reported and can be
        unreported.
        """
        time.sleep(5)
        mouse_over_to_element(self.get_locators("post_report", 1))
        verify_element_on_load(self.get_locators("post_report", 1))
        self.se2lib.click_element(self.get_locators("post_report", 1))
        verify_element_on_load(self.get_locators("post_unreport", 1))

    def click_on_reported_flag(self):
        """This function clicks on a reported flag and verifies the unreport and report elements.
        """
        mouse_over_to_element(self.get_locators("post_unreport", 1))
        verify_element_on_load(self.get_locators("post_unreport", 1))
        self.se2lib.click_element(self.get_locators("post_unreport", 1))
        verify_element_on_load(self.get_locators("post_report", 1))

    def get_name_and_commented_text(self, count):
        """This function retrieves the usernames and commented text of a specified number of comments and
        returns them as lists.
        :param count: The parameter "count" is a list of integers that represents the index of the comments
        on a webpage. The function uses these indices to locate and extract the username and commented text
        of each comment
        :return: two lists, `get_username` and `get_comment`, which contain the usernames and commented text
        of the specified number of comments (specified by the `count` parameter).
        """
        get_username = []
        get_comment = []
        for i in count:
            verify_element_on_load(self.get_locators("commented_first_users_name", f"{i}"))
            data_username = self.se2lib.driver.find_element(By.XPATH, self.get_locators("commented_first_users_name", f"{i}")).text
            data_comment = self.se2lib.driver.find_element(By.XPATH, self.get_locators("commented_first_text", f"{i}")).text
            print("the username and comment text are : "f"{data_username} and {data_comment}")
            get_username.append(data_username.lower())
            get_comment.append(data_comment)
            print(get_username, get_comment)
        return get_username, get_comment

    def get_name_and_replied_text(self, count):
        """
        This function retrieves the username and commented text from a web page and returns them as lists.
        :param count: It is a list of integers representing the indices of the comments for which we want to
        retrieve the username and replied text
        :return: two lists, `get_username` and `get_comment`, which contain the usernames and commented text
        respectively, for each element in the `count` list.
        """
        get_username = []
        get_comment = []
        for i in count:
            verify_element_on_load(self.get_locators("reply_label_user_name", 1, f"{i}"))
            data_username = self.se2lib.driver.find_element(By.XPATH, self.get_locators("reply_label_user_name", 1, f"{i}")).text
            data_comment = self.se2lib.driver.find_element(By.XPATH, self.get_locators("reply_label_commented_text", 1, f"{i}")).text
            print("the username and comment text are : "f"{data_username} and {data_comment}")
            get_username.append(data_username.lower())
            get_comment.append(data_comment)
            print(get_username, get_comment)
        return get_username, get_comment

    def click_on_show_replies(self):
        """
        This function clicks on a "show replies" button after verifying its presence and scrolling to it.
        """
        verify_element_on_load(self.get_locators("show_replies_button", 1))
        Scroll_to_element(self.get_locators("show_replies_button", 1), 300)
        self.se2lib.click_element(self.get_locators("show_replies_button", 1))
        time.sleep(3)

    def scroll_to_frist_reply(self):
        """
        This function scrolls to the first reply in a comment section if it is present on the page.
        """
        if verify_element_on_load(self._locators["first_reply_first_comment"], 15):
            Scroll_to_element(self._locators["first_reply_first_comment"])
            time.sleep(3)

    def click_on_report_flag_for_reply(self):
        """
        This Fucntion is used to click on report falg under the reply section
        """
        time.sleep(2)
        Scroll_to_element(self._locators["first_reply_first_comment"] + self._locators["flag_report"], 200)
        verify_element_on_load(self._locators["first_reply_first_comment"] + self._locators["flag_report"])
        mouse_over_to_element(self._locators["first_reply_first_comment"])
        self.se2lib.click_element(self._locators["first_reply_first_comment"] + self._locators["flag_report"])
        verify_element_on_load(self._locators["first_reply_reported"])

    def click_on_reported_flag_for_reply(self):
        """This function clicks on the reported flag for a reply and verifies the element on load.
        """
        time.sleep(3)
        mouse_over_to_element(self._locators["first_reply_reported"])
        verify_element_on_load(self._locators["first_reply_reported"])
        self.se2lib.click_element(self._locators["first_reply_reported"])
        verify_element_on_load(self._locators["first_reply_first_comment"] + self._locators["flag_report"])

    def delete_the_recent_post_for_report(self, post_type="comment"):
        """
        This function is used to Delete the recent comment post on any show of current user
        This function can be used anywhere, As time will be "just now", 1 min ago, and so on.
        """
        logged_in_user = self.se2lib.get_text(self._locators["logged_in_user_name"])
        if self.is_current_user(logged_in_user, index=1, post_type="comment", reply_index=0):
            post_index = 1
            self.confirm_comment_deletion(post_type, post_index, self.get_reply_index(logged_in_user, post_type, post_index))
            time.sleep(4)
        else:
            log_method("commmetAction", "error in delete the recent post for report")

    def click_on_show_more_comments(self, count):
        """
        This fucntion is used to click on 'show more comments' button on show page
        Args: count: Number of times user wants to click
        """
        for i in range(int(count)):
            verify_element_on_load(self._locators["show_more_comments_button"])
            Scroll_to_element(self._locators["show_more_comments_button"], 200)
            self.se2lib.click_element(self._locators["show_more_comments_button"])

    def user_replaces_characters(self, string):
        """
        This function is used to replace the characters with given characters.
        Args: string: the string value taken under the action
        """
        my_string = (f"{string}").replace("<p>", "").replace("</p>", "").replace("<div>", "")
        print(my_string)
        return my_string

    def click_on_show_more_replies(self, count):
        """
        This fucntion is used to click on 'show more comments' button on show page
        Args: count: Number of times user wants to click
        """
        for i in range(int(count)):
            verify_element_on_load(self._locators["show_more_comments_replies"])
            Scroll_to_element(self._locators["show_more_comments_replies"], 200)
            self.se2lib.click_element(self._locators["show_more_comments_replies"])
