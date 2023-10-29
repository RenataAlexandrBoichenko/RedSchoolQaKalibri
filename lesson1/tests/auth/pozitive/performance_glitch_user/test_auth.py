from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, LOGIN3, PASSWORD, INVENTORY_URL
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN3)

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(3)

    assert INVENTORY_URL

    driver.quit()