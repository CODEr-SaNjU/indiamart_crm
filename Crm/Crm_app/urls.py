from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name="login"),
    path("Api_data/",views.api_data,name="Api_data"),
    path("Admin_panel/",views.Admin_panel,name="Admin_panel"),
    path("Enquiry_search/",views.Enquiry_search,name="Enquiry_search"),
    path("search_enq_month/",views.search_enq_month,name="search_enq_month"),
    path("Enquiry_Update/<str:pk_id>/",views.Enquiry_Update,name="Enquiry_Update"),
    path("Enquiry_Delete/<str:pk_id>/",views.Enquiry_Delete,name="Enquiry_Delete"),
    path("logout/",views.logout,name="logout"),
    path("register/",views.register,name="register"),
    path("salesperson/",views.saleperson_page,name="saleperson"),
    path('create_enquiry/', views.enqCreateView.as_view(), name='create_enquiry'),


]