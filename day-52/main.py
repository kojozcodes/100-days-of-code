from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

SIMILAR_ACCOUNT = "account"
USERNAME = "username"
PASSWORD = "password"


class InstaFollower:
    def __init__(self):
        self.scroll_box = None
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)

        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(USERNAME)

        time.sleep(2.4)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)

        time.sleep(5.8)
        not_now = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        not_now.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(6.4)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers").click()
        time.sleep(3.8)
        self.scroll_box = self.driver.find_element(
            By.XPATH,
            '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div'
        )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scroll_box)
            time.sleep(3.7)

    def follow(self):
        follow_buttons = self.scroll_box.find_elements(By.XPATH, "//button[.//div[text()='Follow']]")
        for btn in follow_buttons:
            try:
                btn.click()
                time.sleep(2.35)
            except:
                continue


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
