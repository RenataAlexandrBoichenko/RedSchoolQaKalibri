from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, LOGIN
from locators import LOGIN_BUTTON, USERNAME_FIELD


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN)

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secretsauce")

    driver.find_element(By.ID, LOGIN_BUTTON).click()
    time.sleep(3)

    error = driver.find_element(By.XPATH, '//div[ @class ="error-message-container error"]')
    assert error

    driver.quit()
