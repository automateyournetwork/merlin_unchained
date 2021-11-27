from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Netgraph/', views.netgraph_page),
    path('Netgraph/EoX_PID/', views.eox_pid_netgraph),
    path('Netgraph/EoX_PID/JSON/eox_pid_netgraph.json', views.eox_pid_json),
    path('Netgraph/EoX_SN/', views.eox_sn_netgraph),
    path('Netgraph/EoX_SN/JSON/eox_pid_netgraph.json', views.eox_sn_json),
    path('Netgraph/EoX_SW/', views.eox_sw_netgraph),
    path('Netgraph/EoX_SW/JSON/eox_pid_netgraph.json', views.eox_sw_json),
    path('Netgraph/LearnACL/', views.learn_acl_netgraph),
    path('Netgraph/LearnACL/JSON/learned_acl_netgraph.json', views.learn_acl_json),
    path('Netgraph/LearnARP/', views.learn_arp_netgraph),
    path('Netgraph/LearnARP/JSON/learned_arp_netgraph.json', views.learn_arp_json),    
    path('Netgraph/LearnPlatform/', views.learn_platform_netgraph),
    path('Netgraph/LearnPlatform/JSON/learned_platform_netgraph.json', views.learn_platform_json),
]