from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

# initiating BeautifulSoup object
soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

# first way to get the Text written in the link
# article_tag = soup.find(name="span", class_="titleline")
# print(article_tag.getText())

# text, link and upvote of the first article
# article_tag = soup.select_one(".titleline a")  # <a> inside a <span> with class="titleline"
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
#
# print(article_text)
# print(article_link)
# print(article_upvote)

# text, link and upvote of all articles
articles = soup.select(".titleline a")  # <a> inside a <span> with class="titleline"

article_text = [article.getText() for article in articles]  # save in a list
article_link = [article.get("href") for article in articles]  # save in a list
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]  # save in a list

# print(article_text)
# print(article_link)
print(articles_upvotes)

highest_upvotes = max(articles_upvotes)
index_highest_upvotes = articles_upvotes.index(highest_upvotes)

print(f"The text of the highest upvotes: {article_text[index_highest_upvotes]}.\n"
      f"The link of the highest upvotes: {article_link[index_highest_upvotes]}.\n"
      f"The index of the highest upvotes: {index_highest_upvotes}.")