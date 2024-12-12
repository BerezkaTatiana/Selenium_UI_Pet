from pages.main_page import MainPage
from config import MAIN_URL

def test_go_to_login_page(browser):
    page = MainPage(browser, MAIN_URL)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('login.png')

