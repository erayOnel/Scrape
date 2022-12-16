import requests
from bs4 import BeautifulSoup
import os,sys
import pandas as pd

# headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#
# response=requests.get("https://tr.vava.cars/buy/cars?pageNum=2")
# soup=BeautifulSoup(response.content,"lxml")
# x=soup.select_one("section.search-results__vehicle-list ng-star-inserted vc-vehicle-list div vc-vehicle.ng-star-inserted")
# print(x)


response = requests.get("https://tr.vava.cars/buy/cars?hideBooked=false&anyBooked=false&pageNum=1")

soup = BeautifulSoup(response.text, "html.parser")

car_links = soup.select(".vehicle-list .ng-star-inserted")
for link in car_links:
    print(link)

