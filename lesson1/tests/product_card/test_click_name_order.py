from selenium.webdriver.common.by import By


def test_name_order(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    name_card = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
    name_card.click()

    page = driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    assert page
