from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count_element = driver.find_element(By.CSS_SELECTOR, "#articlecount li:nth-of-type(2) a")
# print(article_count_element.text)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Hamza")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Ahmed")

email = driver.find_element(By.NAME, "email")
email.send_keys("kojozpythontesting@gmail.com")

button = driver.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(3)
driver.quit()
