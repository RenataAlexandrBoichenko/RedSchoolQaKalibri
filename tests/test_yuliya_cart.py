from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_to_cart_from_catalog(): #Добавление товара в корзину через каталог
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_before_adding = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()

    item_after_adding = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    assert item_before_adding==item_after_adding

def test_delete_item_from_cart(): #Удаление товара из корзины через корзину
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_before_adding = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()

    item_after_adding = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    delete_item = driver.find_element(By.XPATH, '//*[@class="btn btn_secondary btn_small cart_button"]')
    delete_item.click()

    item_name_deleted = "Sauce Labs Backpack"
    assert item_name_deleted not in driver.current_url, f'Unexpectedly found the text: {item_name_deleted}'

def test_add_item_to_cart_from_card(): #Добавление товара в корзину из карточки товара
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_to_add = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
    item_to_add.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@class="btn btn_primary btn_small btn_inventory"]')
    add_to_cart_button.click()

    cart_button = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
    cart_button.click()

    item_after_adding = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    expected_item_name = "Sauce Labs Backpack"
    assert item_after_adding == expected_item_name, f"Expected item name: {expected_item_name}, Actual item name: {item_after_adding}"

def test_delete_item_from_card(): #Удаление товара из корзины через карточку товара
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_to_add = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
    item_to_add.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@class="btn btn_primary btn_small btn_inventory"]')
    add_to_cart_button.click()

    delete_item = driver.find_element(By.XPATH, '//*[@class="btn btn_secondary btn_small btn_inventory"]')
    delete_item.click()

    cart_button = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
    cart_button.click()

    item_name_deleted = "Sauce Labs Backpack"
    assert item_name_deleted not in driver.current_url, f'Unexpectedly found the text: {item_name_deleted}'









