from django import forms
from .models import CK_Account , UserReg
from django.contrib.auth.models import User

from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.forms import BSModalModelForm


class CK_AccountForm(BSModalModelForm):
    class Meta:
        model =CK_Account
        fields = ['username','RN','QUERY_ID','QTYPE','SENDERNAME','SENDEREMAIL','SUBJECT','DATE_RE','DATE_R','DATE_TIME_RE','GLUSR_USR_COMPANYNAME','READ_STATUS','SENDER_GLUSR_USR_ID','MOB','QUERY_MODID','LOG_TIME','QUERY_MODREFID','DIR_QUERY_MODREF_TYPE','ORG_SENDER_GLUSR_ID','ENQ_MESSAGE','ENQ_ADDRESS','ENQ_CALL_DURATION','ENQ_RECEIVER_MOB','ENQ_CITY','ENQ_STATE','PRODUCT_NAME','COUNTRY_ISO','EMAIL_ALT','MOBILE_ALT','PHONE','PHONE_ALT','IM_MEMBER_SINCE','TOTAL_COUNT']