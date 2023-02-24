from selenium import webdriver as wb
from selenium.webdriver.common.by import By

driver = wb.Chrome('./chromedriver.exe')

driver.get('https://www.google.com/')

driver.find_element(By.CLASS_NAME, value='gLFyf').send_keys('군산')

driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()

input()