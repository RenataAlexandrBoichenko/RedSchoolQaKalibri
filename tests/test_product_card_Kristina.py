'''Карточка товара
1. Успешный переход к карточке товара после клика на картинку товара'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_click_image():
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    product_image_button = driver.find_element(By.XPATH, '//img[@class="inventory_item_img"]')
    product_image_button.click()
    time.sleep(5)