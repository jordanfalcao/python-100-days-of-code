import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# request URL e get the text
response = requests.get(URL)
web_html = response.text

# initiating BeautifulSoup object
soup = BeautifulSoup(web_html, "html.parser")
# print(soup.title)
# print(soup.prettify())  # indented print

# select all the movie titles
h3_title = soup.find_all(name="h3", class_="title")
movies_list = [text.getText() for text in h3_title]

movies_ordered = movies_list[::-1]  # revert the order of the list: beginning:final:step
# print(movies_ordered)

with open("movies.txt", 'w', encoding='utf-8') as file:
    for movie in movies_ordered:
        file.write(f"{movie}\n")

