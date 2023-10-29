from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_button(driver, login_form):
    url = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(2)

    button_field = driver.find_element(By.CSS_SELECTOR, '#about_sidebar_link')
    button_field.click()
    time.sleep(2)

    page = driver.find_element(By.XPATH, '//div[@class="MuiStack-root css-mq2a14"]')
    assert page

    driver.quit()