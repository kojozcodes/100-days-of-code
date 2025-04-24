from operator import index

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.select(".titleline a")
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles if "https:" in article.get("href")]

article_scores = soup.find_all(name="span", class_="score")
article_scores_texts = [int(score.getText().split()[0]) for score in article_scores]

index_of_max = article_scores_texts.index(max(article_scores_texts))
print(index_of_max)
print(f"This title and link of the article with the highest points are: \n"
      f"    Title: {article_texts[index_of_max]} \n    Link: {article_links[index_of_max]}")

# print(article_texts)
# print(article_links)
# print(article_scores_texts)

# import lxml
#
# with open("website.html") as website_data:
#     contents = website_data.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
