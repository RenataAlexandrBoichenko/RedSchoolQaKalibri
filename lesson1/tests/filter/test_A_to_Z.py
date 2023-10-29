from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_filter(driver, login_form):
    url = MAIN_PAGE

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(3)

    list_before = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')

    click_button = driver.find_element(By.XPATH, '//option[text()="Name (A to Z)"]')
    click_button.click()

    time.sleep(3)

    list_after = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')
    assert list_before == list_after

    driver.quit()