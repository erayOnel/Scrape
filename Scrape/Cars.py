from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import chain
import os,sys

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#print(url.status_code)

def get_title(url):
    base_url="https://www.cars.com/"
    req=requests.get(url,headers=headers_param)
    soup=BeautifulSoup(req.content,"html.parser")
    item=soup.select("div.vehicle-card a.vehicle-card-visited-tracking-link")
    return [base_url+items.attrs["href"] for items in item if items.get('href')]

def specific_item(url):
    req_s=requests.get(url,headers=headers_param)
    soup_s=BeautifulSoup(req_s.content,"html.parser")
    products={
        "MODEL":soup_s.select_one("h1.listing-title").text.strip(),
        "PRICE":soup_s.select_one("div.price-section").text.strip(),
        "MILEAGE":soup_s.select_one("div.listing-mileage").text.replace(".","")+"lage".strip(),
        "NEW/USED":soup_s.select_one("p.new-used").text,
    }
    #print(url)
    return products

results=[]

def engage(page):
    urls=get_title(f"https://www.cars.com/shopping/results/?page={page}&page_size=20&list_price_max=&makes[]=&maximum_distance=all&models[]=&stock_type=all&zip=%22")
    product_info=[specific_item(url) for url in urls]
    results.append(product_info)
    return

if __name__ == "__main__":
    for page in range(1,21):
        print(page)
        engage(page)
        #print(specific_item("https://www.cars.com/vehicledetail/75d79bb5-d5d5-4bf0-b969-58a011605f01/"))
        # get_title(f"https://www.cars.com/shopping/results/?page={page}&page_size=20&list_price_max=&makes[]=&maximum_distance=all&models[]=&stock_type=all&zip=%22")
    df=pd.DataFrame(list(chain.from_iterable(results)))
    df.to_csv("Cars.com(20).csv",index=True)
    print(results)

#  df=pd.DataFrame(list(chain.from_iterable(engage(page))))
#  df.to_csv("Cars.com",index=False)
# print("Saved as csv")













