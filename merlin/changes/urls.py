from django.urls import path
from . import views
from .views import ChangesResultAll, ChangesResultACL, ChangesResultARP, ChangesResultARPStatistics, ChangesResultBGPInstance, ChangesResultBGPRoute, ChangesResultBGPTable, ChangesResultInterface, ChangesResultVLAN, ChangesResultVRF, ChangesResultInventory, ChangesResultIPInterfaceBrief, ChangesResultVersion

urlpatterns = [
    path('Changes/', views.changes),
    path('Changes/all_changes/', views.all_changes, name="all_changes"),
    path('Changes/learn_acl_changes/', views.learn_acl_changes, name="learn_acl_changes"),
    path('Changes/learn_arp_changes/', views.learn_arp_changes, name="learn_arp_changes"),
    path('Changes/learn_arp_statistics_changes/', views.learn_arp_statistics_changes, name="learn_arp_statistics_changes"),
    path('Changes/learn_bgp_instances_changes/', views.learn_bgp_instances_changes, name="learn_bgp_instances_changes"),
    path('Changes/learn_bgp_route_changes/', views.learn_bgp_route_changes, name="learn_bgp_route_changes"),
    path('Changes/learn_bgp_table_changes/', views.learn_bgp_table_changes, name="learn_bgp_table_changes"),
    path('Changes/learn_interface_changes/', views.learn_interface_changes, name="learn_interface_changes"),
    path('Changes/learn_vlan_changes/', views.learn_vlan_changes, name="learn_vlan_changes"),
    path('Changes/learn_vrf_changes/', views.learn_vrf_changes, name="learn_vrf_changes"),
    path('Changes/show_inventory_changes/', views.show_inventory_changes, name="show_inventory_changes"),
    path('Changes/show_ip_int_brief_changes/', views.show_ip_int_brief_changes, name="show_ip_int_brief_changes"),
    path('Changes/show_version_changes/', views.show_version_changes, name="show_version_changes"),
    path('Changes/all_changes_filter/', ChangesResultAll.as_view(), name="get_all_filter"),
    path('Changes/learn_acl_changes_filter/', ChangesResultACL.as_view(), name="learn_acl_filter"),
    path('Changes/learn_arp_changes_filter/', ChangesResultARP.as_view(), name="learn_arp_filter"),
    path('Changes/learn_arp_statistics_changes_filter/', ChangesResultARPStatistics.as_view(), name="learn_arp_statistics_filter"),
    path('Changes/learn_bgp_instance_changes_filter/', ChangesResultBGPInstance.as_view(), name="learn_bgp_instance_filter"),
    path('Changes/learn_bgp_route_changes_filter/', ChangesResultBGPRoute.as_view(), name="learn_bgp_route_filter"),
    path('Changes/learn_bgp_table_changes_filter/', ChangesResultBGPTable.as_view(), name="learn_bgp_table_filter"),
    path('Changes/learn_interface_changes_filter/', ChangesResultInterface.as_view(), name="learn_interface_filter"),
    path('Changes/learn_vlan_changes_filter/', ChangesResultVLAN.as_view(), name="learn_vlan_filter"),
    path('Changes/learn_vrf_changes_filter/', ChangesResultVRF.as_view(), name="learn_vrf_filter"),
    path('Changes/show_inventory_changes_filter/', ChangesResultInventory.as_view(), name="show_inventory_filter"),
    path('Changes/show_ip_int_brief_changes_filter/', ChangesResultIPInterfaceBrief.as_view(), name="show_ip_int_brief_filter"),
    path('Changes/show_version_changes_filter/', ChangesResultVersion.as_view(), name="show_version_filter"),
]