from config import MAIN_URL, COMMENT
from pages.like_comment_main_page import LikeCommentMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import TIMEOUT
from pages.locators import LikeCommentMainPageLocators


def test_like_main_page(browser, login):
    page = LikeCommentMainPage(browser, MAIN_URL)
    page.open()
    page.go_to_profile()
    wait = WebDriverWait(browser, TIMEOUT)
    wait.until(ec.visibility_of_all_elements_located(LikeCommentMainPageLocators.LIKE_BTN))
    page.like()
    browser.save_screenshot('like.png')

def test_comment_main_page(browser, login):
    page = LikeCommentMainPage(browser, MAIN_URL)
    page.open()
    page.go_to_profile()
    page.details()
    page.comment()
    browser.save_screenshot('comment.png')
    comment = browser.find_element(*LikeCommentMainPageLocators.CARD).text
    assert COMMENT in comment
