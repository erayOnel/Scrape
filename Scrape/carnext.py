from bs4 import BeautifulSoup
import requests


headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# def get_title(url):
#     base_url="https://www.carnext.com/es-es/"
#     response=requests.get(url,headers=headers_param)
#     soup=BeautifulSoup(response.content,"lxml")
#     item=soup.select("div.GridItem-sc-18k7fn-0 bRnNcB")
#     print(item)

def specific_car(url):
    response=requests.get(url,headers=headers_param)
    soup_specific=BeautifulSoup(response.content,"lxml")
    features={
        "NAME":soup_specific.select_one("div.GridItem-sc-18k7fn-0.jgsBKw h1.Heading-sc-1v4ld21-0.diYkvC span").text,
        "MODEL":soup_specific.select_one("div.GridItem-sc-18k7fn-0.jgsBKw h1.Heading-sc-1v4ld21-0.diYkvC").text.split()[1::],
        "ENGINE":soup_specific.select_one("div.GridItem-sc-18k7fn-0.jgsBKw p.Paragraph-sc-25o8pt-0.eVZrhb").text,
        "REGISTRATION":soup_specific.select_one("div.VehiclePropertiesSection__PropertyItemWrapper-sc-1yucq1y-0.bPWtyL div.Grid-sc-1a9f5yw-0.fsBpzI div.GridItem-sc-18k7fn-0.hiszBf p.Label-sc-1xzhlt8-0.kalKkr").text,
        "GAS":soup_specific.select_one("div.Spacing-sc-tkc3s4-0.bVCUBc div.VehiclePropertiesSection__PropertyItemWrapper-sc-1yucq1y-0.bPWtyL div.Grid-sc-1a9f5yw-0.fsBpzI div.GridItem-sc-18k7fn-0.hiszBf p.Label-sc-1xzhlt8-0.kalKkr").text
    }

    return features

print(specific_car("https://www.carnext.com/es-es/coches/ford/focus/wf05-fl62-32u8/"))



