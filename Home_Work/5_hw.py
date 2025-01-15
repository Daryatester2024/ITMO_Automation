from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

user=driver.find_element(By.CSS_SELECTOR, 'input#user-name')

if user is None:
        print('нет')
else:
        print('Элемент найден')

password=driver.find_element(By.CSS_SELECTOR,'input#password')

if password is None:
    print('нет')
else:
    print('Элемент найден')

button_sub=driver.find_element(By.CSS_SELECTOR, 'input#login-button')

if button_sub is None:
    print('no')
else:
    print('Элемент найден')

