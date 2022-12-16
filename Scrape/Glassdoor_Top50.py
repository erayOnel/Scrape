import os, sys
import requests
from bs4 import BeautifulSoup
headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
url=requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm",headers=headers_param)
data=url.content
soup=BeautifulSoup(data,"html.parser")
#'.strip()' methodu gereksiz bo?luklar? kald?rmaya yarar
# x=soup.find_all("div",{"class":"col-12 col-lg-3"})
# for y in x:
#     print(y.a.text)
#css selector
#select()
#select_one()
q=soup.find_all("div",{"class":"col-12 col-lg-3"})
for z in q:
    print(z.text)

o=soup.find_all("div",{"class":"col-6 col-lg mb-lg-0 mb-sm"})
for w in o :
    print(w.text)















































