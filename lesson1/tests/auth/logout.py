from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_logout(driver, login_form):
    url_before = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(3)

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert url_before == url_after

    driver.quit()