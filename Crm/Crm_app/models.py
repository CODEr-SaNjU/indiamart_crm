from django.db import models

# Create your models here.


class CK_Account(models.Model):
    RN = models.CharField(max_length=100)
    QUERY_ID = models.CharField(max_length=300)
    QTYPE = models.CharField(max_length=300)
    SENDERNAME = models.CharField(max_length=300)
    SENDEREMAIL = models.CharField(max_length=300)
    SUBJECT = models.CharField(max_length=2000)
    DATE_RE = models.CharField(max_length=300)
    DATE_R = models.CharField(max_length=300)
    DATE_TIME_RE = models.CharField(max_length=300)
    GLUSR_USR_COMPANYNAME = models.CharField(max_length=1000)
    READ_STATUS = models.CharField(max_length=300)
    SENDER_GLUSR_USR_ID = models.CharField(max_length=300)
    MOB = models.CharField(max_length=300)
    COUNTRY_FLAG =  models.ImageField(upload_to='uploads/',)
    QUERY_MODID = models.CharField(max_length=300)
    LOG_TIME = models.CharField(max_length=300)
    QUERY_MODREFID = models.CharField(max_length=300)
    DIR_QUERY_MODREF_TYPE = models.CharField(max_length=300)
    ORG_SENDER_GLUSR_ID = models.CharField(max_length=300)
    ENQ_MESSAGE = models.CharField(max_length=2030)
    ENQ_ADDRESS = models.CharField(max_length=2000)
    ENQ_CALL_DURATION = models.CharField(max_length=300)
    ENQ_RECEIVER_MOB = models.CharField(max_length=300)
    ENQ_CITY =  models.CharField(max_length=300)
    ENQ_STATE = models.CharField(max_length=300)
    PRODUCT_NAME = models.CharField(max_length=300)
    COUNTRY_ISO = models.CharField(max_length=300)
    EMAIL_ALT = models.CharField(max_length=300)
    MOBILE_ALT = models.CharField(max_length=300)
    PHONE = models.CharField(max_length=300)
    PHONE_ALT = models.CharField(max_length=300)
    IM_MEMBER_SINCE = models.CharField(max_length=300)
    TOTAL_COUNT = models.CharField(max_length=300)

         