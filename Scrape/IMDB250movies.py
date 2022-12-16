import os, sys

import requests
from bs4 import BeautifulSoup

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
url=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250",headers=headers_param)
#print(url.status_code)
#print(url.content)
#'content' websitenin verilerini almaya yarar
#'status_code'  websitenin verileri çekmeye izin verip vermedi?ini teyit etmek için kullan?l?r
data=url.content
soup=BeautifulSoup(data,"html.parser")
#our_movies=soup.find_all("tbody",{"class":"lister-list"})
#çağırmaya çalıştığın etiket içinde belirtilen parmetrelerin bulunup bulunmadığına dikkat et
q = soup.find_all("td",{"class":"titleColumn"})
for m in q:
    print(m.a.text)







































