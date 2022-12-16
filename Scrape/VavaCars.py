import requests
from bs4 import BeautifulSoup
import os,sys
import pandas as pd

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def get_title(url):
    base_url="https://tr.vava.cars/"
    response=requests.get(url,headers=headers_param)
    soup=BeautifulSoup(response.content,"lxml")
    item=soup.select("vc-vehicle.ng-star-inserted a.vehicle_link")
    return [base_url+items.attrs["href"] for items in item if items.get("href")]

def specific_car(url):
    response_specific=requests.get(url,headers=headers_param)
    soup_specific=BeautifulSoup(response_specific.content,"lxml")
    features={
        "NAME":soup_specific.select_one("div.vdp-detail-card div h3").text
    }
    print(url)
    return features

results=[]
def engage(page):
    urls=get_title(f"https://tr.vava.cars/buy/cars?pageNum={page}")
    features=[specific_car(url) for url in urls]
    results.append(features)
    return

if __name__=="__main__":
    for page in range(1,1):
        print(page)
        engage(page)

    print(results)



