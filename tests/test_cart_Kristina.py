'''Корзина
1. Добавление товара в корзину через каталог
2. Удаление товара из корзины через корзину'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_to_cart_from_catalog():
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()
    time.sleep(5)

def test_del_from_cart():
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(2)

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()
    time.sleep(5)

    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    time.sleep(5)

    del_item = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    del_item.click()
    time.sleep(3)