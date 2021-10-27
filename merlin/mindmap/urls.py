from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Mindmap/', views.mindmap_page),
    path('Mindmap/<str:pyats_alias>/EoPID/', views.eox_pid_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnPlatform/', views.learn_platform_mindmap),
]