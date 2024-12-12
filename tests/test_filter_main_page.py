import pytest
from pages.filter_main_page import FilterMainPage
from config import MAIN_URL, NAME_FILTER
from pages.locators import FilterMainPageLocators

@pytest.mark.skip
def test_filter_main_page_by_cat(browser):
    page = FilterMainPage(browser, MAIN_URL)
    page.open()
    page.filter_main_page_by_cat()
    browser.save_screenshot('filter_by_cat.png')
    type_cat = browser.find_elements(*FilterMainPageLocators.CARDS)
    for cat in type_cat:
        cat_text = cat.text
        assert 'cat' in cat_text, "Pets don't filter by cat type"

@pytest.mark.win10
def test_filter_main_page_by_name(browser):
    page = FilterMainPage(browser, MAIN_URL)
    page.open()
    page.filter_main_page_by_name()
    browser.save_screenshot('filter_by_name.png')
    element = browser.find_element(*FilterMainPageLocators.PET_CARD)
    assert NAME_FILTER in element.text
