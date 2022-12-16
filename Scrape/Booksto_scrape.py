import os,sys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import chain
# all_books=soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
# for x in all_books:
#     print(x)
def get_book(url):
    base_url = "http://books.toscrape.com/"
    req=requests.get(url)
    soup = BeautifulSoup(req.content, "lxml")
    book=soup.select("article.product_pod a")
    return[base_url+books.attrs["href"] for books in book]
#print(get_book("http://books.toscrape.com/"))

def specific_item(url):
    req_s=requests.get(url)
    soup_s=BeautifulSoup(req_s.content,"lxml")
    products={
        "Name":soup_s.select_one("h1").text.strip(),
        "Price":float(soup_s.select_one("p.price_color").text.strip().replace("£",""))
    }
    return products

def main():
    final=[]
    urls=get_book("http://books.toscrape.com/")
    info=[specific_item(url) for url in urls]
    final.append(info)
    return

print(main())
# df=pd.DataFrame(list(chain.from_iterable(main())))
# df.to_csv("Books_scraped",index=False)
# print("Saved as csv")





















































