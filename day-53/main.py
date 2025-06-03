import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_FORMS_LINK = ("https://docs.google.com/forms/d/e/1FAIpQLSdqqLp58TipqiFTKDTQQvgu1siecK0F0Ye6yM4IThwjgWPKVA/"
                     "viewform?usp=header")

ZILLOW_CLONE_LINK = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_CLONE_LINK, headers=headers)
zillow_clone_website = response.text

soup = BeautifulSoup(zillow_clone_website, "html.parser")

listings_links_elements = soup.select(".StyledPropertyCardDataWrapper a")
listings_links = [link.get("href") for link in listings_links_elements]

listings_price_elements = soup.select(".StyledPropertyCardDataWrapper .PropertyCardWrapper__StyledPriceLine")
listings_prices = [price.text for price in listings_price_elements]
formatted_prices = [
    re.search(r"\$[\d,]+", price.replace("+", "").replace("/mo", "")).group()
    for price in listings_prices
    if re.search(r"\$[\d,]+", price)
]

listings_addresses = [address.text.strip() for address in listings_links_elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for index in range(len(listings_addresses)):
    driver.get(GOOGLE_FORMS_LINK)
    time.sleep(2)

    address_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    address_field.send_keys(listings_addresses[index])

    price_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price_field.send_keys(formatted_prices[index])

    link_field = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link_field.send_keys(listings_links[index])

    submit_button = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    )
    submit_button.click()
    time.sleep(2)

driver.close()
