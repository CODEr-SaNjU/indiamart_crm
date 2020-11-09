from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name="login"),
    path("Api_data/",views.api_data,name="Api_data"),
    path("Admin_Panel/",views.Admin_panel,name="Admin_panel"),


]