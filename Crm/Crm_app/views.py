from django.shortcuts import render,redirect , get_object_or_404
import os
from .forms import CK_AccountForm
import requests
from django.db.models import Q
# Create your views here.
import json
from .models import CK_Account

def login(request):
    return render(request,"html_files/login.htm")


def Admin_panel(request):
    all_enq = CK_Account.objects.all()
    total_enquiry_data = all_enq.count()
    # user = User.objects.all()
    # total_user = user.count()
    # superusers_count = User.objects.filter(is_superuser=True).count
    last_all_enq = CK_Account.objects.filter().order_by('-id')[:10]
    all_enq_in_ascending_order = reversed(last_all_enq)
    return render(request,'html_files/Main.htm',{'last_all_enq':last_all_enq,'total_enquiry_data':total_enquiry_data,'all_enq':all_enq})



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





def Enquiry_search(request):
    qur = request.GET.get('search')
    print(qur)
    print(type(qur))
    last_all_enq = CK_Account.objects.filter(Q(SENDERNAME__icontains=qur) | Q(QUERY_ID__icontains=qur) | Q(ENQ_STATE__icontains=qur) )
    return render(request,'html_files/Main.htm',{"last_all_enq":last_all_enq})


def Enquiry_Update(request,pk_id):
    obj_update = get_object_or_404(CK_Account,id=pk_id)
    form = CK_AccountForm(request.POST or None , instance=obj_update)
    if form.is_valid():
        account = form.save()
        return redirect('All_Enquiry')
    return render(request,'html_files/Dashboard.htm',{'form':form})



def Enquiry_Delete(request,pk_id):
    obj_delete = get_object_or_404(CK_Account,id=pk_id)
    if request.method == "POST":
        obj_delete.delete()
        return redirect('All_Enquiry')
    return render(request,'html_files/Dashboard.htm' , {"obj_delete":obj_delete})


