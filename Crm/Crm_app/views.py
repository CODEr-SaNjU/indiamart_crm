from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.models import User,auth ,Group
from django.http import Http404, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from django.contrib.auth import authenticate,get_user_model
from django.contrib import auth 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user ,allowed_user ,admin_only
import datetime  
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
import os
from django.http import JsonResponse
from .forms import CK_AccountForm ,UserForm 
import requests
from django.db.models import Q
import json
from django.urls import reverse_lazy
from .models import CK_Account
import datetime
from django.template.loader import render_to_string
from django.contrib import auth 
from bootstrap_modal_forms.generic import BSModalCreateView

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Admin_panel')
        else:
            messages.error(request, 'Error! please enter the correct  Username and Password for a staff account.')
            return render(request,'html_files/login.htm')

    else:
        return render(request,"html_files/login.htm")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return render(request,'html_files/logout.htm')


@login_required(login_url='login')
@admin_only
def Admin_panel(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            messages.success(request, f'Registration complete! You may log in!')
    else:
        userform = UserForm(request.POST)
    all_enq = CK_Account.objects.all()
    all_user = User.objects.all()
    total_enquiry_data = all_enq.count()
    assign_enq = CK_Account.objects.filter(username__isnull=False)
    assign_enq_count = CK_Account.objects.filter(username__isnull=False).count()
    notassign_enq = CK_Account.objects.filter(username__isnull=True)
    notassign_enq_count = CK_Account.objects.filter(username__isnull=True).count()
    last_all_enq = CK_Account.objects.filter().order_by('-id')[:10]
    all_enq_in_ascending_order = reversed(last_all_enq)

    return render(request,'html_files/Main.htm',{'last_all_enq':last_all_enq,'total_enquiry_data':total_enquiry_data,'all_enq':all_enq,'userform': userform, 'all_user':all_user,'assign_enq':assign_enq,'notassign_enq':notassign_enq,'assign_enq_count':assign_enq_count,'notassign_enq_count':notassign_enq_count})





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


def search_enq_month(request):
    qur = request.GET.get('search')
    qur1 = request.GET.get("search1")
    datetime_object = datetime.datetime.strptime(qur1, "%Y-%m-%d")
    datetime_object2 = datetime.datetime.strptime(qur, "%Y-%m-%d")
    strt = datetime_object.strftime("%d-%m-%Y")
    endt = datetime_object2.strftime("%d-%m-%Y")
    print(strt)
    all_enq = CK_Account.objects.filter(DATE_R__lte= "01-Nov-20",DATE_R__gte = "02-Nov-20")
    print(all_enq)
    return render(request,'html_files/Main.htm',{"all_enq":all_enq})



def Enquiry_search(request):
    qur = request.GET.get('search')
    print(qur)
    print(type(qur))
    all_enq = CK_Account.objects.filter(Q(SENDERNAME__icontains=qur) | Q(QUERY_ID__icontains=qur) | Q(ENQ_STATE__icontains=qur) )
    return render(request,'html_files/Main.htm',{"all_enq":all_enq})

   


@login_required(login_url='login')
def saleperson_page(request):
    last_all_enq = CK_Account.objects.filter(username=request.user)
    return render(request,'html_files/salesperson.htm',{'last_all_enq':last_all_enq})



def save_enq_form(request, form, template_name):
    data = dict()
    print("sanju herer",data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            last_all_enq = CK_Account.objects.all()
            last_all_enq = CK_Account.objects.filter().order_by('-id')[:10]
            data['html_enq_list'] = render_to_string('html_files/enq_list.htm',{'last_all_enq':last_all_enq})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def enq_create(request):
    data = dict()
    if request.method == 'POST':
        form = CK_AccountForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            last_all_enq = CK_Account.objects.all()
            data['html_enq_list'] = render_to_string('html_files/enq_list.htm',{'last_all_enq':last_all_enq})
        else:
            data['form_is_valid'] =False
    else:
        form = CK_AccountForm()
    context={'form':form}
    data['html_form']  = render_to_string('html_files/add_enq.htm',context,request=request)
    return JsonResponse(data)



def Enquiry_Update(request,pk_id):
    obj_update = get_object_or_404(CK_Account,id=pk_id)
    if request.method=="POST":
        form = CK_AccountForm(request.POST, instance=obj_update)
    else:
        form = CK_AccountForm(instance=obj_update)
    return save_enq_form(request,form,'html_files/enquiry_update.htm')
    

def Enquiry_Delete(request,pk_id):
    obj_delete = get_object_or_404(CK_Account,id=pk_id)
    data = dict()
    if request.method == "POST":
        obj_delete.delete()
        data['form_is_valid'] = True
        last_all_enq = CK_Account.objects.filter().order_by('-id')[:10]
        data['html_enq_list'] = render_to_string('html_files/enq_list.htm',{'last_all_enq':last_all_enq})
    else:
        data['html_form'] = render_to_string('html_files/enquiry_delete.htm', {'obj_delete':obj_delete}, request=request)
    return JsonResponse(data)


def save_user_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            all_user = User.objects.all()
            data['html_user_list'] = render_to_string('html_files/all_user_list.htm',{'all_user':all_user})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data) 



def user_update(request,pk_id):
    user_update = get_object_or_404(User,id=pk_id)
    if request.method=="POST":
        form = UserForm(request.POST, instance=user_update)
    else:
        form = UserForm(instance=user_update)
    return save_user_form(request,form,'html_files/user_update.htm')


def user_delete(request,pk_id):
    user_delete = get_object_or_404(User,id=pk_id)
    data = dict()
    if request.method=="POST":
        user_delete.delete()
        data['form_is_valid'] = True
        all_user = User.objects.all()
        data['html_user_list'] = render_to_string('html_files/all_user_list.htm',{'all_user':all_user})
    else:
        data['html_form'] = render_to_string('html_files/user_delete.htm', {'user_delete':user_delete}, request=request)
    return JsonResponse(data)

