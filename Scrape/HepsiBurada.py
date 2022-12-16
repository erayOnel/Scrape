# import requests
# import os,sys
# from bs4 import BeautifulSoup
# import pandas as pd
#
# headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
# #url=requests.get("https://www.ciceksepeti.com/cok-satan-tasarim-cicekler?page=3",headers=headers_param)
# # url="https://www.hepsiburada.com/cep-telefonlari-c-371965"
# # response=requests.get(url,headers=headers_param)
# # soup=BeautifulSoup(response.content,"html.parser")
# #print(soup.encode("utf-8"))
# def get_item(url):
#     base_url="https://www.hepsiburada.com/"
#     response=requests.get(url,headers=headers_param)
#     soup=BeautifulSoup(response.content,"lxml")
#     item=soup.select("li.productListContent-item")
#     return [base_url+items.attrs["href"] for items in item]
#
# def specific_item(url):
#     response=requests.get(url,headers=headers_param)
#     soup=BeautifulSoup(response.content,"lxml")
#     features={
#         "MODEL":soup.select_one("header.title-wrapper span").text.strip(),
#         "PRICE":soup.select_one("span").text.strip(),
#         "RATINGS": soup.select_one("div.ratings-container bigger visible a span.rating-star").text.strip(),
#         # "CAMERA":soup.select_one("div.col lg-4 visible ul li strong")
#     }

