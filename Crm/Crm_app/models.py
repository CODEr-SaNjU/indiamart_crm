from django.db import models

# Create your models here.


class CK_Account(models.Model):
    RN = models.CharField(max_length=10)
    QUERY_ID = models.CharField(max_length=30)
    QTYPE = models.CharField(max_length=30)
    SENDERNAME = models.CharField(max_length=30)
    SENDEREMAIL = models.CharField(max_length=30)
    SUBJECT = models.CharField(max_length=2000)
    DATE_RE = models.CharField(max_length=30)
    DATE_R = models.CharField(max_length=30)
    DATE_TIME_RE = models.CharField(max_length=30)
    GLUSR_USR_COMPANYNAME = models.CharField(max_length=1000)
    READ_STATUS = models.CharField(max_length=30)
    SENDER_GLUSR_USR_ID = models.CharField(max_length=30)
    MOB = models.CharField(max_length=30)
    COUNTRY_FLAG =  models.ImageField(upload_to='uploads/',)
    QUERY_MODID = models.CharField(max_length=30)
    LOG_TIME = models.CharField(max_length=30)
    QUERY_MODREFID = models.CharField(max_length=30)
    DIR_QUERY_MODREF_TYPE = models.CharField(max_length=30)
    ORG_SENDER_GLUSR_ID = models.CharField(max_length=30)
    ENQ_MESSAGE = models.CharField(max_length=2030)
    ENQ_ADDRESS = models.CharField(max_length=2000)
    ENQ_CALL_DURATION = models.CharField(max_length=30)
    ENQ_RECEIVER_MOB = models.CharField(max_length=30)
    ENQ_CITY =  models.CharField(max_length=30)
    ENQ_STATE = models.CharField(max_length=30)
    PRODUCT_NAME = models.CharField(max_length=30)
    COUNTRY_ISO = models.CharField(max_length=30)
    EMAIL_ALT = models.CharField(max_length=30)
    MOBILE_ALT = models.CharField(max_length=30)
    PHONE = models.CharField(max_length=30)
    PHONE_ALT = models.CharField(max_length=30)
    IM_MEMBER_SINCE = models.CharField(max_length=30)
    TOTAL_COUNT = models.CharField(max_length=30)

         