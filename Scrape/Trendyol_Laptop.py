import os, sys
from bs4 import BeautifulSoup
import requests
import encodings
import pandas as pd
from itertools import chain
#
# def scrape(page):
#     headers_param = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#     base_url = requests.get(f"https://www.trendyol.com/laptop-x-c103108?pi={page}", headers=headers_param)
#     data = base_url.content
#     soup = BeautifulSoup(data, "lxml")
    # x = soup.find_all("div", {"class": "prdct-desc-cntnr-ttl-w two-line-text"})
    # for y in x:
    #     print(y.text)
    # # return soup
    # z=soup.find_all("div",{"class":"prc-box-dscntd"})
    # for q in z:
    #     print(q.text)
def get_item(url):
    base_url="https://www.trendyol.com/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"lxml")
    item=soup.select("div.p-card-wrppr a")
    return [base_url+items.attrs["href"] for items in item]
#print(get_item("https://www.trendyol.com/laptop-x-c103108?pi=1"))

def specific_item(url):
    req_s=requests.get(url)
    soup_s=BeautifulSoup(req_s.content,"lxml")
    products={
        "MODEL":soup_s.select_one("h1.pr-new-br span").text.strip(),
        "SALER": soup_s.select_one("div.merchant-box-wrapper a").text,
        "PRICE":soup_s.select_one("span.prc-dsc").text.strip()
    }
    return products

def engage():
    results=[]
    x = 1
    main_url=get_item(f"https://www.trendyol.com/laptop-x-c103108?pi={x}")
    product_info=[specific_item(url) for  url in main_url]
    results.append(product_info)
    return results
#print(engage())
df=pd.DataFrame(list(chain.from_iterable(engage())))
df.to_csv("Trendyol_Laptop_1",index=False)
print("Saved as csv")



