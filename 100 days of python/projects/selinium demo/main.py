from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/Vans-SK8-Hi-Krooked-Sneaker-71002957/dp/B09XHPYV2W/ref=sr_1_1?crid=3UG7KSKW6LC4B&keywords=vans+sneakers+for+men&qid=1680627676&sprefix=vans%2Caps%2C204&sr=8-1")

img = driver.find_element(by=By.ID, value="imgTagWrapperId")
img.screenshot(r"100 days of python\projects\selinium demo\testimg.png")

print(img.size)
