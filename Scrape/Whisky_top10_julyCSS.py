from bs4 import BeautifulSoup
import requests
import os,sys
import pandas as pd
from itertools import chain
#CSS_Selector Methodları:
# (*)     => tüm etiketler
# (p)    => tüm p etiketleri
# (div p) => div içindeki tüm p etiketleri
# (div,p) => tüm div ve tüm p etiketleri
# (div > p) => üst etiketi div olan tüm p etiketleri
# (p ~ div)=> p ile aynı seviyede tüm div etiketleri
# (p + div)=> p etiketinden sonra gelen aynı seviyedeki div etiketi

def get_page_link(url):
    base_url="https://www.thewhiskyexchange.com/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html.parser")
    item=soup.select("li.top10-list__item a")
    return [base_url + items.attrs["href"] for items in item]
    #print(item)
#print(get_page_link("https://www.thewhiskyexchange.com/d/978/top-10-wines"))

def specific_item(url):
    req_s=requests.get(url)
    soup_s=BeautifulSoup(req_s.content,"html.parser")
    products={
        "Name":soup_s.select_one("h1.product-main__name").text.strip(),
        "Price":float(soup_s.select_one("p.product-action__price").text.strip().replace("£","")),
        "Stock":soup_s.select_one("p.product-action__stock-flag").text.strip()
    }
    #print(products)
    return products

# def eng():
#     urls= get_page_link(f"https://www.thewhiskyexchange.com/d/978/top-10-wines")
#     product_info=[specific_item(url) for url in urls]
#     return product_info
# print(eng())

def eng():
    results=[]
    urls= get_page_link("https://www.thewhiskyexchange.com/d/978/top-10-wines")
    product_info=[specific_item(url) for url in urls]
    results.append(product_info)
    #return results
    print(results)

eng()
# df=pd.DataFrame(list(chain.from_iterable(eng())))
# df.to_csv("Whisky_top10_july",index=False)
# print("Saved as csv")
