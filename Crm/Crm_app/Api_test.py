import requests
import json
Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/8469789298/GLUSR_MOBILE_KEY/MTYwMjgzMTEyNS40NDg0IzExMjc0OTQ0/")
data = Url.json()
# print(data)
# print(type(data))
for i in range(len(data)):
    x = data[i]
    for i in x.items():
        data_1 = i[1]
        print(data_1)
    