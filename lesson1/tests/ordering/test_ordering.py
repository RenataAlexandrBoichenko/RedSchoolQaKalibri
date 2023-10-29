from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_login_form(driver, login_form):
    url = MAIN_PAGE

    text_name_card = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_title_link"]')

    add_to_card_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()
    time.sleep(3)

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()
    time.sleep(3)

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()
    time.sleep(3)

    checkout_card = driver.find_element(By.CSS_SELECTOR, '#checkout_info_container')
    assert checkout_card

    driver.quit()
