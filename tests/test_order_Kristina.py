'''Оформление заказа
1. Оформление заказа используя корректные данные'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_order():
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
    time.sleep(2)

    cart_button = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    cart_button.click()
    time.sleep(2)

    checkout_button = driver.find_element(By.XPATH, '//button[@class="btn btn_action btn_medium checkout_button"]')
    checkout_button.click()
    time.sleep(2)

    USERNAME_FIELD = '//input[@data-test="firstName"]'