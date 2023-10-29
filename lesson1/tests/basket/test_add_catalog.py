from selenium.webdriver.common.by import By
from data import MAIN_PAGE
import time


def test_add_from_catalog(driver, login_form):
    url = MAIN_PAGE

    add_to_card_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_card_button.click()
    time.sleep(3)

    basket_button = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    basket_button.click()
    time.sleep(2)

    text_name_card = driver.find_element(By.CSS_SELECTOR, 'a[id="item_1_title_link"]')

    assert text_name_card

    time.sleep(3)

    driver.quit()
