from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Interfaces/<str:pyats_alias>/', views.shut_noshut),
    path('Interfaces/result/', views.result),
]