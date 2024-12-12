from .base_page import BasePage
from .locators import DeletePetProfileLocators

class DeletePetProfile(BasePage):
    def go_to_delete_profile(self):
        delete_buttons = self.browser.find_elements(*DeletePetProfileLocators.DELETE_BTN)
        i = len(delete_buttons)
        self.browser.find_elements(*DeletePetProfileLocators.DELETE_BTN)[i-1].click()
        self.browser.find_element(*DeletePetProfileLocators.CONFIRM_BTN).click()

