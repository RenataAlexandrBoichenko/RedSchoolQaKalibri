from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, INVENTORY_URL


def test_login_form(driver, login_form):
    url_before = MAIN_PAGE

    time.sleep(3)
    url_after = INVENTORY_URL

    assert url_before != url_after

    driver.quit()
