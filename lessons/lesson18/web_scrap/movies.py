import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL, timeout=10)
archives_movies = response.text

soup = BeautifulSoup(archives_movies, "html.parser")
movies = soup.find_all(name="h3", class_="title")

if not movies:
    raise ValueError("No movie title found - check the CSS selector")

movies_list = []
for movie in movies:
    movie_title = movie.get_text()
    movies_list.append(movie_title)

with open(file="./movies.txt", mode="w") as write_file:
    for movie in movies_list:
        write_file.write(f"{movie.title()}\n")
