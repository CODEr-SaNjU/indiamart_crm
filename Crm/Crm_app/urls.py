from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name="login"),
    path("Api_data/",views.api_data,name="Api_data"),
    path("Admin_Panel/",views.Admin_panel,name="Admin_panel"),
    path("All_enq/",views.All_Enquiry,name="All_Enquiry"),
    path("Enquiry_search/",views.Enquiry_search,name="Enquiry_search"),
    path("Enquiry_Update/<str:pk_id>/",views.Enquiry_Update,name="Enquiry_Update"),
    path("Enquiry_Delete/<str:pk_id>/",views.Enquiry_Delete,name="Enquiry_Delete"),

]