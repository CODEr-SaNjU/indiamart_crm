from django.shortcuts import render
import os
import requests
# Create your views here.
import json
from .models import CK_Account

def login(request):
    return render(request,"html_files/login.htm")


def Admin_panel(request):
    return render(request,"html_files/Dashboard.htm")


def api_data(request):
    if request.method == "POST":
        print("sanju")
        Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/8469789298/GLUSR_MOBILE_KEY/MTYwMjgzMTEyNS40NDg0IzExMjc0OTQ0/",data = request.POST)
    else:
        Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/8469789298/GLUSR_MOBILE_KEY/MTYwMjgzMTEyNS40NDg0IzExMjc0OTQ0/",data = request.POST)    
    if Url.status_code == 200:
        data = Url.json()
        for i in range(len(data)):
            x = data[i]
            RN= x["RN"] 
            QUERY_ID= x["QUERY_ID"] 
            QTYPE= x["QTYPE"]
            SENDERNAME= x["SENDERNAME"]
            SENDEREMAIL= x["SENDEREMAIL"]
            SUBJECT= x["SUBJECT"]
            DATE_RE= x["DATE_RE"]
            DATE_R= x["DATE_R"]
            DATE_TIME_RE= x["DATE_TIME_RE"]
            GLUSR_USR_COMPANYNAME= x["GLUSR_USR_COMPANYNAME"] 
            READ_STATUS= x["READ_STATUS"]
            SENDER_GLUSR_USR_ID= x["SENDER_GLUSR_USR_ID"]
            MOB= x["MOB"]
            COUNTRY_FLAG= x["COUNTRY_FLAG"]
            QUERY_MODID= x["QUERY_MODID"]
            LOG_TIME= x["LOG_TIME"]
            QUERY_MODREFID= x["QUERY_MODREFID"]
            DIR_QUERY_MODREF_TYPE= x["DIR_QUERY_MODREF_TYPE"]
            ORG_SENDER_GLUSR_ID= x["ORG_SENDER_GLUSR_ID"]
            ENQ_MESSAGE= x["ENQ_MESSAGE"]
            ENQ_ADDRESS= x["ENQ_ADDRESS"]
            ENQ_CALL_DURATION= x["ENQ_CALL_DURATION"]
            ENQ_RECEIVER_MOB= x["ENQ_RECEIVER_MOB"]
            ENQ_CITY= x["ENQ_CITY"]
            ENQ_STATE= x["ENQ_STATE"]
            PRODUCT_NAME= x["PRODUCT_NAME"]
            COUNTRY_ISO= x["COUNTRY_ISO"]
            EMAIL_ALT= x["EMAIL_ALT"]
            MOBILE_ALT= x["MOBILE_ALT"]
            PHONE= x["PHONE"]
            PHONE_ALT= x["PHONE_ALT"]
            IM_MEMBER_SINCE= x["IM_MEMBER_SINCE"]
            TOTAL_COUNT = x["TOTAL_COUNT"]
            ck_account = CK_Account.objects.create(RN=RN, QUERY_ID=QUERY_ID, QTYPE=QTYPE, SENDERNAME=SENDERNAME, SENDEREMAIL=SENDEREMAIL, SUBJECT=SUBJECT, DATE_RE=DATE_RE, DATE_R=DATE_R, DATE_TIME_RE=DATE_TIME_RE, SENDER_GLUSR_USR_ID=SENDER_GLUSR_USR_ID, MOB=MOB, QUERY_MODID=QUERY_MODID, LOG_TIME=LOG_TIME, ENQ_MESSAGE=ENQ_MESSAGE, ENQ_ADDRESS=ENQ_ADDRESS, ENQ_CALL_DURATION=ENQ_CALL_DURATION, ENQ_RECEIVER_MOB=ENQ_RECEIVER_MOB, ENQ_CITY=ENQ_CITY, ENQ_STATE=ENQ_STATE, PRODUCT_NAME=PRODUCT_NAME, COUNTRY_ISO=COUNTRY_ISO,PHONE_ALT=PHONE_ALT, TOTAL_COUNT=TOTAL_COUNT)
            ck_account.save()
    return render(request,'html_files/Api_Data.htm')


def All_Enquiry(request):
    all_enq = CK_Account.objects.all()
    return render(request,'html_files/Dashboard.htm',{"all_enq":all_enq})



def Enquiry_search(request):
    qur = request.GET.get('search')
    print(qur)
    print(type(qur))
    all_enq = CK_Account.objects.filter(SENDERNAME__contains= qur)
    # all_enq = [item for item in CK_Account.objects.all() if qur in item.QUERY_ID or qur in item.SENDERNAME or qur in item.ENQ_STATE]
    return render(request,'html_files/Dashboard.htm',{"all_enq":all_enq})