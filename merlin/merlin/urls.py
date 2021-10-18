"""merlin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('', include('ondemand.urls')),
    path('', include('search.urls')),
    path('', include('changes.urls')),
    path('API/', include('merlin_api.urls')),
    path('', include('spreadsheet.urls')),
    path('', include('latest.urls')),
    path('HTML/', views.html),
    path('Devices/All/', views.devices_all),
    path('Devices/<int:year>/', views.devices_year_archive),
    path('Devices/<int:year>/<int:month>/', views.devices_month_archive),
    path('Devices/<int:year>/<int:month>/<int:day>/', views.devices_day_archive),
    path('Devices/Hostname/<str:hostname>/', views.devices_hostname_archive),
    path('Devices/Alias/<str:alias>/', views.devices_alias_archive),
    path('Devices/OS/<str:os>', views.devices_os_archive),
    path('Devices/Type/<str:device_type>', views.devices_device_type_archive),
    path('Devices/Username/<str:username>', views.devices_username_archive),
    path('Devices/Protocol/<str:protocol>', views.devices_protocol_archive),
    path('Devices/IP/<str:ip_address>', views.devices_ip_address_archive),
    path('Devices/Port/<str:port>', views.devices_port_archive),
    path('EoX_PID/All/', views.eox_pid_all),
    path('EoX_PID/<int:year>/', views.eox_pid_year_archive),
    path('EoX_PID/<int:year>/<int:month>/', views.eox_pid_month_archive),
    path('EoX_PID/<int:year>/<int:month>/<int:day>/', views.eox_pid_day_archive),
    path('EoX_PID/nxos/', views.eox_pid_nxos_archive),
    path('EoX_PID/<str:pyats_alias>/', views.eox_pid_alias_archive),
    path('EoX_SN/All/', views.eox_sn_all),
    path('EoX_SN/<int:year>/', views.eox_sn_year_archive),
    path('EoX_SN/<int:year>/<int:month>/', views.eox_sn_month_archive),
    path('EoX_SN/<int:year>/<int:month>/<int:day>/', views.eox_sn_day_archive),
    path('EoX_SN/nxos/', views.eox_sn_nxos_archive),
    path('EoX_SN/<str:pyats_alias>/', views.eox_sn_alias_archive),
    path('EoX_SW/All/', views.eox_sw_all),
    path('EoX_SW/<int:year>/', views.eox_sw_year_archive),
    path('EoX_SW/<int:year>/<int:month>/', views.eox_sw_month_archive),
    path('EoX_SW/<int:year>/<int:month>/<int:day>/', views.eox_sw_day_archive),
    path('EoX_SW/nxos/', views.eox_sw_nxos_archive),
    path('EoX_SW/<str:pyats_alias>/', views.eox_sw_alias_archive),    
    path('LearnACL/All/', views.learn_acl_all),
    path('LearnACL/<int:year>/', views.learn_acl_year_archive),
    path('LearnACL/<int:year>/<int:month>/', views.learn_acl_month_archive),
    path('LearnACL/<int:year>/<int:month>/<int:day>/', views.learn_acl_day_archive),
    path('LearnACL/nxos/', views.learn_acl_nxos_archive),
    path('LearnACL/<str:pyats_alias>/', views.learn_acl_alias_archive),
    path('LearnARP/All/', views.learn_arp_all),
    path('LearnARP/<int:year>/', views.learn_arp_year_archive),
    path('LearnARP/<int:year>/<int:month>/', views.learn_arp_month_archive),
    path('LearnARP/<int:year>/<int:month>/<int:day>/', views.learn_arp_day_archive),
    path('LearnARP/nxos/', views.learn_arp_nxos_archive),
    path('LearnARP/<str:pyats_alias>/', views.learn_arp_alias_archive),
    path('LearnARPStatistics/All/', views.learn_arp_statistics_all),
    path('LearnARPStatistics/<int:year>/', views.learn_arp_statistics_year_archive),
    path('LearnARPStatistics/<int:year>/<int:month>/', views.learn_arp_statistics_month_archive),
    path('LearnARPStatistics/<int:year>/<int:month>/<int:day>/', views.learn_arp_statistics_day_archive),
    path('LearnARPStatistics/nxos/', views.learn_arp_statistics_nxos_archive),
    path('LearnARPStatistics/<str:pyats_alias>/', views.learn_arp_statistics_alias_archive),
    path('LearnBGPInstances/All/', views.learn_bgp_instances_all),
    path('LearnBGPInstances/<int:year>/', views.learn_bgp_instances_year_archive),
    path('LearnBGPInstances/<int:year>/<int:month>/', views.learn_bgp_instances_month_archive),
    path('LearnBGPInstances/<int:year>/<int:month>/<int:day>/', views.learn_bgp_instances_day_archive),
    path('LearnBGPInstances/nxos/', views.learn_bgp_instances_nxos_archive),
    path('LearnBGPInstances/<str:pyats_alias>/', views.learn_bgp_instances_alias_archive),
    path('LearnBGPRoutes/All/', views.learn_bgp_routes_all),
    path('LearnBGPRoutes/<int:year>/', views.learn_bgp_routes_year_archive),
    path('LearnBGPRoutes/<int:year>/<int:month>/', views.learn_bgp_routes_month_archive),
    path('LearnBGPRoutes/<int:year>/<int:month>/<int:day>/', views.learn_bgp_routes_day_archive),
    path('LearnBGPRoutes/nxos/', views.learn_bgp_routes_nxos_archive),
    path('LearnBGPRoutes/<str:pyats_alias>/', views.learn_bgp_routes_alias_archive),
    path('LearnBGPTables/All/', views.learn_bgp_tables_all),
    path('LearnBGPTables/<int:year>/', views.learn_bgp_tables_year_archive),
    path('LearnBGPTables/<int:year>/<int:month>/', views.learn_bgp_tables_month_archive),
    path('LearnBGPTables/<int:year>/<int:month>/<int:day>/', views.learn_bgp_tables_day_archive),
    path('LearnBGPTables/nxos/', views.learn_bgp_tables_nxos_archive),
    path('LearnBGPTables/<str:pyats_alias>/', views.learn_bgp_tables_alias_archive),        
    path('LearnConfig/All/', views.learn_config_all),
    path('LearnConfig/<int:year>/', views.learn_config_year_archive),
    path('LearnConfig/<int:year>/<int:month>/', views.learn_config_month_archive),
    path('LearnConfig/<int:year>/<int:month>/<int:day>/', views.learn_config_day_archive),
    path('LearnConfig/nxos/', views.learn_config_nxos_archive),
    path('LearnConfig/<str:pyats_alias>/', views.learn_config_alias_archive),
    path('LearnInterface/All/', views.learn_interface_all),
    path('LearnInterface/<int:year>/', views.learn_interface_year_archive),
    path('LearnInterface/<int:year>/<int:month>/', views.learn_interface_month_archive),
    path('LearnInterface/<int:year>/<int:month>/<int:day>/', views.learn_interface_day_archive),
    path('LearnInterface/nxos/', views.learn_interface_nxos_archive),
    path('LearnInterface/<str:pyats_alias>/', views.learn_interface_alias_archive),
    path('LearnPlatform/All/', views.learn_platform_all),
    path('LearnPlatform/<int:year>/', views.learn_platform_year_archive),
    path('LearnPlatform/<int:year>/<int:month>/', views.learn_platform_month_archive),
    path('LearnPlatform/<int:year>/<int:month>/<int:day>/', views.learn_platform_day_archive),
    path('LearnPlatform/nxos/', views.learn_platform_nxos_archive),
    path('LearnPlatform/<str:pyats_alias>/', views.learn_platform_alias_archive),
    path('LearnPlatformSlots/All/', views.learn_platform_slots_all),
    path('LearnPlatformSlots/<int:year>/', views.learn_platform_slots_year_archive),
    path('LearnPlatformSlots/<int:year>/<int:month>/', views.learn_platform_slots_month_archive),
    path('LearnPlatformSlots/<int:year>/<int:month>/<int:day>/', views.learn_platform_slots_day_archive),
    path('LearnPlatformSlots/nxos/', views.learn_platform_slots_nxos_archive),
    path('LearnPlatformSlots/<str:pyats_alias>/', views.learn_platform_slots_alias_archive),
    path('LearnPlatformVirtual/All/', views.learn_platform_virtual_all),
    path('LearnPlatformVirtual/<int:year>/', views.learn_platform_virtual_year_archive),
    path('LearnPlatformVirtual/<int:year>/<int:month>/', views.learn_platform_virtual_month_archive),
    path('LearnPlatformVirtual/<int:year>/<int:month>/<int:day>/', views.learn_platform_virtual_day_archive),
    path('LearnPlatformVirtual/nxos/', views.learn_platform_virtual_nxos_archive),
    path('LearnPlatformVirtual/<str:pyats_alias>/', views.learn_platform_virtual_alias_archive),        
    path('LearnVLAN/All/', views.learn_vlan_all),
    path('LearnVLAN/<int:year>/', views.learn_vlan_year_archive),
    path('LearnVLAN/<int:year>/<int:month>/', views.learn_vlan_month_archive),
    path('LearnVLAN/<int:year>/<int:month>/<int:day>/', views.learn_vlan_day_archive),
    path('LearnVLAN/nxos/', views.learn_vlan_nxos_archive),
    path('LearnVLAN/<str:pyats_alias>/', views.learn_vlan_alias_archive),
    path('LearnVRF/All/', views.learn_vrf_all),
    path('LearnVRF/<int:year>/', views.learn_vrf_year_archive),
    path('LearnVRF/<int:year>/<int:month>/', views.learn_vrf_month_archive),
    path('LearnVRF/<int:year>/<int:month>/<int:day>/', views.learn_vrf_day_archive),
    path('LearnVRF/nxos/', views.learn_vrf_nxos_archive),
    path('LearnVRF/<str:pyats_alias>/', views.learn_vrf_alias_archive),
    path('NMAP/All/', views.nmap_all),
    path('NMAP/<int:year>/', views.nmap_year_archive),
    path('NMAP/<int:year>/<int:month>/', views.nmap_month_archive),
    path('NMAP/<int:year>/<int:month>/<int:day>/', views.nmap_day_archive),
    path('NMAP/nxos/', views.nmap_nxos_archive),
    path('NMAP/<str:pyats_alias>/', views.nmap_alias_archive),  
    path('PSIRT/All/', views.psirt_all),
    path('PSIRT/<int:year>/', views.psirt_year_archive),
    path('PSIRT/<int:year>/<int:month>/', views.psirt_month_archive),
    path('PSIRT/<int:year>/<int:month>/<int:day>/', views.psirt_day_archive),
    path('PSIRT/nxos/', views.psirt_nxos_archive),
    path('PSIRT/<str:pyats_alias>/', views.psirt_alias_archive),    
    path('Recommended/All/', views.recommended_all),
    path('Recommended/<int:year>/', views.recommended_year_archive),
    path('Recommended/<int:year>/<int:month>/', views.recommended_month_archive),
    path('Recommended/<int:year>/<int:month>/<int:day>/', views.recommended_day_archive),
    path('Recommended/nxos/', views.recommended_nxos_archive),
    path('Recommended/<str:pyats_alias>/', views.recommended_alias_archive),
    path('Serial2Contract/All/', views.serial2contract_all),
    path('Serial2Contract/<int:year>/', views.serial2contract_year_archive),
    path('Serial2Contract/<int:year>/<int:month>/', views.serial2contract_month_archive),
    path('Serial2Contract/<int:year>/<int:month>/<int:day>/', views.serial2contract_day_archive),
    path('Serial2Contract/nxos/', views.serial2contract_nxos_archive),
    path('Serial2Contract/<str:pyats_alias>/', views.serial2contract_alias_archive),    
    path('ShowInventory/All/', views.show_inventory_all),
    path('ShowInventory/<int:year>/', views.show_inventory_year_archive),
    path('ShowInventory/<int:year>/<int:month>/', views.show_inventory_month_archive),
    path('ShowInventory/<int:year>/<int:month>/<int:day>/', views.show_inventory_day_archive),
    path('ShowInventory/nxos/', views.show_inventory_nxos_archive),
    path('ShowInventory/<str:pyats_alias>/', views.show_inventory_alias_archive),
    path('ShowIPInterfaceBrief/All/', views.show_ip_int_brief_all),
    path('ShowIPInterfaceBrief/<int:year>/', views.show_ip_int_brief_year_archive),
    path('ShowIPInterfaceBrief/<int:year>/<int:month>/', views.show_ip_int_brief_month_archive),
    path('ShowIPInterfaceBrief/<int:year>/<int:month>/<int:day>/', views.show_ip_int_brief_day_archive),
    path('ShowIPInterfaceBrief/nxos/', views.show_ip_int_brief_nxos_archive),
    path('ShowIPInterfaceBrief/<str:pyats_alias>/', views.show_ip_int_brief_alias_archive),    
    path('ShowVersion/All/', views.show_version_all),
    path('ShowVersion/<int:year>/', views.show_version_year_archive),
    path('ShowVersion/<int:year>/<int:month>/', views.show_version_month_archive),
    path('ShowVersion/<int:year>/<int:month>/<int:day>/', views.show_version_day_archive),
    path('ShowVersion/nxos/', views.show_version_nxos_archive),
    path('ShowVersion/<str:pyats_alias>/', views.show_version_alias_archive),
]