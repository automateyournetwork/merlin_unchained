from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Interfaces/', views.device_list, name="device_list"),
    path('Interfaces/<str:pyats_alias>/', views.shut_noshut, name="shut_noshut"),
]