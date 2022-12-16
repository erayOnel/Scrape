import os, sys
import requests
from bs4 import BeautifulSoup

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
url=requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250",headers=headers_param)

data=url.content
soup=BeautifulSoup(data,"html.parser")
our_shows=soup.find_all("td",{"class":"titleColumn"})
for z in our_shows:
    print(z.a.text)













