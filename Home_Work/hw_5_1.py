from selenium import webdriver

from selenium.webdriver.common.by import By

class Site:

    def __init__(self, url, user, password, submit):
        self.url=url
        self.user=user
        self.password=password
        self.submit=submit

    def open_site (self):
        if user  and password and submit is None:
            print('нет')
        else:
            print('Элементы найдены')


driver = webdriver.Chrome()
url = (driver.get("https://www.saucedemo.com/"))
user = (driver.find_element(By.CSS_SELECTOR,'input#user-name'))
password = (driver.find_element(By.CSS_SELECTOR, 'input#password'))
submit = (driver.find_element(By.CSS_SELECTOR, 'input#login-button'))

site_1=Site ("https://www.saucedemo.com/",'input#user-name', 'input#password', 'input#login-button' )

site_1.open_site()
