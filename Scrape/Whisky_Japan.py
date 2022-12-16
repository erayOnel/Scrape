from bs4 import BeautifulSoup
import requests
import os, sys

base_url=("https://www.thewhiskyexchange.com/")
headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

productlinks= [ ]
for y in range(0,2):
    url=requests.get(f"https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={y}",headers=headers_param)
    data=url.content
    soup=BeautifulSoup(data,"html.parser")
    productlist = soup.find_all("li", {"class": "product-grid__item"})
    for x in productlist:
       for link in x.find_all("a",href=True):
                productlinks.append(base_url+link["href"])

for z in productlinks:
    req=requests.get(z,headers=headers_param)
    soup=BeautifulSoup(req.content,"html.parser")
    name=soup.find("h1",{"class":"product-main__name"}).text.strip()
    try:
        ratings=soup.find("div", {"class": "review-overview"}).text.strip()
    except:
        ratings="There is no ratings"
    price=soup.find("p",{"class":"product-action__price"}).text
    print(f"{name} , Reviews: {ratings} , Price: {price}")

































































