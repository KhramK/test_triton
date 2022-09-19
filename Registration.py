from selenium import webdriver
from selenium.webdriver.common.by import By
import time

registration_btn_xpath = '/html/body/div[1]/div/div/div/div/form/div[5]/a'
email_block_xpath = '/html/body/div[1]/div/div/div/div/form/div[2]/p'
login_field_id = 'signupform-username'
email_field_id = 'signupform-email'
password_field_id = 'signupform-password'
button_btn_xpath = '/html/body/div[1]/div/div/div/div/form/div[4]/button'
account_xpath = '/html/body/header/div[3]/div/div/div/div/a[1]'
account_login_id = 'loginform-username'
account_password_id = 'loginform-password'
button_account_xpath = '/html/body/div[1]/div/div/div/div/form/div[6]/button'
button_logout_xpath = '/html/body/div[1]/div/div[1]/ul/li[3]/form/button'
personal_account_xpath = '/html/body/div[1]/div/div[2]/h1'
password_reset_xpath = '/html/body/div[1]/div/div/div/div/form/div[4]/a'
password_reset_form_id = 'passwordresetrequestform-email'
button_reset_xpath = '/html/body/div[1]/div/div/div/form/div[2]/button'

def run_all_test(driver):
    test_case_1(driver)
    test_case_2(driver)
    test_case_3(driver)
    test_case_4(driver)
    test_case_5(driver)
    test_case_6(driver)
    test_case_7(driver)
    test_case_8(driver)
    test_case_9(driver)
    test_case_10(driver)

def test_case_1(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('*test77')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('*999@mail.ru')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('*1253456')

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    time.sleep(1)
    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    time.sleep(1)
    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_2(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('test77*')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('999@mail.ru*')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('123456*')

    email_block = driver.find_element(By.XPATH, email_block_xpath)
    time.sleep(1)
    assert email_block.text == 'Значение «Email» не является правильным email адресом.'

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    driver.close

def test_case_3(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys(' test977')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys(' 799@mail.ru')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys(' 123456')

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    time.sleep(1)
    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_4(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('test555 ')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('555@mail.ru ')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('123456 ')

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    time.sleep(1)
    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    time.sleep(1)
    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_5(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('test2007')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('2007@mail.ru')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('123456')

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    time.sleep(1)
    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_6(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('test9')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('абв@mail.ru')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('123456')

    email_block = driver.find_element(By.XPATH, email_block_xpath)
    time.sleep(1)
    assert email_block.text == 'Значение «Email» не является правильным email адресом.'

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    driver.close

def test_case_7(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    registration_btn = driver.find_element(By.XPATH, registration_btn_xpath)
    registration_btn.click()

    login_field = driver.find_element(By.ID, login_field_id)
    login_field.send_keys('test9')

    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys('1345mail.ru')

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys('123456')

    email_block = driver.find_element(By.XPATH, email_block_xpath)
    time.sleep(1)
    assert email_block.text == 'Значение «Email» не является правильным email адресом.'

    button_btn = driver.find_element(By.XPATH, button_btn_xpath)
    button_btn.click()

    driver.close

def test_case_8(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    account_login = driver.find_element(By.ID, account_login_id)
    account_login.send_keys('test9')

    account_password = driver.find_element(By.ID, account_password_id)
    account_password.send_keys('123456')

    button_account = driver.find_element(By.XPATH, button_account_xpath)
    button_account.click()

    time.sleep(1)
    driver.refresh()

    time.sleep(1)

    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_9(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    account_login = driver.find_element(By.ID, account_login_id)
    account_login.send_keys('test9')

    account_password = driver.find_element(By.ID, account_password_id)
    account_password.send_keys('123456')

    button_account = driver.find_element(By.XPATH, button_account_xpath)
    button_account.click()

    time.sleep(2)

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    account_login = driver.find_element(By.ID, account_login_id)
    account_login.send_keys('test9')

    account_password = driver.find_element(By.ID, account_password_id)
    account_password.send_keys('123456')

    button_account = driver.find_element(By.XPATH, button_account_xpath)
    button_account.click()

    time.sleep(1)

    personal_account = driver.find_element(By.XPATH, personal_account_xpath)
    assert personal_account.text == 'Личный кабинет'

    button_logout = driver.find_element(By.XPATH, button_logout_xpath)
    button_logout.click()

    driver.close

def test_case_10(driver):
    driver.get("https://tritonshoes.ru/")

    account = driver.find_element(By.XPATH, account_xpath)
    account.click()

    time.sleep(1)
    password_reset = driver.find_element(By.XPATH, password_reset_xpath)
    password_reset.click()

    password_reset_page = driver.find_element(By.TAG_NAME, 'h1')
    assert password_reset_page.text == 'Request password reset'

    password_reset_form = driver.find_element(By.ID, password_reset_form_id)
    password_reset_form.send_keys('1345@mail.ru')

    button_reset = driver.find_element(By.XPATH, button_reset_xpath)
    button_reset.click()

    driver.close
