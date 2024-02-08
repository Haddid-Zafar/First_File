import requests
from bs4 import BeautifulSoup
url="https://www.sclothers.com/pages/menshome"
page=requests.get(url)
soup=BeautifulSoup(page.text,"lxml")
Name=soup.find_all("div",class_="grid-product__title grid-product__title--body")
for n in Name:
    print(n.text)
