import pytest
from pages.edit_pet_profile import EditPetProfile
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import TIMEOUT
from pages.locators import EditPetProfileLocators

@pytest.mark.regression
def test_edit_profile(browser, login, edit):
    wait = WebDriverWait(browser, TIMEOUT)
    page = EditPetProfile(browser, edit)
    page.open()
    page.go_to_name()
    page.clear_name()
    wait.until(ec.text_to_be_present_in_element_value(EditPetProfileLocators.DOG_NAME, ''))
    page.go_to_edit_name()
    page.go_to_type()
    page.go_to_age()
    wait.until(ec.text_to_be_present_in_element_value(EditPetProfileLocators.DOG_AGE, ''))
    page.go_to_edit_age()
    page.go_to_save()
    browser.save_screenshot('edit_profile.png')


