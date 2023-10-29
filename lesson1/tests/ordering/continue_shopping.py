from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_continue_shopping(driver, login_form, add_order):
    url = MAIN_PAGE

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    checkout_button.click()
    time.sleep(2)

    continue_shopping = driver.find_element(By.CSS_SELECTOR, '#page_wrapper')
    assert continue_shopping

    driver.quit()

