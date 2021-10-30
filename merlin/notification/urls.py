from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [  
    path('Notification/', views.device_list, name="device_list"),
    path('Notification/<str:pyats_alias>/', views.device_notifications, name="device_notifications"),
]