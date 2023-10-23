from selenium.webdriver.common.by import By


def test_picture_order(driver, login_form):
    driver.get("https://www.saucedemo.com/")

    picture_card = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]/img')
    picture_card.click()

    page = driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_details_name large_size"]')
    assert page
