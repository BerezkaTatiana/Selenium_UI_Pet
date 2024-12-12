from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT
from pages.add_image_to_profile import AddImageToPetProfile
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import AddImageToPetLocators


def test_add_image_to_pet(browser, login, edit):
    page = AddImageToPetProfile(browser, edit)
    page.open()
    page.go_to_add_image()
    page.go_to_upload_image()
    wait = WebDriverWait(browser, TIMEOUT)
    wait.until(ec.visibility_of_element_located(AddImageToPetLocators.PLUS_BTN))
    wait.until(ec.element_to_be_clickable(AddImageToPetLocators.PLUS_BTN))
    page.go_to_click()
    browser.save_screenshot("add_image.png")

