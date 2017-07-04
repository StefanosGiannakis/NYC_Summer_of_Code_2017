from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


my_url ="https://www.politeianet.gr/best-sellers"
uClient=urlopen(my_url)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html, "html.parser")
containers=page_soup.findAll("div",{"browse-page-block"})


# Csv file config
filename="products.csv"
f = open(filename,"w")
headers ="Book_Title, Price\n"

f.write(headers)


for container in containers:
    bookTitle = container.div.div.div.div.div.a.img["title"]
    Title=bookTitle[0]

    price = container.findAll("span",{"productPrice"})
    bookPrice = price[0].text.strip()

    print("Title :" + bookTitle)
    print("Price :" + bookPrice)

    f.write(bookTitle.replace(",","|") + "," + bookPrice + "\n")

f.close()
