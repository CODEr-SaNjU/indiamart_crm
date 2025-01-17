from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from phone_field import PhoneField
Role = [
        ('SP', 'sales Person'),
        ('PH', 'Production Head'),
        ('Ac', 'Accountant'),
        ('SM', 'Service Manager'),  
        ('STM', 'Store Manager'),
    ]

STATUS = (
    (0,"Yes"),
    (1,"No")
)






class UserRole(models.Model):
  role = models.CharField(max_length=6, choices=Role, default='green')
  
  def __str__(self):
      return self.role


class Enquiry_Source(models.Model):
    enq_source = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.enq_source




class Profession(models.Model):
    profession = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.profession

class Client_Visit(models.Model):
    Visit_status = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.Visit_status


class CK_Account(models.Model):
    username = models.ForeignKey(User, verbose_name='username', on_delete=models.CASCADE ,blank=True,null=True )
    RN = models.CharField(max_length=100,blank=True,null=True)
    QUERY_ID = models.CharField(max_length=300,blank=True,null=True)
    QTYPE = models.CharField(max_length=300,blank=True,null=True)
    SENDERNAME = models.CharField(max_length=300,blank=True,null=True)
    SENDEREMAIL = models.CharField(max_length=300,blank=True,null=True)
    SUBJECT = models.CharField(max_length=2000,blank=True,null=True)
    DATE_RE = models.CharField(max_length=300,blank=True,null=True)
    DATE_R = models.CharField(max_length=300,blank=True,null=True)
    DATE_TIME_RE = models.CharField(max_length=300,blank=True,null=True)
    GLUSR_USR_COMPANYNAME = models.CharField(max_length=1000,blank=True,null=True)
    READ_STATUS = models.CharField(max_length=300,blank=True,null=True)
    SENDER_GLUSR_USR_ID = models.CharField(max_length=300,blank=True,null=True)
    MOB = models.CharField(max_length=300,blank=True,null=True)
    COUNTRY_FLAG =  models.ImageField(upload_to='uploads/',blank=True,null=True)
    QUERY_MODID = models.CharField(max_length=300,blank=True,null=True)
    LOG_TIME = models.CharField(max_length=300,blank=True,null=True)
    QUERY_MODREFID = models.CharField(max_length=300,blank=True,null=True)
    DIR_QUERY_MODREF_TYPE = models.CharField(max_length=300,blank=True,null=True)
    ORG_SENDER_GLUSR_ID = models.CharField(max_length=300,blank=True,null=True)
    ENQ_MESSAGE = models.CharField(max_length=2030,blank=True,null=True)
    ENQ_ADDRESS = models.CharField(max_length=2000,blank=True,null=True)
    ENQ_CALL_DURATION = models.CharField(max_length=300,blank=True,null=True)
    ENQ_RECEIVER_MOB = models.CharField(max_length=300,blank=True,null=True)
    ENQ_CITY =  models.CharField(max_length=300,blank=True,null=True)
    ENQ_STATE = models.CharField(max_length=300,blank=True,null=True)
    PRODUCT_NAME = models.CharField(max_length=300,blank=True,null=True)
    COUNTRY_ISO = models.CharField(max_length=300,blank=True,null=True)
    EMAIL_ALT = models.CharField(max_length=300,blank=True,null=True)
    MOBILE_ALT = models.CharField(max_length=300,blank=True,null=True)
    PHONE = models.CharField(max_length=300,blank=True,null=True)
    PHONE_ALT = models.CharField(max_length=300,blank=True,null=True)
    IM_MEMBER_SINCE = models.CharField(max_length=300,blank=True,null=True)
    TOTAL_COUNT = models.CharField(max_length=300,blank=True,null=True)
    enquiry_source = models.ForeignKey(Enquiry_Source,on_delete=models.CASCADE,null=True,blank=True )
    expected_purchase_Date = models.DateField(verbose_name='Expected Purchase Date',auto_now_add=False,blank=True,null=True)
    profession = models.ForeignKey(Profession,on_delete=models.CASCADE,null=True,blank=True )
    visit_date = models.DateField(verbose_name='Visit Date',auto_now_add=False,blank=True,null=True)
    visited_status = models.IntegerField(choices=STATUS, default=1)
    Visit_status = models.ForeignKey(Client_Visit,on_delete=models.CASCADE,null=True,blank=True )
    Booking_Date = models.DateField(verbose_name='Booking Date',auto_now_add=False,blank=True,null=True)
    remarks  = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.QUERY_ID

