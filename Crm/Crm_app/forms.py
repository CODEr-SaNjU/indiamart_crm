from django import forms
from .models import CK_Account
from django.contrib.auth.models import User

from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.forms import BSModalModelForm


class CK_AccountForm(forms.ModelForm):
    class Meta:
        model =CK_Account
        fields = ['username','enquiry_source','profession','visited_status','Visit_status','RN','QUERY_ID','QTYPE','SENDERNAME','SENDEREMAIL','SUBJECT','DATE_RE','DATE_R','DATE_TIME_RE','GLUSR_USR_COMPANYNAME','READ_STATUS','SENDER_GLUSR_USR_ID','MOB','QUERY_MODID','LOG_TIME','QUERY_MODREFID','DIR_QUERY_MODREF_TYPE','ORG_SENDER_GLUSR_ID','ENQ_MESSAGE','ENQ_ADDRESS','ENQ_CALL_DURATION','ENQ_RECEIVER_MOB','ENQ_CITY','ENQ_STATE','PRODUCT_NAME','COUNTRY_ISO','EMAIL_ALT','MOBILE_ALT','PHONE','PHONE_ALT','IM_MEMBER_SINCE','TOTAL_COUNT','expected_purchase_Date','visit_date','Booking_Date','remarks']
        widgets = {
          'RN' : forms.TextInput(attrs={'class':'form-control','id':'rnid'}),
          'QUERY_ID' : forms.TextInput(attrs={'class':'form-control','id':'queryid'}),
          'QTYPE' : forms.TextInput(attrs={'class':'form-control','id':'qtypeid'}),
          'SENDERNAME' : forms.TextInput(attrs={'class':'form-control','id':'sendernameid'}),
          'SENDEREMAIL' : forms.TextInput(attrs={'class':'form-control','id':'SENDEREMAILid'}),
          'SUBJECT' : forms.Textarea(attrs={'class':'form-control','id':'SUBJECTid'}),
          'DATE_RE' : forms.TextInput(attrs={'class':'form-control','id':'DATE_REid'}),
          'DATE_R' : forms.TextInput(attrs={'class':'form-control','id':'DATE_Rid'}),
          'DATE_TIME_RE' : forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','id':'DATE_TIME_REid'}),
          'GLUSR_USR_COMPANYNAME' : forms.TextInput(attrs={'class':'form-control','id':'GLUSR_USR_COMPANYNAMEid'}),
          'READ_STATUS' : forms.TextInput(attrs={'class':'form-control','id':'READ_STATUSid'}),
          'SENDER_GLUSR_USR_ID' : forms.TextInput(attrs={'class':'form-control','id':'SENDER_GLUSR_USR_IDid'}),
          'MOB' : forms.TextInput(attrs={'class':'form-control','id':'MOBid'}),
          'QUERY_MODID' : forms.TextInput(attrs={'class':'form-control','id':'QUERY_MODIDid'}),
          'GLUSR_USR_COMPANYNAMEid' : forms.TextInput(attrs={'class':'form-control','id':'GLUSR_USR_COMPANYNAMEid'}),
          'ENQ_MESSAGE':forms.Textarea(attrs={'class':'form-control'})

        }
        labels = {
            'username': ('Assign to user')
        }




class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
          'username' : forms.TextInput(attrs={'class':'form-control','id':'usernameid'}),
          'first_name' : forms.TextInput(attrs={'class':'form-control','id':'first_nameid'}),
          'email' : forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
          'password1' : forms.PasswordInput(attrs={'class':'form-control','id':'password1id'}),
          'password2' : forms.PasswordInput(attrs={'class':'form-control','id':'password2id'}),
        }
        labels = {
            'first_name': ('full Name')
        }

