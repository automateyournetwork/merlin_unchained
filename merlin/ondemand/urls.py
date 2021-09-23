from django.urls import path
from . import views
from .views import OnDemandResultAll, OnDemandResultACL, OnDemandResultARP, OnDemandResultBGP, OnDemandResultConfig, OnDemandResultInterface, OnDemandResultPlatform, OnDemandResultVLAN, OnDemandResultVRF, OnDemandResultInventory, OnDemandResultIPInterfaceBrief, OnDemandResultVersion

urlpatterns = [
    path('OnDemand/', views.button),
    path('OnDemand/GetAll/get_all_all_result/', views.get_all_all_ondemand, name="get_all_all"),
    path('OnDemand/LearnACL/learn_acl_all_result/', views.learn_acl_all_ondemand, name="learn_acl_all"),
    path('OnDemand/LearnARP/learn_arp_all_result/', views.learn_arp_all_ondemand, name="learn_arp_all"),
    path('OnDemand/LearnBGP/learn_bgp_all_result/', views.learn_bgp_all_ondemand, name="learn_bgp_all"),
    path('OnDemand/LearnConfig/learn_config_all_result/', views.learn_config_all_ondemand, name="learn_config_all"),
    path('OnDemand/LearnInterface/learn_interface_all_result/', views.learn_interface_all_ondemand, name="learn_interface_all"),
    path('OnDemand/LearnPlatform/learn_platform_all_result/', views.learn_platform_all_ondemand, name="learn_platform_all"),
    path('OnDemand/LearnVLAN/learn_vlan_all_result/', views.learn_vlan_all_ondemand, name="learn_vlan_all"),
    path('OnDemand/LearnVRF/learn_vrf_all_result/', views.learn_vrf_all_ondemand, name="learn_vrf_all"),
    path('OnDemand/ShowInventory/show_inventory_all_result/', views.show_inventory_all_ondemand, name="show_inventory_all"),
    path('OnDemand/ShowIPInterfaceBrief/show_ip_int_brief_all_result/', views.show_ip_int_brief_all_ondemand, name="show_ip_int_brief_all"),
    path('OnDemand/ShowVersion/show_version_all_result/', views.show_version_all_ondemand, name="show_version_all"),
    path('OnDemand/GetAll/get_all_filter_result/', OnDemandResultAll.as_view(), name="get_all_filter"),
    path('OnDemand/LearnACL/learn_acl_filter_result/', OnDemandResultACL.as_view(), name="learn_acl_filter"),
    path('OnDemand/LearnARP/learn_arp_filter_result/', OnDemandResultARP.as_view(), name="learn_arp_filter"),
    path('OnDemand/LearnBGP/learn_bgp_filter_result/', OnDemandResultBGP.as_view(), name="learn_bgp_filter"),
    path('OnDemand/LearnConfig/learn_config_filter_result/', OnDemandResultConfig.as_view(), name="learn_config_filter"),
    path('OnDemand/LearnInterface/learn_interface_filter_result/', OnDemandResultInterface.as_view(), name="learn_interface_filter"),
    path('OnDemand/LearnPlatform/learn_platform_filter_result/', OnDemandResultPlatform.as_view(), name="learn_platform_filter"),
    path('OnDemand/LearnVLAN/learn_vlan_filter_result/', OnDemandResultVLAN.as_view(), name="learn_vlan_filter"),
    path('OnDemand/LearnVRF/learn_vrf_filter_result/', OnDemandResultVRF.as_view(), name="learn_vrf_filter"),
    path('OnDemand/ShowInventory/show_inventory_filter_result/', OnDemandResultInventory.as_view(), name="show_inventory_filter"),
    path('OnDemand/ShowIPInterfaceBrief/show_ip_int_brief_filter_result/', OnDemandResultIPInterfaceBrief.as_view(), name="show_ip_int_brief_filter"),
    path('OnDemand/ShowVersion/show_version_filter_result/', OnDemandResultVersion.as_view(), name="show_version_filter"),
]