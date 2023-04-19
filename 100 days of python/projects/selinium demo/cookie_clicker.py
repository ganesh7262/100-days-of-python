from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element(by=By.XPATH, value='//*[@id="bigCookie"]')

while True:
    cookie.click()
