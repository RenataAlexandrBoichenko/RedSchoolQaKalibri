from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_logout(driver, login_form):
    url = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    button_field = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    button_field.click()
    time.sleep(3)

    form_login = driver.find_element(By.CSS_SELECTOR, 'div[class="form_group"]')
    assert form_login

    driver.quit()