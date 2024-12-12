from .base_page import BasePage
from .locators import LikeCommentMainPageLocators
from config import COMMENT

class LikeCommentMainPage(BasePage):
    def go_to_profile(self):
        self.browser.find_element(*LikeCommentMainPageLocators.LOGO).click()

    def like(self):
        self.browser.find_element(*LikeCommentMainPageLocators.LIKE_BTN).click()

    def details(self):
        self.browser.find_element(*LikeCommentMainPageLocators.DETAILS_BTN).click()

    def comment(self):
        self.browser.find_element(*LikeCommentMainPageLocators.EDITOR).send_keys(COMMENT)
        self.browser.find_element(*LikeCommentMainPageLocators.SAVE_COMMENT_BTN).click()

