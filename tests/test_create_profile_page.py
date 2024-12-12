import pytest
from pages.create_profile_page import CreateProfilePage
from config import NEW_PROFILE_URL

@pytest.mark.smoke
def test_go_to_create_profile(browser, login):
    page = CreateProfilePage(browser, NEW_PROFILE_URL)
    page.open()
    page.go_to_pet_name()
    page.go_to_pet_type()
    page.go_to_pet_age()
    page.go_to_pet_gender()
    page.go_to_pet_submit()
    browser.save_screenshot('create_profile.png')