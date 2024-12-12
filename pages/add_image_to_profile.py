import os
from .base_page import BasePage
from .locators import AddImageToPetLocators

class AddImageToPetProfile(BasePage):

    def go_to_add_image(self):
        self.browser.find_element(*AddImageToPetLocators.PET_IMAGE).click()

    def go_to_upload_image(self):
        upload_image = os.path.abspath("dog1.jpg")
        pet_image = self.browser.find_element(*AddImageToPetLocators.PLUS_BTN)
        pet_image.send_keys(upload_image)

    def go_to_click(self):
        self.browser.find_element(*AddImageToPetLocators.PLUS_BTN).click()



