from django.contrib import admin
from .models import CK_Account  ,UserRole ,Profession,Client_Visit,Enquiry_Source


# Register your models here.






admin.site.register(CK_Account)
admin.site.register(UserRole)
admin.site.register(Profession)
admin.site.register(Client_Visit)
admin.site.register(Enquiry_Source)