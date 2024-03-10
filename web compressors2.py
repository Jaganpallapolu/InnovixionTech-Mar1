import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")[3]
print(boxes)

name = boxes.find("a").text
print(name)
desc = boxes.find("p", class_="card product-wrapper thumbnail")
print(desc)

