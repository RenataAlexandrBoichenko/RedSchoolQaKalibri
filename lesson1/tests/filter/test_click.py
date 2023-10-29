from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE


def test_click(driver, login_form):
    url = MAIN_PAGE

    text_name_card_before = driver.find_element(By.CSS_SELECTOR,'#item_4_title_link').text

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()

    basket_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    basket_button.click()

    text_name_card_after = driver.find_element(By.XPATH, '//div[@class="inventory_details_desc_container"]').text

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(5)

    checkout_card = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link')
    assert checkout_card

    driver.quit()