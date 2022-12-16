from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1= browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap").text
    num2= browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap").text
    num3= int(num1)+int(num2)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num3))
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button1.click()
  

finally:
  
    time.sleep(30)
 
    browser.quit()
