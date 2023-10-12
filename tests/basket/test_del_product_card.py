from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_del_order():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    name_card = driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    name_card.click()

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()

    text_name_card = driver.find_element(By.CSS_SELECTOR, '#item_3_title_link').text

    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue-shopping')
    continue_button.click()

    time.sleep(3)

    name_card = driver.find_element(By.CSS_SELECTOR, 'a[id="item_3_title_link"] > div[class="inventory_item_name"]')
    name_card.click()

    time.sleep(3)

    dell_from_card_button = driver.find_element(By.CSS_SELECTOR, 'button[id="remove-test.allthethings()-t-shirt-(red)"]')
    dell_from_card_button.click()

    time.sleep(3)

    page = driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    assert page