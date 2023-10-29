from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_continue_shopping(driver, login_form):
    url = MAIN_PAGE

    text_name_card = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_title_link"]')

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()
    time.sleep(2)

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()
    time.sleep(2)

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    checkout_button.click()
    time.sleep(2)

    continue_shopping = driver.find_element(By.CSS_SELECTOR, '#page_wrapper')
    assert continue_shopping

    driver.quit()

