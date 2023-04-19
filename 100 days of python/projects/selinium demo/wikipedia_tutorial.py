from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(article_count.click())
