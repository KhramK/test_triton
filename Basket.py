from pydoc import text

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

basket_xpath = '/html/body/header/div[3]/div/div/div/div/a[2]'
trash_button_xpath = '/html/body/div[1]/section/div/div[2]/div/div/div/table/tbody/tr[2]/td[5]/span'
basket_Text_xpath = '/html/body/div[1]/section/div/div[2]/div/p'
button_without_registration_xpath = '/html/body/div[1]/section/div/div[2]/div/div/div/a[1]'
button_next_xpath = '/html/body/div[1]/section/div/div[2]/div/div/div/form/div[4]/button'
name_customer_id = 'orders-name'
email_customer_id = 'orders-email'
telephone_customer_id = 'orders-phone'
total_basket_id = 'total-basket'
woman_shoes_xpath = '/html/body/header/div[3]/div/div/div/nav/ul/li[1]/a'
woman_sandals_xpath = '/html/body/div[1]/section/div/div[2]/div/div[2]/div[1]/div/div/a[8]'
choose_sandals_xpath = '/html/body/div[1]/section/div/div[2]/div/div[2]/div/div[1]'
button_buy_xpath = '/html/body/div[1]/section/div/div[2]/div/div[2]/a'
plus_quantity_xpath = '/html/body/div[1]/section/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/button[2]'
minus_quantity_xpath = '/html/body/div[1]/section/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/button[1]'
alert_Text_xpath = '/html/body/div[3]/span'
page_of_ordering_xpath = '/html/body/div[1]/section/div/div[2]/div/h1'
page_of_delivery_xpath = '/html/body/div[1]/section/div/div[2]/div/h1'

def run_all_test(driver):
    test_case_11(driver)
    test_case_12(driver)
    test_case_13(driver)
    test_case_14(driver)
    test_case_15(driver)
    test_case_16(driver)

def test_case_11(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    time.sleep(1)
    alert_Text = driver.find_element(By.XPATH, alert_Text_xpath)
    assert alert_Text.text == 'Товар добавлено в корзину'

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    trash_button = driver.find_element(By.XPATH, trash_button_xpath)
    trash_button.click()

    basket_Text = driver.find_element(By.XPATH, basket_Text_xpath)
    assert basket_Text.text == 'Ваша корзина пуста.'

    driver.close

def test_case_12(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    plus_quantity = driver.find_element(By.XPATH, plus_quantity_xpath)
    plus_quantity.click()

    time.sleep(1)
    total_basket = driver.find_element(By.ID, total_basket_id)
    assert total_basket.text == '17982'

    plus_quantity = driver.find_element(By.XPATH, plus_quantity_xpath)
    plus_quantity.click()

    time.sleep(1)
    total_basket = driver.find_element(By.ID, total_basket_id)
    assert total_basket.text == '26973'

    minus_quantity = driver.find_element(By.XPATH, minus_quantity_xpath)
    minus_quantity.click()

    time.sleep(1)
    total_basket = driver.find_element(By.ID, total_basket_id)
    assert total_basket.text == '17982'

    minus_quantity = driver.find_element(By.XPATH, minus_quantity_xpath)
    minus_quantity.click()

    time.sleep(1)
    total_basket = driver.find_element(By.ID, total_basket_id)
    assert total_basket.text == '8991'

    driver.close

def test_case_13(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    button_without_registration = driver.find_element(By.XPATH, button_without_registration_xpath)
    button_without_registration.click()

    page_of_ordering = driver.find_element(By.XPATH, page_of_ordering_xpath)
    assert page_of_ordering.text == 'Оформление заказа'

    driver.close

def test_case_14(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    button_without_registration = driver.find_element(By.XPATH, button_without_registration_xpath)
    button_without_registration.click()

    name_customer = driver.find_element(By.ID, name_customer_id)
    name_customer.send_keys('Иванов Иван Иванович')

    email_customer = driver.find_element(By.ID, email_customer_id)
    email_customer.send_keys('1345@mail.ru')

    telephone_customer = driver.find_element(By.ID, telephone_customer_id)
    telephone_customer.send_keys('89095551122')
    time.sleep(1)

    button_next = driver.find_element(By.XPATH, button_next_xpath)
    button_next.click()

    time.sleep(2)
    page_of_delivery = driver.find_element(By.XPATH, page_of_delivery_xpath)
    assert page_of_delivery.text == 'Доставка'

    driver.close

def test_case_15(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    button_without_registration = driver.find_element(By.XPATH, button_without_registration_xpath)
    button_without_registration.click()

    name_customer = driver.find_element(By.ID, name_customer_id)
    name_customer.clear()
    name_customer.send_keys('прклпр')

    email_customer = driver.find_element(By.ID, email_customer_id)
    email_customer.clear()
    email_customer.send_keys('135343mail.ru')

    telephone_customer = driver.find_element(By.ID, telephone_customer_id)
    telephone_customer.clear()
    telephone_customer.send_keys('ьп ьбук')

    button_next = driver.find_element(By.XPATH, button_next_xpath)
    button_next.click()

    driver.close

def test_case_16(driver):
    driver.get("https://tritonshoes.ru/")

    woman_shoes = driver.find_element(By.XPATH, woman_shoes_xpath)
    woman_shoes.click()

    woman_sandals = driver.find_element(By.XPATH, woman_sandals_xpath)
    woman_sandals.click()

    choose_sandals = driver.find_element(By.XPATH, choose_sandals_xpath)
    choose_sandals.click()

    button_buy = driver.find_element(By.XPATH, button_buy_xpath)
    button_buy.click()

    basket = driver.find_element(By.XPATH, basket_xpath)
    basket.click()

    button_without_registration = driver.find_element(By.XPATH, button_without_registration_xpath)
    button_without_registration.click()

    name_customer = driver.find_element(By.ID, name_customer_id)
    name_customer.clear()
    name_customer.send_keys('прклпр')

    email_customer = driver.find_element(By.ID, email_customer_id)
    email_customer.clear()
    email_customer.send_keys('135343@mail.ru')

    telephone_customer = driver.find_element(By.ID, telephone_customer_id)
    telephone_customer.clear()
    telephone_customer.send_keys('ьп ьбук')

    button_next = driver.find_element(By.XPATH, button_next_xpath)
    button_next.click()

    driver.close()
