import random
import time
from utils.generic_keywords import *
from modules.custom_keywords import *
from PageObjectLibrary import PageObject


class CommentAction(PageObject):
    """
    A Page Object class that provides methods to interact with the comment section on a webpage.

    This class contains locators & functions for elements related to comments, such as comment buttons, input fields,
    emoji options, and actions for posting, replying, deleting, and managing comments.
    """
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
        This function is used to pPrepares and posts a comment on the main video with optional text, emoji, or GIF.

        This keyword contains 5 arguments:
            - `text` (*str*): The comment text to be posted.
            - `add_smily` (*bool*): Set to True to include a random emoji in the comment.
            - `add_gif` (*bool*): Set to True to include a random GIF in the comment.
            - `post_type` (*str*): Specifies the type of post action to perform.
            - `delete_post` (*bool*): Set to True if the comment should be deleted after posting.
        """
        log_method("CommentAction", "comment the main video")
        self.go_to_comment_list(text, add_smily, add_gif, post_type, delete_post)

    def go_to_comment_list(self, text, add_smily, add_gif, post_type, delete_post):
        """This function  Navigates to the comment section, calculates existing replies, and posts a comment with optional
        emoji or GIF.

        This keyword contains 5 arguments:
            - `text` (*str*): The comment text to be posted.
            - `add_smily` (*bool*): Set to True to include a random emoji in the comment.
            - `add_gif` (*bool*): Set to True to include a random GIF in the comment.
            - `post_type` (*str*): Specifies the type of post action (e.g., "comment" or "reply").
            - `delete_post` (*bool*): Set to True if the comment should be deleted after posting.
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
        """
        This function Returns the index of a post based on its type.

        This keyword contains 1 argument:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
        """
        if post_type == "comment":
            return 1
        elif post_type == "reply":
            return 1

    def get_post_count(self, post_type, post_index):
        """
        This function Returns the count of comments or replies based on the given post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post to retrieve the count for.
        """
        if post_type == "comment":
            return self.get_current_comment_count()
        elif post_type == "reply":
            return self.get_reply_count(post_index)

    def get_reply_count(self, post_index):
        """
        This function Calculates and returns the number of replies for a given post index.

        This keyword contains 1 argument:
            - `post_index` (*int*): The index of the post for which the reply count is to be calculated.
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
        """
        Returns the locator string based on the specified type and indices for the comment or reply.

        This keyword contains 3 arguments:
            - `type` (*str*): The type of locator to be retrieved (e.g., "post_btn", "popup_gif_selector").
            - `index` (*int*, optional): The index of the comment or post. Defaults to 0.
            - `reply_index` (*int*, optional): The index of the reply. Defaults to 0.

        Returns:
            - `str`: The locator string based on the specified type and indices.
        """
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
        Returns the locator string for the comment list.

        Returns:
            - `str`: The locator string for the comment list.
        """
        return self._locators["comment_list"]

    def get_comment_row(self, index):
        """
        This function Returns the locator string for a specific comment row based on the provided index.

        Args:
            - `index` (*int*): The index of the comment row.

        Returns:
            - `str`: The locator string for the specific comment row.
        """
        return self._locators["comment_row"] + "["+str(index)+"]"

    def get_reply_locator(self, comment_index, reply_index):
        """
        This function Returns the locator string for a specific reply comment within a comment thread.

        This keyword contains 2 arguments:
            - `comment_index` (*int*): The index of the comment row.
            - `reply_index` (*int*): The index of the reply comment within the specific comment thread.

        Returns:
            - `str`: The locator string for the specific reply comment.
        """
        return self._locators["comment_row"] + "["+str(comment_index)+"]" + self._locators["reply_comment_row"] + "["+str(reply_index)+"]"

    def prepare_and_post(self, text, add_smily, add_gif, post_type, post_index, delete_post):
        """
        This function is used to prepare and post a comment with given text and emoji or GIF as per given details.

        This keyword contains 6 arguments:
            - `text` (*str*): The text to be posted in the comment or reply.
            - `add_smily` (*bool*): Set to True to include a random emoji in the comment or reply.
            - `add_gif` (*bool*): Set to True to include a random GIF in the comment or reply.
            - `post_type` (*str*): Specifies the type of post ("comment" or "reply").
            - `post_index` (*int*): The index of the post for which the comment or reply is being made.
            - `delete_post` (*bool*): Set to True to delete the post after it is made.

        Raises:
            - Asserts if the post count hasn't changed after posting.
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
            - `str`: The current comment count displayed on the page.
        """
        Scroll_to_element(self._locators["total_comment"], 200)
        log_method("total comment count : ", self.se2lib.get_text(self._locators["total_comment"]))
        return self.se2lib.get_text(self._locators["total_comment"])

    def get_current_replies_count(self):
        """
        Retrieves the current replies count for the first comment on the show page.

        Returns:
            - `str`: The current replies count for the first comment displayed on the page.
        """
        verify_element_on_load(self.get_locators("show_replies_count", 1))
        Scroll_to_element(self.get_locators("show_replies_count", 1))
        return self.se2lib.get_text(self.get_locators("show_replies_count", 1))

    def post(self, post_type, post_index):
        """
        This function is used to Posts a comment or reply by clicking the appropriate post button.

        This keyword contains 2 arguments::
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post or reply to be submitted.

        Raises:
            - Clicks the post button for the specified post type and index.
        """
        log_method("CommentAction", f"posting comment")
        locator_post_btn = self.get_post_button(post_type, post_index)
        self.scroll_to_post_reply_button(post_type, post_index)
        verify_element_and_click(locator_post_btn, 15)
        time.sleep(5)

    def get_post_button(self, post_type, post_index):
        """
        This function returns the appropriate locator for a post button based on the post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post or reply.

        Returns:
            - `str`: The locator for the post button corresponding to the given type and index.
        """
        if post_type == "comment":
            return self.get_locators("post_btn")
        elif post_type == "reply":
            return self.get_locators("post_btn_reply", post_index)

    def prepare_post(self, text, add_emoji, add_gif, post_type, post_index):
        """
        This function is used to prepare comment by putting the text, emojis and GIF.

        This keyword contains 5 arguments:
            - `text` (*str*): The text to post in the comment.
            - `add_emoji` (*bool*): Set to True to add a random emoji to the comment.
            - `add_gif` (*bool*): Set to True to add a random GIF to the comment.
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post or reply to which the comment is being added.
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
        This function Returns the input field locator for a post or a reply based on the post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post or reply to retrieve the input field for.

        Returns:
            - (*str*): The locator for the input field of the specified post type and index.
        """
        if post_type == "comment":
            return self._locators["post_input"]
        elif post_type == "reply":
            return self.get_reply_input(post_index)

    def get_reply_input(self, post_index):
        """
        This function Returns the locator for the reply input field of a post identified by its index.

        This keyword contains 1 argument::
            - `post_index` (*int*): The index of the post for which the reply input is being retrieved.

        Returns:
            - (*str*): The locator for the reply input field of the specified post.
        """
        Scroll_to_element(self.get_locators("label_reply", post_index), 200)
        verify_element_and_click(self.get_locators("label_reply", post_index))
        time.sleep(5)
        return self.get_locators("reply_input", post_index)

    def get_random_emoji(self, post_type, post_index):
        """
        Returns a randomly picked emoji based on the post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post to which the emoji is being added.

        Returns:
            - (*None*): The function does not return any value but performs actions to add the emoji.
        """
        emoji_selector = "popup_smily_selector" if post_type == "comment" else "reply_popup_smily_selector"
        self.get_random_attachment(emoji_selector, "smily_list", post_type, post_index)

    def get_random_gif(self, post_type, post_index):
        """
        The function is used to Returns a randomly picked GIF based on the post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post to which the GIF is being added.

        Returns:
            - (*None*): The function does not return any value but performs actions to add the GIF.
        """
        gif_selector = "popup_gif_selector" if post_type == "comment" else "reply_popup_gif_selector"
        self.get_random_attachment(gif_selector, "gif_list", post_type, post_index)

    def get_random_attachment(self, popup_selector, list, post_type, post_index):
        """
        The function is used to Returns a randomly picked attachment (emoji or GIF) based on the provided parameters.

        This keyword contains 4 arguments:
            - `popup_selector` (*str*): The reference to the popup selector for the emoji or GIF.
            - `list` (*str*): The reference to the list of attachments (either "smily_list" or "gif_list").
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post to which the attachment is being added.

        Returns:
            - (*None*): The function performs the action of selecting a random attachment but does not return a value.
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
        The function is used to Deletes the most recent comment of the logged-in user.

        This keyword contains 2 arguments:
            - `post_type` (*str*): The type of post to delete ("comment" or "reply").
            - `post_index` (*int*): The index of the post to be deleted.

        Returns:
            - (*None*): The function performs the deletion action but does not return a value.
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
        """This function Deletes a user post and its associated comments if the logged-in user is the author of the post.

        This keyword contains 4 arguments:
            - `post_index` (*int*): The index of the post to be deleted.
            - `post_type` (*str*): The type of post, which can be either "comment" or "reply".
            - `comments` (*list*): A list of dictionaries containing details of comments on a post.
            - `logged_in_user` (*str*): The username of the currently logged-in user trying to delete their post.

        Returns:
            - (*None*): This function performs the deletion action but does not return a value.
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

        This keyword contains 3 arguments:
            - `logged_in_user` (*str*): The username of the user who is currently logged in.
            - `post_type` (*str*): The type of post, which can be either "comment" or "reply".
            - `post_index` (*int*): The index of the post or comment for which we want to find the reply index.

        Returns:
            - (*int*): The index of the reply made by the logged-in user, or 0 if no reply is found for a comment.
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

        This keyword contains 3 arguments:
            - `post_type` (*str*): The type of post, which can be either "comment" or "reply".
            - `post_index` (*int*): The index of the post (comment or reply) to be deleted.
            - `reply_index` (*int*, optional): The index of the reply (default is 0).

        Returns:
            None: The function performs an action but does not return any value.
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

        This keyword contains 3 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post (comment or reply).
            - `reply_index` (*int*): The index of the reply, relevant when `post_type` is "reply".

        Returns:
            - (*str*): The locator for the delete button corresponding to the provided post type and indices.
        """
        if post_type == "comment":
            return self.get_locators("btn_delete", post_index)
        elif post_type == "reply":
            return self.get_locators("reply_btn_delete", post_index, reply_index)

    def get_post_label_comment_row(self, post_type, post_index, reply_index):
        """
        This function returns the locator for the label comment row of a post or reply based on its type and index.

        This keyword contains 3 arguments:
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post (comment or reply).
            - `reply_index` (*int*): The index of the reply, relevant when `post_type` is "reply".

        Returns:
            - (*str*): The locator for the label comment row corresponding to the provided post type and indices.
        """
        if post_type == "comment":
            return self.get_comment_row(post_index)
        elif post_type == "reply":
            return self.get_reply_locator(post_index, reply_index=reply_index)

    def is_posted_by_logged_in_user(self, logged_in_user, index, post_type, reply_index=0):
        """
        This function checks if the logged-in user has posted a certain type of post or reply just now.

        This keyword contains 4 arguments:
            - `logged_in_user` (*str*): The username of the logged-in user.
            - `index` (*int*): The index of the post (comment or reply).
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `reply_index` (*int*, optional): The index of the reply, relevant when `post_type` is "reply" (default is 0).

        Returns:
            - (*bool*): Returns True if the logged-in user posted the comment or reply just now; False otherwise.
        """
        return self.is_current_user(logged_in_user, index, post_type, reply_index) and self.is_posted_just_now(index, post_type, reply_index)

    def is_current_user(self, logged_in_user, index, post_type, reply_index):
        """
        This function checks if the logged-in user is the same as the user who made a comment or reply.

        This keyword contains 4 arguments:
            - `logged_in_user` (*str*): The username of the logged-in user.
            - `index` (*int*): The index of the post (comment or reply).
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `reply_index` (*int*): The index of the reply, relevant when `post_type` is "reply".

        Returns:
            - (*bool*): Returns True if the logged-in user is the same as the user who made the comment or reply; False otherwise.
        """
        locator_label = "label_user_name" if post_type == "comment" else "reply_label_user_name"
        return self.se2lib.get_text(self.get_locators(locator_label, index, reply_index)).lower() == logged_in_user.lower()

    def is_posted_just_now(self, index, post_type, reply_index):
        """
        This function checks if a post or comment was posted just now.

        This keyword contains 3 arguments:
            - `index` (*int*): The index of the post (comment or reply).
            - `post_type` (*str*): The type of post, either "comment" or "reply".
            - `reply_index` (*int*): The index of the reply, relevant when `post_type` is "reply".

        Returns:
            - (*bool*): Returns True if the post or comment was posted just now; False otherwise.
        """
        locator_label = "label_time" if post_type == "comment" else "reply_label_time"
        return self.se2lib.get_text(self.get_locators(locator_label, index, reply_index)) == "Just now"

    def replying_on_first_comment(self, text, add_smily, add_gif, post_type, delete_post):
        """
        This function is used to prepare and post a reply to the first comment with the given text, emoji, or GIF.

        This keyword contains 5 arguments:
            - `text` (*str*): The text content to post in the reply.
            - `add_smily` (*bool*): Set to True to add a random smiley to the reply.
            - `add_gif` (*bool*): Set to True to add a random GIF to the reply.
            - `post_type` (*str*): The type of the post, either "comment" or "reply".
            - `delete_post` (*bool*): Set to True to delete the post after it's made.
        """
        log_method("CommentAction", "reply to a comment on the main video")
        self.go_to_comment_list(text, add_smily, add_gif, post_type, delete_post)

    def scroll_to_post_reply_button(self, post_type, post_index):
        """
        This function scrolls to the post reply button based on the post type and index.

        This keyword contains 2 arguments:
            - `post_type` (*str*): A string indicating the type of post, either "comment" or "reply".
            - `post_index` (*int*): The index of the post or comment for which the reply button needs to be scrolled to.
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
        """
        This function clicks the report flag on a post to report it,
        and then verifies that the post can be unreported.
        It waits for the elements to load, moves the mouse over the report flag,
        clicks it, and checks if the unreport option is visible.
        """
        time.sleep(5)
        mouse_over_to_element(self.get_locators("post_report", 1))
        verify_element_on_load(self.get_locators("post_report", 1))
        self.se2lib.click_element(self.get_locators("post_report", 1))
        verify_element_on_load(self.get_locators("post_unreport", 1))

    def click_on_reported_flag(self):
        """
        This function clicks the unreport flag on a reported post to unreport it,
        then verifies that the report flag is visible again.
        It waits for the elements to load, moves the mouse over the unreport flag,
        clicks it, and checks if the report option is visible.
        """
        mouse_over_to_element(self.get_locators("post_unreport", 1))
        verify_element_on_load(self.get_locators("post_unreport", 1))
        self.se2lib.click_element(self.get_locators("post_unreport", 1))
        verify_element_on_load(self.get_locators("post_report", 1))

    def get_name_and_commented_text(self, count):
        """
        This function retrieves the usernames and commented text of multiple comments based on the provided indices.
        It returns two lists: one with the usernames and the other with the corresponding commented text.

        This keyword contains 1 argument:
        - `count`: A list of integers representing the indices of the comments on the webpage.
            The function extracts the username and comment text for each index in the list.

        :return: Two lists:
            - `get_username`: Contains the usernames of the specified comments.
            - `get_comment`: Contains the corresponding comment text of the specified comments.
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
        This function retrieves the usernames and replied text of multiple comments based on the provided indices.
        It returns two lists: one with the usernames and the other with the corresponding replied text.

        This keyword contains 1 argument:
        - `count`: A list of integers representing the indices of the comments for which the username and replied text are retrieved.

        Return:
        - `get_username`: A list of usernames of the specified comments.
        - `get_comment`: A list of corresponding replied texts.
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
        This function is used to delete the most recent comment post by the current user on any show.
        It works for posts with time stamps such as "just now", "1 min ago", etc.

        This keyword contains 1 argument:
            - `post_type` (*`str`*): The type of post to delete (default is "comment").
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
        This function clicks on the "show more comments" button on the show page multiple times.

        This keyword contains 1 argument:
        - `count` (*`int`*): The number of times the user wants to click on the "show more comments" button.
        """
        for i in range(int(count)):
            verify_element_on_load(self._locators["show_more_comments_button"])
            Scroll_to_element(self._locators["show_more_comments_button"], 200)
            self.se2lib.click_element(self._locators["show_more_comments_button"])

    def user_replaces_characters(self, string):
        """
        This function replaces certain HTML tags in a string with an empty string.

        This keyword contains 1 argument:
        - `string` (*`str`*): The string value in which HTML tags will be replaced.

        Return:
        - *`str`*: The string after replacing `<p>`, `</p>`, and `<div>` tags.
        """
        my_string = (f"{string}").replace("<p>", "").replace("</p>", "").replace("<div>", "")
        print(my_string)
        return my_string

    def click_on_show_more_replies(self, count):
        """
        This function clicks on the 'show more replies' button on a show page multiple times based on the provided count.

        This keyword contains 1 argument:
        - `count` (*`int`*): The number of times the user wants to click the 'show more replies' button.
        """
        for i in range(int(count)):
            verify_element_on_load(self._locators["show_more_comments_replies"])
            Scroll_to_element(self._locators["show_more_comments_replies"], 200)
            self.se2lib.click_element(self._locators["show_more_comments_replies"])
