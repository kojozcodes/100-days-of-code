import requests
from bs4 import BeautifulSoup
import smtplib

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/135.0.0.0 Safari/537.36",
}


MY_EMAIL = "kojozpythontesting@gmail.com"
MY_PASSWORD = "THE PASSWORD"

response = requests.get(live_url, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# price_whole = soup.find(name="span", class_="a-price-whole")
# price_fraction = soup.find(name="span", class_="a-price-fraction")
# price = float(f"{price_whole.getText()}{price_fraction.getText()}")
# print(price)

price_html = soup.find(class_="a-offscreen")
price = float(price_html.getText().split("$")[1])

product_title = " ".join(soup.find(id="title").getText().split())
print(product_title)

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{product_title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="theemail@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"{message}\n\n"
                f"{practice_url}\n\n"
                f"Click the link above to buy!".encode("utf-8")
        )
