from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_picture_order():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    picture_card = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]/img')
    picture_card.click()

    page = driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')

    assert page
