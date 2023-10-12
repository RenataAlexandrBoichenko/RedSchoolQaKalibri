from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_filtr():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(3)

    list_before = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')

    click_button = driver.find_element(By.XPATH, '//option[text()="Name (A to Z)"]')
    click_button.click()

    time.sleep(3)

    list_after = driver.find_element(By.XPATH, '//span[text()="Name (A to Z)"]')
    assert list_before == list_after