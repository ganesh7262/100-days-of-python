from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.python.org/")

event_date = [
    i.get_attribute("datetime").split(sep="T")[0]
    for i in driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget ul li time")
]

event_name = [
    i.text
    for i in driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget ul li a")
]

event_details = {
    i: {date: event}
    for i, date, event in zip(range(len(event_date)), event_date, event_name)
}

print(event_details)
