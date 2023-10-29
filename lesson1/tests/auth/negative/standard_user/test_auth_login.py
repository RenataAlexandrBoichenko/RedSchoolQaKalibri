from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, PASSWORD
from locators import LOGIN_BUTTON, PASSWORD_FIELD


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standar_user")

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(3)

    error = driver.find_element(By.XPATH, '//div[ @class ="error-message-container error"]')
    assert error

    driver.quit()