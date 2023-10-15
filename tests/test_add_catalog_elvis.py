from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_from_catalog(): # Добавление товара в корзину через каталог
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    loggin_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    loggin_button.click()

    name_item_before = driver.find_element(By.CSS_SELECTOR,'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()

    time.sleep(1)

    cart_button = driver.find_element(By.ID, 'shopping_cart_container').click()

    time.sleep(2)

    name_item_adding = driver.find_element(By.CSS_SELECTOR,
                                            'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    assert name_item_adding == name_item_adding

    driver.quit()


def test_add_from_catalog(): # Удаление товара из корзины через корзину
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    loggin_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    loggin_button.click()

    name_item_before = driver.find_element(By.CSS_SELECTOR,
                                           'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()

    time.sleep(1)

    cart_button = driver.find_element(By.ID, 'shopping_cart_container').click()

    time.sleep(2)

    name_item_adding = driver.find_element(By.CSS_SELECTOR,
                                           'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text

    assert name_item_adding == name_item_adding

    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]').click()

    time.sleep(1)

    removed_cart_item = driver.find_element(By.CLASS_NAME, 'removed_cart_item')

    time.sleep(1)

    driver.quit()