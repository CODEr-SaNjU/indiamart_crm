from django.shortcuts import render
import os
import requests
# Create your views here.
import json
from .models import CK_Account

def login(request):
    return render(request,"html_files/login.htm")





def api_data(request):
    if request.method == "POST":
        print("sanju")
        Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/9909775046/GLUSR_MOBILE_KEY/MTYwMjgzMDcyMC4zMTIjNDg5NjA5NjY=/",data = request.POST)
    else:
        Url = requests.get("https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/9909775046/GLUSR_MOBILE_KEY/MTYwMjgzMDcyMC4zMTIjNDg5NjA5NjY=/",data = request.POST)
    
    if Url.status_code == 200:
        data = Url.json()
        for i in range(len(data)):
            x = data[i]
            print("x")
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
            
            ck_account = CK_Account.objects.create(RN=RN, QUERY_ID=QUERY_ID, QTYPE=QTYPE, SENDERNAME=SENDERNAME, SENDEREMAIL=SENDEREMAIL, SUBJECT=SUBJECT, DATE_RE=DATE_RE, DATE_R=DATE_R, DATE_TIME_RE=DATE_TIME_RE, GLUSR_USR_COMPANYNAME=GLUSR_USR_COMPANYNAME, READ_STATUS=READ_STATUS, SENDER_GLUSR_USR_ID=SENDER_GLUSR_USR_ID, MOB=MOB, QUERY_MODID=QUERY_MODID, LOG_TIME=LOG_TIME, QUERY_MODREFID=QUERY_MODREFID, DIR_QUERY_MODREF_TYPE=DIR_QUERY_MODREF_TYPE, ORG_SENDER_GLUSR_ID=ORG_SENDER_GLUSR_ID, ENQ_MESSAGE=ENQ_MESSAGE, ENQ_ADDRESS=ENQ_ADDRESS, ENQ_CALL_DURATION=ENQ_CALL_DURATION, ENQ_RECEIVER_MOB=ENQ_RECEIVER_MOB, ENQ_CITY=ENQ_CITY, ENQ_STATE=ENQ_STATE, PRODUCT_NAME=PRODUCT_NAME, COUNTRY_ISO=COUNTRY_ISO, EMAIL_ALT=EMAIL_ALT, MOBILE_ALT=MOBILE_ALT, PHONE=PHONE, PHONE_ALT=PHONE_ALT, IM_MEMBER_SINCE=IM_MEMBER_SINCE, TOTAL_COUNT=TOTAL_COUNT)
            ck_account.save()
    return render(request,'html_files/Api_Data.htm')



    #   for i in range(len(data)):
    #     x = data[i]
    #     for i in x.items():
    #         all_data = i[1]
    # if request.method == "POST":