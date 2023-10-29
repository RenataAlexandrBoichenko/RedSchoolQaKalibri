from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_login_form(driver, login_form, add_order):
    url = MAIN_PAGE

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()
    time.sleep(3)

    checkout_card = driver.find_element(By.CSS_SELECTOR, '#checkout_info_container')
    assert checkout_card

    driver.quit()
