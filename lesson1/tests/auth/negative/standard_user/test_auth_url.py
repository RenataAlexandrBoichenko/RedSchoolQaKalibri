from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, LOGIN, PASSWORD, INVENTORY_URL
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(3)

    url_before = driver.current_url == "https://www.saucedemo.com/inventor.html"

    time.sleep(3)
    url_after = INVENTORY_URL

    assert url_before != url_after

    driver.quit()