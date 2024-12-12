import pytest
from selenium import webdriver
from config import LOGIN_URL, PROFILE_URL, TIMEOUT
from pages.login_page import LoginPage
from pages.edit_pet_profile import EditPetProfile

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def login(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login_positive()
    page.go_to_password_positive()
    page.go_to_submit()

@pytest.fixture()
def edit(browser, login):
    page = EditPetProfile(browser, PROFILE_URL)
    page.open()
    page.go_to_edit_profile()
    browser.implicitly_wait(TIMEOUT)
    return browser.current_url


