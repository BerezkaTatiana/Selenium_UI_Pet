from .base_page import BasePage
from .locators import EditPetProfileLocators, CreatePetProfileLocators, DeletePetProfileLocators
from config import EDIT_NAME, EDIT_AGE

class EditPetProfile(BasePage):
    def go_to_edit_profile(self):
        pets = self.browser.find_elements(*DeletePetProfileLocators.PETS)
        i= len(pets)
        self.browser.find_elements(*EditPetProfileLocators.EDIT_BTN)[i-1].click()

    def go_to_name(self):
        self.browser.find_element(*EditPetProfileLocators.DOG_NAME)

    def clear_name(self):
        self.browser.find_element(*EditPetProfileLocators.DOG_NAME).clear()

    def go_to_edit_name(self):
        self.browser.find_element(*EditPetProfileLocators.DOG_NAME).send_keys(EDIT_NAME)

    def go_to_type(self):
        self.browser.find_element(*CreatePetProfileLocators.PET_TYPE_DROPDOWN).click()
        self.browser.find_element(*CreatePetProfileLocators.PET_TYPE_DOG).click()

    def go_to_age(self):
        edit_age = self.browser.find_element(*EditPetProfileLocators.DOG_AGE)
        edit_age.clear()

    def go_to_edit_age(self):
        self.browser.find_element(*EditPetProfileLocators.DOG_AGE).send_keys(EDIT_AGE)

    def go_to_save(self):
        save_btn = self.browser.find_element(*EditPetProfileLocators.SAVE_BTN)
        save_btn.click()

