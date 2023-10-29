from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_filter(driver, login_form):
    url = MAIN_PAGE

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(3)

    click_button = driver.find_element(By.XPATH, '//option[text()="Price (high to low)"]')
    click_button.click()

    time.sleep(3)

    list = driver.find_element(By.XPATH, '//span[text()="Price (high to low)"]')
    assert list



