from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_del_order(driver, login_form):
    url = MAIN_PAGE

    name_card = driver.find_element(By.CSS_SELECTOR, '#item_3_title_link')
    name_card.click()

    add_to_card_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    add_to_card_button.click()
    time.sleep(5)

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()
    time.sleep(5)

    remove_button = driver.find_element(By.XPATH, '//button[@id="remove-test.allthethings()-t-shirt-(red)"]')
    remove_button.click()
    time.sleep(5)

    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue-shopping')
    continue_button.click()
    time.sleep(5)

    name_card = driver.find_element(By.CSS_SELECTOR, '#item_3_title_link')
    name_card.click()

    add_to_card_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    assert add_to_card_button
