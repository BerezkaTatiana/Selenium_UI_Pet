from .base_page import BasePage
from .locators import FilterMainPageLocators
from config import NAME_FILTER
from selenium.webdriver.common.keys import Keys

class FilterMainPage(BasePage):
    def filter_main_page_by_cat(self):
        self.browser.find_element(*FilterMainPageLocators.FILTER_DPD).click()
        self.browser.find_element(*FilterMainPageLocators.PET_TYPE_CAT).click()

    def filter_main_page_by_name(self):
        filter_name = self.browser.find_element(*FilterMainPageLocators.FILTER_BY_NAME)
        filter_name.send_keys(NAME_FILTER)
        filter_name.send_keys(Keys.RETURN)