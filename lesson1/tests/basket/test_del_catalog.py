from selenium.webdriver.common.by import By


def test_dell_order(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    text_name_card_before = driver.find_element(By.CSS_SELECTOR,
                                                'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    add_to_card_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_card_button.click()

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()

    text_name_card_after = driver.find_element(By.CSS_SELECTOR,
                                               'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    continue_button = driver.find_element(By.CSS_SELECTOR, '#continue-shopping')
    continue_button.click()

    dell_from_card_button = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-bike-light')
    dell_from_card_button.click()

    page = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    assert page
