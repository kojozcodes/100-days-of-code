from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "email"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        go_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a'
        )
        go_btn.click()

        time.sleep(60)
        cookie_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_btn.click()

        close_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/div/div[2]/a'
        )
        close_btn.click()

        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print(f"Down: {self.down}\nUp: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")

        time.sleep(5)
        sign_in_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="loginButton"]')
        sign_in_btn.click()

        time.sleep(3)
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(TWITTER_EMAIL)
        username_input.send_keys(Keys.ENTER)

        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_field = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/'
            'div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/'
            'div/div/span/br'
        )
        tweet_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up?")

        post_btn = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
            'div[2]/div[2]/div[2]/div/div/div/button'
        )
        post_btn.click()

        self.driver.quit()
        print("Done tweeting")
