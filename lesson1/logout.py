from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user") # it's username

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce") #it's password

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    button_field = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    button_field.click()
    time.sleep(3)

    form_login = driver.find_element(By.CSS_SELECTOR, 'div[class="form_group"]')

    assert form_login
    driver.quit()