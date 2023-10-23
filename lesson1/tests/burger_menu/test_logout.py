from selenium.webdriver.common.by import By
import time


def test_logout(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    button_field = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    button_field.click()
    time.sleep(3)

    form_login = driver.find_element(By.CSS_SELECTOR, 'div[class="form_group"]')
    assert form_login
