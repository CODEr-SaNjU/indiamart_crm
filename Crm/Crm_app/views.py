from django.shortcuts import render
import os
import requests
# Create your views here.
import json


def login(request):
    return render(request,"html_files/login.htm")





def api_data(request):
    Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/8469789298/GLUSR_MOBILE_KEY/MTYwMjgzMTEyNS40NDg0IzExMjc0OTQ0/")
    data = Url.json()
    for i in range(len(data)):
        x = data[i]
        for i in x.items():
            all_data = i[1]
    return render(request,'html_files/Api_Data.htm',{"all_data":all_data})