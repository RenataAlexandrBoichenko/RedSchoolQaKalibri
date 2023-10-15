from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login_form(): # Авторизация используя корректные данные (standard_user, secret_sauce)
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field =driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    loggin_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    loggin_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.quit()

def test_login_form_incorrect_name_incorrect_pass(): # Авторизация используя некорректные данные (user, user)
    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('user')

    password_field =driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('user')

    loggin_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    loggin_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/'

    error_message = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
    assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    driver.quit()