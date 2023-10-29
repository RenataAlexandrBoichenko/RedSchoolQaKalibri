from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_picture_order(driver, login_form):
    url = MAIN_PAGE

    picture_card = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]/img')
    picture_card.click()
    time.sleep(3)

    page = driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    assert page

    driver.quit()
