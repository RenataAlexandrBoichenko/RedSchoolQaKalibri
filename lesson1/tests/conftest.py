import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD
from data import LOGIN, PASSWORD, MAIN_PAGE
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()


@pytest.fixture()
def add_order(driver, login_form):
    url = MAIN_PAGE

    text_name_card = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_title_link"]')

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()
    time.sleep(2)

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()
    time.sleep(2)


