from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Latest/', views.latest),
    path('Latest/All/', views.all_latest),
    path('Latest/LearnACL/', views.learn_acl_latest),
    path('Latest/LearnARP/', views.learn_arp_latest),
    path('Latest/LearnARPStatistics/', views.learn_arp_statistics_latest),
    path('Latest/LearnBGPInstances/', views.learn_bgp_instances_latest),
    path('Latest/LearnBGPRoutes/', views.learn_bgp_routes_latest),
    path('Latest/LearnBGPTables/', views.learn_bgp_tables_latest),
    path('Latest/LearnConfig/', views.learn_config_latest),
    path('Latest/LearnInterface/', views.learn_interface_latest),
    path('Latest/LearnPlatform/', views.learn_platform_latest),
    path('Latest/LearnPlatformSlots/', views.learn_platform_slots_latest),
    path('Latest/LearnPlatformVirtual/', views.learn_platform_virtual_latest),
    path('Latest/LearnVLAN/', views.learn_vlan_latest),
    path('Latest/LearnVRF/', views.learn_vrf_latest),
    path('Latest/PSIRT/', views.psirt_latest),    
    path('Latest/Recommended/', views.recommended_latest),
    path('Latest/Serial2Contract/', views.serial2contract_latest),
    path('Latest/ShowInventory/', views.show_inventory_latest),
    path('Latest/ShowIPInterfaceBrief/', views.show_ip_int_brief_latest),
    path('Latest/ShowVersion/', views.show_version_latest),
]