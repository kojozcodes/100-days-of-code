from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

my_email = "kojozpythontesting@gmail.com"
my_password = "H@k2oTwo2Pyth0n"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&"
    "keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

time.sleep(3)

sign_in_btn = driver.find_element(
    By.XPATH,
    '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'
)
sign_in_btn.click()

time.sleep(3)

email_text_input = driver.find_element(By.ID, "base-sign-in-modal_session_key")
email_text_input.send_keys(my_email)

password_text_input = driver.find_element(By.ID, "base-sign-in-modal_session_password")
password_text_input.send_keys(my_password)
password_text_input.send_keys(Keys.RETURN)

time.sleep(5)

actions = ActionChains(driver)

jobs = driver.find_elements(By.CSS_SELECTOR, "li .job-card-job-posting-card-wrapper")
for job in jobs:
    actions.move_to_element(job).perform()
    job.click()
    time.sleep(2)

    save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_btn.click()

    t_14 = driver.find_element(
        By.XPATH,
        '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/section[2]/section/div[1]/div[2]'
    )

    follow_btn = driver.find_element(
        By.XPATH,
        '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/section[2]/section/div[1]/div[1]/button'
    )

    actions.move_to_element(t_14).perform()
    follow_btn.click()

driver.quit()
