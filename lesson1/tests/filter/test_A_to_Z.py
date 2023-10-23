from selenium.webdriver.common.by import By
import time


def test_filter(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(3)

    list_before = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')

    click_button = driver.find_element(By.XPATH, '//option[text()="Name (A to Z)"]')
    click_button.click()

    time.sleep(3)

    list_after = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')
    assert list_before == list_after