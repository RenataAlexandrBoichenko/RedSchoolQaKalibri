from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_dell_order(driver, login_form):
    url = MAIN_PAGE

    add_to_card_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_card_button.click()
    time.sleep(3)

    basket_button = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    basket_button.click()
    time.sleep(2)

    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue-shopping')
    continue_button.click()
    time.sleep(2)

    dell_from_card_button = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-bolt-t-shirt')
    dell_from_card_button.click()
    time.sleep(2)

    page = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    assert page
