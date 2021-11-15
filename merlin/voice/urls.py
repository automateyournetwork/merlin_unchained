from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Voice/', views.voice_page),
    path('Voice/Learn/', views.learn_voice_page),
    path('Voice/Show/', views.show_voice_page),
    path('Voice/Config/', views.config_voice_page),
]
