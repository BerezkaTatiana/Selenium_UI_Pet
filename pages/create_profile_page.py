from .base_page import BasePage
from .locators import CreatePetProfileLocators
from config import PET_NAME, PET_AGE

class CreateProfilePage(BasePage):

    def go_to_pet_name(self):
        pet_name = self.browser.find_element(*CreatePetProfileLocators.PET_NAME)
        pet_name.send_keys(PET_NAME)

    def go_to_pet_type(self):
        pet_type = self.browser.find_element(*CreatePetProfileLocators.PET_TYPE_DROPDOWN)
        pet_type.click()
        pet_dog = self.browser.find_element(*CreatePetProfileLocators.PET_TYPE_DOG)
        pet_dog.click()

    def go_to_pet_age(self):
        pet_age = self.browser.find_element(*CreatePetProfileLocators.PET_AGE)
        pet_age.send_keys(PET_AGE)

    def go_to_pet_gender(self):
        pet_gender = self.browser.find_element(*CreatePetProfileLocators.PET_GENDER)
        pet_gender.click()
        pet_gender_male = self.browser.find_element(*CreatePetProfileLocators.PET_GENDER_MALE)
        pet_gender_male.click()

    def go_to_pet_submit(self):
        pet_submit = self.browser.find_element(*CreatePetProfileLocators.PET_SUBMIT)
        pet_submit.click()







