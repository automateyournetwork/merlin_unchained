from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Mindmap/', views.mindmap_page),
    path('Mindmap/<str:pyats_alias>/EoX_PID/', views.eox_pid_mindmap),
    path('Mindmap/<str:pyats_alias>/EoX_SN/', views.eox_sn_mindmap),
    path('Mindmap/<str:pyats_alias>/EoX_SW/', views.eox_sw_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnACL/', views.learn_acl_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnARP/', views.learn_arp_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnARPStatistics/', views.learn_arp_statistics_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnBGPInstances/', views.learn_bgp_instances_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnBGPRoutes/', views.learn_bgp_route_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnBGPTables/', views.learn_bgp_table_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnInterface/', views.learn_interface_mindmap),
    path('Mindmap/<str:pyats_alias>/LearnPlatform/', views.learn_platform_mindmap),
    path('Mindmap/<str:pyats_alias>/ShowLicenseSummary/', views.show_license_summary_mindmap),
]