from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_add_from_product_card(driver, login_form):
    url = MAIN_PAGE

    text_name_card = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
    text_name_card.click()
    time.sleep(2)

    add_to_card_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_to_card_button.click()
    time.sleep(2)

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()
    time.sleep(2)

    text_name_card = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
    assert text_name_card


