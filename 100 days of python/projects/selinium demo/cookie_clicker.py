from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')

perk_vs_price = {
    17: '//*[@id="buyCursor"]',
    100: '//*[@id="buyGrandma"]',
    500: '//*[@id="buyFactory"]',
    2000: '//*[@id="buyMine"]',
    7000: '//*[@id="buyShipment"]',
    50000: '//*[@id="buyAlchemy lab"]',
    1000000: '//*[@id="buyPortal"]',
    123456789: '//*[@id="buyTime machine"]',
}


def buyPerk():
    for i in range(len(perk_vs_price)):
        if int(money.text) < list(perk_vs_price.keys())[i]:
            perk = driver.find_element(
                by=By.XPATH, value=perk_vs_price[list(perk_vs_price.keys())[i - 1]]
            )
            perk.click()
            return


STARTTIME = time.time()

money = driver.find_element(by=By.XPATH, value='//*[@id="money"]')

start_time = time.time()
while True:
    cookie.click()

    if time.time() > start_time + 5:
        buyPerk()
        start_time = time.time()
    elif time.time() > STARTTIME + 300:
        print(driver.find_element(By.XPATH, value='//*[@id="cps"]'))
