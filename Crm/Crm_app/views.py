from django.shortcuts import render
import os
import requests
# Create your views here.
import json


def login(request):
    return render(request,"html_files/login.htm")





def api_data(request):
    return render(request,'html_files/Api_Data.htm')