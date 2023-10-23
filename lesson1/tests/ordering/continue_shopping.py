from selenium.webdriver.common.by import By


def test_continue_shopping(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    text_name_card_before = driver.find_element(By.CSS_SELECTOR,'a[id="item_0_title_link"] > div[class="inventory_item_name"]').text

    add_to_card_button = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_card_button.click()

    basket_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    basket_button.click()

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    checkout_button.click()

    continue_shopping = driver.find_element(By.CSS_SELECTOR, '#page_wrapper')
    assert continue_shopping

