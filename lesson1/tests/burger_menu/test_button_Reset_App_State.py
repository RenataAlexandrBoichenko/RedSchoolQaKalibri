from selenium.webdriver.common.by import By
import time


def test_button(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    text_name_card_before = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_card_button.click()

    basket_button = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    basket_button.click()

    text_name_card_after = driver.find_element(By.CSS_SELECTOR,'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    assert text_name_card_before == text_name_card_after

    text_counter_basket_before = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    time.sleep(3)

    button_field = driver.find_element(By.CSS_SELECTOR, '#reset_sidebar_link')
    button_field.click()

    time.sleep(3)

    exit_button = driver.find_element(By.XPATH, '//button[@id="react-burger-cross-btn"]')
    exit_button.click()

    text_counter_basket_after = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    assert text_counter_basket_before != text_counter_basket_after