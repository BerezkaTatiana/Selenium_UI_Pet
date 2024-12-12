import pytest
from pages.delete_pet_profile_page import DeletePetProfile
from config import PROFILE_URL

@pytest.mark.smoke
def test_delete_pet_profile(browser, login):
    page = DeletePetProfile(browser, PROFILE_URL)
    page.open()
    page.go_to_delete_profile()
    browser.save_screenshot('delete_profile.png')
