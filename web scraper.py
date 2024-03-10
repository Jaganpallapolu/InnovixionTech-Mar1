import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# data = soup.find_all(string = "Galaxy Tab")
# data = soup.find_all(string=re.compile("WsCube"))
names = soup.find_all("a", class_="title")
product_name = []

for i in names:
    name = i.text
    product_name.append(name)
print(product_name)

prices = soup.find_all("h4", class_="float-end price card-title pull-right")
prices_list = []
for i in prices:
    price = i.text
    prices_list.append(price)
print(prices_list)

reviews = soup.find_all("p", class_="float-end review-count")
review_list = []
for i in reviews:
    rew = i.text
    review_list.append(rew)
print(review_list)

df = pd.DataFrame({"Product Name": product_name, "Prices": prices_list, "Review": review_list})
print(df)

