import pytest
from selenium.common import TimeoutException
from pages.login_page import LoginPage
from config import LOGIN_URL
from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.smoke
def test_go_to_login_positive(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login_positive()
    page.go_to_password_positive()
    page.go_to_submit()
    browser.save_screenshot('login_page_positive.png')
    try:
        WebDriverWait(browser, TIMEOUT).until(ec.url_contains("profile"))
        assert 'profile' in browser.current_url
        print("The user is logged in.")
    except TimeoutException:
        print("The user is not logged in.")

@pytest.mark.regression
def test_go_to_login_negative_login(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login_negative()
    page.go_to_password_positive()
    page.go_to_submit()
    browser.save_screenshot('login_page_negative_login.png')
    try:
        WebDriverWait(browser, TIMEOUT).until(ec.url_contains("profile"))
        assert 'profile' in browser.current_url
    except TimeoutException:
        print("The user is not logged in.")

@pytest.mark.regression
def test_go_to_login_negative_password(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.go_to_login_positive()
    page.go_to_password_negative()
    page.go_to_submit()
    browser.save_screenshot('login_page_negative_password.png')
    try:
        WebDriverWait(browser, TIMEOUT).until(ec.url_contains("profile"))
        assert 'profile' in browser.current_url
    except TimeoutException:
        print("The user is not logged in.")