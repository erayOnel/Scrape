import requests
import json
import pandas as pd
from itertools import chain

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class CarNextSpain:
    def __init__(self,  date):
        self.base_url = ''""
        self.link = "https://gateway.carnext.com/api/showroom/v1/cars/?orderBy=-date&locale=es-es&size=30&continuationToken=eyJjIjp7ImNjIjoiRVMiLCJ0IjpbXSwiZiI6W10sImIiOltdLCJjIjpbXSwicyI6W10sImRyIjpbXSwidnQiOltdLCJtbSI6W10sImNsIjpbXSwiZCI6ZmFsc2UsImxjIjpbXSwicmNpIjoiIiwicmNpcyI6W10sImVuYyI6W10sImR0dCI6W10sInNzIjpbXSwidGFncyI6W10sInRzcyI6W10sInJsdCI6W10sIm9wIjpbXX0sImEiOnsiYyI6MTY2MDEyNjQ0NDE0NywiaSI6ZmFsc2UsImNjIjoiRVMiLCJpcnMiOmZhbHNlfSwibyI6W3siZCI6dHJ1ZSwiZiI6MH1dfQ%3D%3D"

    def generate_url(self, token):
        return f"https://gateway.carnext.com/api/showroom/v1/cars/?orderBy=-date&locale=es-es&size=30&continuationToken={token}"

    def cars_info(self):
        response = requests.get(self.link)
        data  = json.loads(response.text)
        # data["occassion"] #verileri al
        for f in data["occasions"]:
            print(
                {
                    "MAKE": f["make"],
                    "MODEL": f["model"],
                    "TYPE": f["type"],
                    "YEAR": f["yearOfConstruction"],
                    "FUEL": f["fuel"],
                    "MILEAGE": f["mileage"]["amount"],
                    # "UNIT" : f["mileage"]["unit"],
                    "TRANSMISSION": f["transmission"],
                    "PRICE": f["salePrice"]["amount"],
                    "CURRENCY": f["salePrice"]["currencyCode"],
                    "LINK": f["_links"][0]["href"]
                }
            )
        self.link = self.generate_url(token)

        while True:
            if data["nextContinuationToken"]==None:
                break
            else:
                continue

spain = CarNextSpain("2022-08-19")
url = spain.generate_url("eyJjIjp7ImNjIjoiRVMiLCJ0IjpbXSwiZiI6W10sImIiOltdLCJjIjpbXSwicyI6W10sImRyIjpbXSwidnQiOltdLCJtbSI6W10sImNsIjpbXSwiZCI6ZmFsc2UsImxjIjpbXSwicmNpIjoiIiwicmNpcyI6W10sImVuYyI6W10sImR0dCI6W10sInNzIjpbXSwidGFncyI6W10sInRzcyI6W10sInJsdCI6W10sIm9wIjpbXX0sImEiOnsiYyI6MTY1OTY4OTE3MDU2MCwiaSI6ZmFsc2UsImNjIjoiRVMiLCJpcnMiOmZhbHNlfSwibyI6W3siZCI6dHJ1ZSwiZiI6MH1dfQ==")

response = requests.get(url)
data = json.loads(response.text)
print(data)


# def first():
#     response = requests.get("https://gateway.carnext.com/api/showroom/v1/cars/?orderBy=-date&locale=es-es&size=30&continuationToken=eyJjIjp7ImNjIjoiRVMiLCJ0IjpbXSwiZiI6W10sImIiOltdLCJjIjpbXSwicyI6W10sImRyIjpbXSwidnQiOltdLCJtbSI6W10sImNsIjpbXSwiZCI6ZmFsc2UsImxjIjpbXSwicmNpIjoiIiwicmNpcyI6W10sImVuYyI6W10sImR0dCI6W10sInNzIjpbXSwidGFncyI6W10sInRzcyI6W10sInJsdCI6W10sIm9wIjpbXX0sImEiOnsiYyI6MTY2MDEyNjQ0NDE0NywiaSI6ZmFsc2UsImNjIjoiRVMiLCJpcnMiOmZhbHNlfSwibyI6W3siZCI6dHJ1ZSwiZiI6MH1dfQ%3D%3D",headers=headers_param)
#     data = json.loads(response.text)
#     for f in data["occasions"]:
#         print(
#             {
#                 "MAKE" : f["make"],
#                 "MODEL" : f["model"],
#                 "TYPE" : f["type"],
#                 "YEAR" : f["yearOfConstruction"],
#                 "FUEL": f["fuel"],
#                 "MILEAGE" : f["mileage"]["amount"],
#                 # "UNIT" : f["mileage"]["unit"],
#                 "TRANSMISSION" : f["transmission"],
#                 "PRICE" : f["salePrice"]["amount"],
#                 "CURRENCY" : f["salePrice"]["currencyCode"],
#                 "LINK":f["_links"][0]["href"]
#             }
#         )
# first()

# response = requests.get("https://gateway.carnext.com/api/showroom/v1/cars/?orderBy=-date&locale=es-es&size=30&continuationToken=eyJjIjp7ImNjIjoiRVMiLCJ0IjpbXSwiZiI6W10sImIiOltdLCJjIjpbXSwicyI6W10sImRyIjpbXSwidnQiOltdLCJtbSI6W10sImNsIjpbXSwiZCI6ZmFsc2UsImxjIjpbXSwicmNpIjoiIiwicmNpcyI6W10sImVuYyI6W10sImR0dCI6W10sInNzIjpbXSwidGFncyI6W10sInRzcyI6W10sInJsdCI6W10sIm9wIjpbXX0sImEiOnsiYyI6MTY2MDEyNjQ0NDE0NywiaSI6ZmFsc2UsImNjIjoiRVMiLCJpcnMiOmZhbHNlfSwibyI6W3siZCI6dHJ1ZSwiZiI6MH1dfQ%3D%3D",headers=headers_param)
# data = json.loads(response.text)
#
# #nextContinuationToken
#
# def first():
#     print(data["nextContinuationToken"])
#     for f in data["occasions"]:
#             print(
#                 {
#                     "MAKE" : f["make"],
#                     "MODEL" : f["model"],
#                     "TYPE" : f["type"],
#                     "YEAR" : f["yearOfConstruction"],
#                     "FUEL": f["fuel"],
#                     "MILEAGE" : f["mileage"]["amount"],
#                     # "UNIT" : f["mileage"]["unit"],
#                     "TRANSMISSION" : f["transmission"],
#                     "PRICE" : f["salePrice"]["amount"],
#                     "CURRENCY" : f["salePrice"]["currencyCode"],
#                     "LINK":f["_links"][0]["href"]
#                 }
#             )

# first()






