from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Mindmap/', views.mindmap_page),
    path('Mindmap/<str:pyats_alias>/EoX_PID/', views.eox_pid_mindmap),
    path('Mindmap/<str:pyats_alias>/EoX_SN/', views.eox_sn_mindmap),
    path('Mindmap/<str:pyats_alias>/EoX_SW/', views.eox_sw_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnACL/', views.learn_acl_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnPlatform/', views.learn_platform_mindmap),
]