from django.urls import path
from . import views
from .views import OnDemandResult

urlpatterns = [
    path('OnDemand/', views.button),
    path('OnDemand/get_all_all_result/', views.get_all_all_ondemand, name="get_all_all"),
    path('OnDemand/LearnACL/learn_acl_all_result/', views.learn_acl_all_ondemand, name="learn_acl_all"),
    path('OnDemand/LearnARP/learn_arp_all_result/', views.learn_arp_all_ondemand, name="learn_arp_all"),
    path('OnDemand/LearnBGP/learn_bgp_all_result/', views.learn_bgp_all_ondemand, name="learn_bgp_all"),
    path('OnDemand/LearnVLAN/learn_vlan_all_result/', views.learn_vlan_all_ondemand, name="learn_vlan_all"),
    path('OnDemand/LearnVRF/learn_vrf_all_result/', views.learn_vrf_all_ondemand, name="learn_vrf_all"),
    path('OnDemand/ShowInventory/show_inventory_all_result/', views.show_inventory_all_ondemand, name="show_inventory_all"),
    path('OnDemand/ShowIPInterfaceBrief/show_ip_int_brief_all_result/', views.show_ip_int_brief_all_ondemand, name="show_ip_int_brief_all"),
    path('OnDemand/ShowVersion/show_version_all_result/', views.show_version_all_ondemand, name="show_version_all"),

]