from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.DOWN_LIMIT = 50
        self.UP_LIMIT = 50
        self.getInternetSpeed()

    def getInternetSpeed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go_button.click()
        sleep(60)
        down_speed = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        up_speed = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text

        if float(down_speed) < self.DOWN_LIMIT or float(up_speed) < self.UP_LIMIT:
            self.tweetAtProvider()

    def tweetAtProvider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        email_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email_input.send_keys("hsenagednihs7262@gmail.com")
        email_input.send_keys(Keys.ENTER)
        pass_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        pass_input.send_keys("hsenag7262")
        pass_input.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot()
