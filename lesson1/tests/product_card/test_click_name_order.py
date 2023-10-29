from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_name_order(driver, login_form):
    url = MAIN_PAGE

    name_card = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
    name_card.click()
    time.sleep(2)

    page = driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    assert page

    driver.quit()
