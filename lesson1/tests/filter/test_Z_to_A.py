from selenium.webdriver.common.by import By
import time


def test_filter(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(3)

    click_button = driver.find_element(By.XPATH, '//option[text()="Name (Z to A)"]')
    click_button.click()

    time.sleep(5)

    list = driver.find_element(By.XPATH, '//span[text()="Name (Z to A)"]')
    assert list