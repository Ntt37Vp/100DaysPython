from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)
anchor_tags = soup.find_all(name="a")
paragraphs = soup.find_all(name="p")
# print(anchor_tags)
# print(paragraphs)
# to get the strings inside the tags:
# for tag in anchor_tags:
    # print(tag.getText()) # to get the links tag
    # print(tag.get("href")) # to get all links

# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# get hold of specific element (similar to CSS approach of specificity)
# company_url = soup.select_one(selector="p a")
# print(company_url)
# company = soup.select_one(selector="#name") # pound sign for the ID name
# print(company)
headings = soup.select(selector=".heading") # dot sign for the class heading
print(headings)
