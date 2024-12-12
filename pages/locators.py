from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BTN = (By.CLASS_NAME, 'p-button-label')

class TransitionToCreatePet:
    PET_ADD = (By.CLASS_NAME, 'p-button-label')

class CreatePetProfileLocators:
    PET_NAME = (By.ID, "name")
    PET_TYPE_DROPDOWN = (By.XPATH, '//*[@id="typeSelector"]')
    PET_TYPE_DOG = (By.XPATH, "//li[contains(.,'dog')]")
    PET_AGE = (By.CSS_SELECTOR, 'span#age > input')
    PET_GENDER = (By.XPATH, '//*[@id="genderSelector"]')
    PET_GENDER_MALE = (By.XPATH, "//li[contains(.,'Male')]")
    PET_SUBMIT = (By.CSS_SELECTOR, '.p-button-success > .p-button-label')

class AddImageToPetLocators:
    PET_IMAGE = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/span/span[2]')
    PLUS_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/span')

class EditPetProfileLocators:
    EDIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div/div[2]/button[1]/span[2]')
    DOG_NAME = (By.XPATH, "//input[@id='name']")
    DOG_AGE = (By.CSS_SELECTOR, '.p-inputnumber-input')
    SAVE_BTN = (By.CSS_SELECTOR, ".p-button-success > .p-button-label")

class DeletePetProfileLocators:
    PETS = (By.CSS_SELECTOR, '.col-12')
    DELETE_BTN = (By.XPATH, "//span[contains(.,'Delete')]")
    CONFIRM_BTN = (By.XPATH, "//span[contains(.,'Yes')]")

class FilterMainPageLocators:
    FILTER_DPD = (By.XPATH, "//span[contains(.,'Filter By type')]")
    PET_TYPE_CAT = (By.XPATH, "//li[contains(.,'cat')]")
    FILTER_BY_NAME = (By.XPATH, "//input[@id='petName']")
    PET_CARD = (By.CLASS_NAME, 'product-name')
    CARDS = (By.CLASS_NAME, 'product-category')

class LikeCommentMainPageLocators:
    LOGO = (By.CSS_SELECTOR, '.logo')
    LIKE_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(4) .product-grid-item-bottom .pi')
    DETAILS_BTN = (By.CSS_SELECTOR, '.col-12:nth-child(4) .p-button-label')
    EDITOR = (By.CSS_SELECTOR, '.ql-editor')
    SAVE_COMMENT_BTN = (By.XPATH, "//span[contains(.,'Save comment')]")
    CARD = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[2]/div')

