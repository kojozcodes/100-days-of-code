import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
movie_titles_tags = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movie_titles_tags]
movie_titles.reverse()

with open("Top 100 movies to watch.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
