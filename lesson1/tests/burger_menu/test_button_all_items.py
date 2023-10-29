from selenium.webdriver.common.by import By
from data import MAIN_PAGE
import time


def test_login_form(driver, login_form):
    url = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    button_field = driver.find_element(By.CSS_SELECTOR, '#inventory_sidebar_link')
    button_field.click()

    time.sleep(5)

    page = driver.find_element(By.CSS_SELECTOR,'#inventory_container')
    assert page

    driver.quit()

