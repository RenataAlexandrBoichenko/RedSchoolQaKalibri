from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, LOGIN1, PASSWORD
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN1)

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(3)

    text_message = driver.find_element(By.CSS_SELECTOR, 'button[class ="error-button"]')

    time.sleep(5)
    assert text_message

    driver.quit()