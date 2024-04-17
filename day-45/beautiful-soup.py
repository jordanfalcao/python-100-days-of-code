from bs4 import BeautifulSoup

# opening the file
with open("website.html", encoding='utf-8') as file:
    contents = file.read()

# creating BeautifulSoup object
soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.h3.string)
# print(soup.prettify())  # indented printing

# finding all the tags, not only the first one
all_paragraphs = soup.find_all(name="p")  # list with all paragraphs <p> tags
all_anchor_tags = soup.find_all(name="a")  # list with all anchor <a> tags

# print(all_paragraphs)

# printing only the texts from the paragraphs
for tag in all_anchor_tags:
    # print(tag.getText())  # getText method
    print(tag.get("href"))  # get method: get any attribute you set

# getting item by the "id"
# heading = soup.find(name="h1", id="name")
heading = soup.find(id="name")  # it gets the same to the line before
print(heading)

# getting by the class attribute
h3_heading = soup.find_all(name="h3", class_="heading")
print(h3_heading[1].getText())
print(h3_heading[0].get("class"))

# specific tag using inherit
company_url = soup.select_one(selector="p a")  # first anchor <a> which is inside tag <p>
print(company_url)

name_id = soup.select_one(selector="#name")  # select the first element with id="name"
print(name_id)

headings = soup.select(".heading")  # select ALL the elementS with class="heading"
print(headings)
