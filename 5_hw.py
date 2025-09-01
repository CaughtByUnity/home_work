from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

user_name_field = driver.find_element(By.CSS_SELECTOR, '#user-name')
password_field = driver.find_element(By.CSS_SELECTOR, '#password')
submit_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

if user_name_field and password_field and submit_button:
    print('Элементы найдены')
else:
    print('Элементы не найдены')


