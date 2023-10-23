from selenium.webdriver.common.by import By
import time


def test_click(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    text_name_card_before = driver.find_element(By.CSS_SELECTOR,'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()

    basket_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    basket_button.click()

    text_name_card_after = driver.find_element(By.CSS_SELECTOR,'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    click_button = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
    click_button.click()

    time.sleep(5)

    checkout_card = driver.find_element(By.CSS_SELECTOR, '#page_wrapper')
    assert checkout_card


