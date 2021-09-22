from django.shortcuts import render
from django.http import HttpResponse
from .models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion
import os
import csv

# HTML VIEWS #
def devices_all(request):
    device_list = Devices.objects.all()
    context = {'device_list': device_list}
    return render(request, 'HTML/Devices/devices_all.html', context)

def devices_year_archive(request, year):
    device_list = Devices.objects.filter(timestamp__year=year)
    context = {'year': year, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_year_archive.html', context)

def devices_month_archive(request, year, month):
    device_list = Devices.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_month_archive.html', context)

def devices_day_archive(request, year, month, day):
    device_list = Devices.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_day_archive.html', context)

def devices_hostname_archive(request, hostname):
    device_list = Devices.objects.filter(hostname=hostname)
    context = {'hostname': hostname, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_hostname_archive.html', context)

def devices_alias_archive(request, alias):
    device_list = Devices.objects.filter(alias=alias)
    context = {'alias': alias, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_alias_archive.html', context)

def devices_os_archive(request, os):
    device_list = Devices.objects.filter(os=os)
    context = {'os': os, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_os_archive.html', context)

def devices_device_type_archive(request, device_type):
    device_list = Devices.objects.filter(device_type=device_type)
    context = {'device_type': device_type, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_device_type_archive.html', context)

def devices_username_archive(request, username):
    device_list = Devices.objects.filter(username=username)
    context = {'username': username, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_username_archive.html', context)

def devices_protocol_archive(request, protocol):
    device_list = Devices.objects.filter(protocol=protocol)
    context = {'protocol': protocol, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_protocol_archive.html', context)

def devices_protocol_archive(request, protocol):
    device_list = Devices.objects.filter(protocol=protocol)
    context = {'protocol': protocol, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_protocol_archive.html', context)

def devices_ip_address_archive(request, ip_address):
    device_list = Devices.objects.filter(ip_address=ip_address)
    context = {'ip_address': ip_address, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_ip_address_archive.html', context)

def devices_port_archive(request, port):
    device_list = Devices.objects.filter(port=port)
    context = {'port': port, 'device_list': device_list}
    return render(request, 'HTML/Devices/devices_port_address_archive.html', context)

def learn_acl_all(request):
    acl_list = LearnACL.objects.all()
    context = {'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_all.html', context)

def learn_acl_year_archive(request, year):
    acl_list = LearnACL.objects.filter(timestamp__year=year)
    context = {'year': year, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_year_archive.html', context)

def learn_acl_month_archive(request, year, month):
    acl_list = LearnACL.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_month_archive.html', context)

def learn_acl_day_archive(request, year, month, day):
    acl_list = LearnACL.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_day_archive.html', context)

def learn_acl_nxos_archive(request):
    acl_list = LearnACL.objects.filter(os='nxos')
    context = {'os': os, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_nxos_archive.html', context)

def learn_acl_alias_archive(request, pyats_alias):
    acl_list = LearnACL.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_alias_archive.html', context)

def learn_arp_all(request):
    arp_list = LearnARP.objects.all()
    context = {'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_all.html', context)

def learn_arp_year_archive(request, year):
    arp_list = LearnARP.objects.filter(timestamp__year=year)
    context = {'year': year, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_year_archive.html', context)

def learn_arp_month_archive(request, year, month):
    arp_list = LearnARP.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_month_archive.html', context)

def learn_arp_day_archive(request, year, month, day):
    arp_list = LearnARP.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_day_archive.html', context)

def learn_arp_nxos_archive(request):
    arp_list = LearnARP.objects.filter(os='nxos')
    context = {'os': os, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_nxos_archive.html', context)

def learn_arp_alias_archive(request, pyats_alias):
    arp_list = LearnARP.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_alias_archive.html', context)

def learn_arp_statistics_all(request):
    arp_statistics_list = LearnARPStatistics.objects.all()
    context = {'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_all.html', context)

def learn_arp_statistics_year_archive(request, year):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year)
    context = {'year': year, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_year_archive.html', context)

def learn_arp_statistics_month_archive(request, year, month):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_month_archive.html', context)

def learn_arp_statistics_day_archive(request, year, month, day):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_day_archive.html', context)

def learn_arp_statistics_nxos_archive(request):
    arp_statistics_list = LearnARPStatistics.objects.filter(os='nxos')
    context = {'os': os, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_nxos_archive.html', context)

def learn_arp_statistics_alias_archive(request, pyats_alias):
    arp_statistics_list = LearnARPStatistics.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_alias_archive.html', context)    

def learn_bgp_instances_all(request):
    bgp_instance_list = LearnBGPInstances.objects.all()
    context = {'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_all.html', context)

def learn_bgp_instances_year_archive(request, year):
    bgp_instance_list = LearnBGPInstances.objects.filter(timestamp__year=year)
    context = {'year': year, 'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_year_archive.html', context)

def learn_bgp_instances_month_archive(request, year, month):
    bgp_instance_list = LearnBGPInstances.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_month_archive.html', context)

def learn_bgp_instances_day_archive(request, year, month, day):
    bgp_instance_list = LearnBGPInstances.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_day_archive.html', context)

def learn_bgp_instances_nxos_archive(request):
    bgp_instance_list = LearnBGPInstances.objects.filter(os='nxos')
    context = {'os': os, 'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_nxos_archive.html', context)

def learn_bgp_instances_alias_archive(request, pyats_alias):
    bgp_instance_list = LearnBGPInstances.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'bgp_instance_list': bgp_instance_list}
    return render(request, 'HTML/LearnBGPInstances/learn_bgp_instances_alias_archive.html', context)

def learn_bgp_routes_all(request):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.all()
    context = {'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_all.html', context)

def learn_bgp_routes_year_archive(request, year):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(timestamp__year=year)
    context = {'year': year, 'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_year_archive.html', context)

def learn_bgp_routes_month_archive(request, year, month):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_month_archive.html', context)

def learn_bgp_routes_day_archive(request, year, month, day):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_day_archive.html', context)

def learn_bgp_routes_nxos_archive(request):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(os='nxos')
    context = {'os': os, 'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_nxos_archive.html', context)

def learn_bgp_routes_alias_archive(request, pyats_alias):
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'bgp_route_list': bgp_route_list}
    return render(request, 'HTML/LearnBGPRoutes/learn_bgp_routes_alias_archive.html', context)

def learn_bgp_tables_all(request):
    bgp_tables_list = LearnBGPTables.objects.all()
    context = {'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_all.html', context)

def learn_bgp_tables_year_archive(request, year):
    bgp_tables_list = LearnBGPTables.objects.filter(timestamp__year=year)
    context = {'year': year, 'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_year_archive.html', context)

def learn_bgp_tables_month_archive(request, year, month):
    bgp_tables_list = LearnBGPTables.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_month_archive.html', context)

def learn_bgp_tables_day_archive(request, year, month, day):
    bgp_tables_list = LearnBGPTables.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_day_archive.html', context)

def learn_bgp_tables_nxos_archive(request):
    bgp_tables_list = LearnBGPTables.objects.filter(os='nxos')
    context = {'os': os, 'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_nxos_archive.html', context)

def learn_bgp_tables_alias_archive(request, pyats_alias):
    bgp_tables_list = LearnBGPTables.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'bgp_tables_list': bgp_tables_list}
    return render(request, 'HTML/LearnBGPTables/learn_bgp_tables_alias_archive.html', context)    

def learn_interface_all(request):
    interface_list = LearnInterface.objects.all()
    context = {'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_all.html', context)

def learn_interface_year_archive(request, year):
    interface_list = LearnInterface.objects.filter(timestamp__year=year)
    context = {'year': year, 'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_year_archive.html', context)

def learn_interface_month_archive(request, year, month):
    interface_list = LearnInterface.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_month_archive.html', context)

def learn_interface_day_archive(request, year, month, day):
    interface_list = LearnInterface.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_day_archive.html', context)

def learn_interface_nxos_archive(request):
    interface_list = LearnInterface.objects.filter(os='nxos')
    context = {'os': os, 'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_nxos_archive.html', context)

def learn_interface_alias_archive(request, pyats_alias):
    interface_list = LearnInterface.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'interface_list': interface_list}
    return render(request, 'HTML/LearnInterface/learn_interface_alias_archive.html', context)

def learn_vlan_all(request):
    v_list = LearnVLAN.objects.all()
    context = {'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_all.html', context)

def learn_vlan_year_archive(request, year):
    v_list = LearnVLAN.objects.filter(timestamp__year=year)
    context = {'year': year, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_year_archive.html', context)

def learn_vlan_month_archive(request, year, month):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_month_archive.html', context)

def learn_vlan_day_archive(request, year, month, day):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_day_archive.html', context)

def learn_vlan_nxos_archive(request):
    v_list = LearnVLAN.objects.filter(os='nxos')
    context = {'os': os, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_nxos_archive.html', context)

def learn_vlan_alias_archive(request, pyats_alias):
    v_list = LearnVLAN.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_alias_archive.html', context)

def learn_vrf_all(request):
    v_list = LearnVRF.objects.all()
    context = {'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_all.html', context)

def learn_vrf_year_archive(request, year):
    v_list = LearnVRF.objects.filter(timestamp__year=year)
    context = {'year': year, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_year_archive.html', context)

def learn_vrf_month_archive(request, year, month):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_month_archive.html', context)

def learn_vrf_day_archive(request, year, month, day):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_day_archive.html', context)

def learn_vrf_nxos_archive(request):
    v_list = LearnVRF.objects.filter(os='nxos')
    context = {'os': os, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_nxos_archive.html', context)

def learn_vrf_alias_archive(request,pyats_alias):
    v_list = LearnVRF.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_alias_archive.html', context)    

def show_inventory_all(request):
    inventory_list = ShowInventory.objects.all()
    context = {'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_all.html', context)

def show_inventory_year_archive(request, year):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year)
    context = {'year': year, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_year_archive.html', context)

def show_inventory_month_archive(request, year, month):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_month_archive.html', context)

def show_inventory_day_archive(request, year, month, day):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_day_archive.html', context)

def show_inventory_nxos_archive(request):
    inventory_list = ShowInventory.objects.filter(os='nxos')
    context = {'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_nxos_archive.html', context)

def show_inventory_alias_archive(request, pyats_alias):
    inventory_list = ShowInventory.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_alias_archive.html', context)

def show_ip_int_brief_all(request):
    interface_list = ShowIPIntBrief.objects.all()
    context = {'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_all.html', context)

def show_ip_int_brief_year_archive(request, year):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year)
    context = {'year': year, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_year_archive.html', context)

def show_ip_int_brief_month_archive(request, year, month):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_month_archive.html', context)

def show_ip_int_brief_day_archive(request, year, month, day):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_day_archive.html', context)

def show_ip_int_brief_nxos_archive(request):
    interface_list = ShowIPIntBrief.objects.filter(os='nxos')
    context = {'os': os, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_nxos_archive.html', context)

def show_ip_int_brief_alias_archive(request, pyats_alias):
    interface_list = ShowIPIntBrief.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_alias_archive.html', context)

def show_version_all(request):
    v_list = ShowVersion.objects.all()
    context = {'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_all.html', context)

def show_version_year_archive(request, year):
    v_list = ShowVersion.objects.filter(timestamp__year=year)
    context = {'year': year, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_year_archive.html', context)

def show_version_month_archive(request, year, month):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_month_archive.html', context)

def show_version_day_archive(request, year, month, day):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_day_archive.html', context)

def show_version_nxos_archive(request):
    v_list = ShowVersion.objects.filter(os='nxos')
    context = {'os': os, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_nxos_archive.html', context)

def show_version_alias_archive(request, pyats_alias):
    v_list = ShowVersion.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_alias_archive.html', context)

# CSV VIEWS
def csv_page(request):
    return render(request, 'CSV/csv.html')    

def all_csv_download(request):
    return render(request, 'CSV/csv.html')  

def devices_csv(request):
    return render(request, 'CSV/Devices/devices_csv.html')

def devices_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_devices.csv'
    writer = csv.writer(response)
    writer.writerow(['Hostname','Alias','Device Type','Operating System','Username','Password','Protocol','IP Address','Port','Connection Timeout','Timestamp'])
    devices = Devices.objects.all().values_list('hostname','alias','device_type','os','username','password','protocol','ip_address','port','connection_timeout','timestamp')
    for device in devices:
        writer.writerow(device)
    return response

def learn_acl_csv(request):
    return render(request, 'CSV/LearnACL/learn_acl_csv.html')

def learn_acl_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_acl_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Access Control List','Access Control Entry','Permission','Logging','Source Network','Destination Network','Layer 3 Protocol','Layer 4 Protocol','Operator','Port','Timestamp'])
    acls = LearnACL.objects.all().values_list('pyats_alias','acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')
    for acl in acls:
        writer.writerow(acl)
    return response

def learn_acl_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_acl_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Access Control List','Access Control Entry','Permission','Logging','Source Network','Destination Network','Layer 3 Protocol','Layer 4 Protocol','Operator','Port','Timestamp'])
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acls = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')
    for acl in acls:
        writer.writerow(acl)
    return response

def learn_arp_csv(request):
    return render(request, 'CSV/LearnARP/learn_arp_csv.html')

def learn_arp_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Neighbor IP','Neighbor MAC','Origin','Local Proxy','Proxy','Timestamp'])
    interfaces = LearnARP.objects.all().values_list('pyats_alias', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_arp_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Neighbor IP','Neighbor MAC','Origin','Local Proxy','Proxy','Timestamp'])
    latest_timestamp = LearnARP.objects.latest('timestamp')
    interfaces = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_arp_statistics_csv(request):
    return render(request, 'CSV/LearnARP/learn_arp_csv.html')

def learn_arp_statistics_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_statistics_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Total Entries','Input Drops','Input Replies','Input Requests','Incomplete Requests','Output Replies','Output Requests','Timestamp'])
    statistics = LearnARPStatistics.objects.all().values_list('pyats_alias','entries_total','in_drops','in_replies_pkts','in_requests_pkts','incomplete_total','out_replies_pkts','out_requests_pkts','timestamp')
    for stat in statistics:
        writer.writerow(stat)
    return response

def learn_arp_statistics_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_statistics_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Total Entries','Input Drops','Input Replies','Input Requests','Incomplete Requests','Output Replies','Output Requests','Timestamp'])
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    statistics = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','entries_total','in_drops','in_replies_pkts','in_requests_pkts','incomplete_total','out_replies_pkts','out_requests_pkts','timestamp')
    for stat in statistics:
        writer.writerow(statistics)
    return response

def learn_bgp_instances_csv(request):
    return render(request, 'CSV/LearnBGPInstances/learn_bgp_instances_csv.html')

def learn_bgp_instances_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_instances_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','BGP ID','Protocol State','Next Hop Trigger Critial Delay','Next Hop Trigger Non-Critical Delay','Next Hop Trigger Enabled','VRF','Router ID','Cluster ID','Confederation ID','Neighbor','Version','Hold Time','Keep Alive Interval','Local AS','Remote AS','Neighbor Receive Bytes Queue','Neighbor Receive Capability','Neighbor Receive Keep Alive','Neighbor Receive Notifications','Neighbor Receive Opens','Neighbor Receive Route Refresh','Neighbor Receive Total','Neighbor Receive Total Bytes','Neighbr Receive Updates','Neighbor Sent Bytes Queue','Neighbor Sent Capability','Neighbor Sent Keep Alive','Neighbor Sent Notifications','Neighbor Sent Opens','Neighbor Sent Route Refresh','Neighbor Sent Total','Neighbor Sent Total Bytes','Neighbr Sent Updates','Last Reset','Reset Reason','Timestamp'])
    instances = LearnBGPInstances.objects.all().values_list('pyats_alias','instance','bgp_id','protocol_state','nexthop_trigger_delay_critical','nexthop_trigger_delay_noncritical','nexthop_trigger_enabled','vrf','router_id','cluster_id','confederation_id','neighbor','version','hold_time','keep_alive_interval','local_as','remote_as','neighbor_counters_received_bytes_in_queue','neighbor_counters_received_capability','neighbor_counters_received_keepalives','neighbor_counters_received_notifications','neighbor_counters_received_opens','neighbor_counters_received_route_refresh','neighbor_counters_received_total','neighbor_counters_received_total_bytes','neighbor_counters_received_updates','neighbor_counters_sent_bytes_in_queue','neighbor_counters_sent_capability','neighbor_counters_sent_keepalives','neighbor_counters_sent_notifications','neighbor_counters_sent_opens','neighbor_counters_sent_route_refresh','neighbor_counters_sent_total','neighbor_counters_sent_total_bytes','neighbor_counters_sent_updates','last_reset','reset_reason','timestamp')
    for instance in instances:
        writer.writerow(instance)
    return response

def learn_bgp_instances_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_instances_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','BGP ID','Protocol State','Next Hop Trigger Critial Delay','Next Hop Trigger Non-Critical Delay','VRF','Router ID','Cluster ID','Confederation ID','Neighbor','Version','Hold Time','Keep Alive Interval','Local AS','Remote AS','Neighbor Receive Bytes Queue','Neighbor Receive Capability','Neighbor Receive Keep Alive','Neighbor Receive Notifications','Neighbor Receive Opens','Neighbor Receive Route Refresh','Neighbor Receive Total','Neighbor Receive Total Bytes','Neighbr Receive Updates','Neighbor Sent Bytes Queue','Neighbor Sent Capability','Neighbor Sent Keep Alive','Neighbor Sent Notifications','Neighbor Sent Opens','Neighbor Sent Route Refresh','Neighbor Sent Total','Neighbor Sent Total Bytes','Neighbr Sent Updates','Last Reset','Reset Reason','Timestamp'])
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','instance','bgp_id','protocol_state','nexthop_trigger_delay_critical','nexthop_trigger_delay_noncritical','nexthop_trigger_enabled','vrf','router_id','cluster_id','confederation_id','neighbor','version','hold_time','keep_alive_interval','local_as','remote_as','neighbor_counters_received_bytes_in_queue','neighbor_counters_received_capability','neighbor_counters_received_keepalives','neighbor_counters_received_notifications','neighbor_counters_received_opens','neighbor_counters_received_route_refresh','neighbor_counters_received_total','neighbor_counters_received_total_bytes','neighbor_counters_received_updates','neighbor_counters_sent_bytes_in_queue','neighbor_counters_sent_capability','neighbor_counters_sent_keepalives','neighbor_counters_sent_notifications','neighbor_counters_sent_opens','neighbor_counters_sent_route_refresh','neighbor_counters_sent_total','neighbor_counters_sent_total_bytes','neighbor_counters_sent_updates','last_reset','reset_reason','timestamp')
    for instance in instances:
        writer.writerow(instance)
    return response

def learn_bgp_routes_csv(request):
    return render(request, 'CSV/LearnBGPRoutes/learn_bgp_routes_csv.html')

def learn_bgp_routes_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_routes_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','VRF','Neighbor','Advertised','Routes','Remote AS','Timestamp'])
    routes = LearnBGPRoutesPerPeer.objects.all().values_list('pyats_alias','instance','vrf','neighbor','advertised','routes','remote_as','timestamp')
    for route in routes:
        writer.writerow(route)
    return response

def learn_bgp_routes_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_routes_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','VRF','Neighbor','Advertised','Routes','Remote AS','Timestamp'])
    latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    routes = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','instance','vrf','neighbor','advertised','routes','remote_as','timestamp')
    for route in routes:
        writer.writerow(route)
    return response

def learn_bgp_tables_csv(request):
    return render(request, 'CSV/LearnBGPTables/learn_bgp_tables_csv.html')

def learn_bgp_tables_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_tables_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','VRF','Table Version','Prefix','Index','Local Preference','Next Hop','Origin Code','Status Code','Weight','Timestamp'])
    tables = LearnBGPTables.objects.all().values_list('pyats_alias','instance','vrf','table_version','prefix','index','localpref','next_hop','origin_code','status_code','weight','timestamp')
    for table in tables:
        writer.writerow(table)
    return response

def learn_bgp_tables_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_bgp_tables_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Instance','VRF','Table Version','Prefix','Index','Local Preference','Next Hop','Origin Code','Status Code','Weight','Timestamp'])
    latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    tables = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','instance','vrf','table_version','prefix','index','localpref','next_hop','origin_code','status_code','weight','timestamp')
    for table in tables:
        writer.writerow(table)
    return response        

def learn_interface_csv(request):
    return render(request, 'CSV/LearnInterface/learn_interface_csv.html')

def learn_interface_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_interface_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Description','Enabled','Status','Access VLAN','Native VLAN','Switchport','Switchport Mode','Interface Type','Bandwidth','Auto Negotiate','Speed','Duplex','MTU','MAC Address','Physical Address','Medium','Delay','Encapsulation','Flow Control Receive','Flow Control Send','Port Channel','Port Channel Member Interfaces','Port Channel Member','Last Change','Input Broadcast','Input CRC Errors','Input MAC Pause Frames','Input Multicast','Input Octets','Input Unicast','Input Unknown','Input Total','Output Broadcast','Output Discard','Output Errors','Output MAC Pause Frames','Output Multicast','Output Unicast','Output Total','Last Clear','Input Rate','Load Interval','Output Rate','Timestamp'])
    interfaces = LearnInterface.objects.all().values_list('pyats_alias','interface','description','enabled','status','access_vlan','native_vlan','switchport','switchport_mode','interface_type','bandwidth','auto_negotiate','speed','duplex','mtu','mac_address','physical_address','ip_address','medium','delay','encapsulation','flow_control_receive','flow_control_send','port_channel','port_channel_member_interfaces','port_channel_member','last_change','input_broadcast','input_crc_errors','input_errors','input_mac_pause_frames','input_multicast','input_octets','input_unicast','input_unknown','input_total','output_broadcast','output_discard','output_errors','output_mac_pause_frames','output_multicast','output_unicast','output_total','last_clear','input_rate','load_interval','output_rate','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_interface_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_interface_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Description','Enabled','Status','Access VLAN','Native VLAN','Switchport','Switchport Mode','Interface Type','Bandwidth','Auto Negotiate','Speed','Duplex','MTU','MAC Address','Physical Address','Medium','Delay','Encapsulation','Flow Control Receive','Flow Control Send','Port Channel','Port Channel Member Interfaces','Port Channel Member','Last Change','Input Broadcast','Input CRC Errors','Input MAC Pause Frames','Input Multicast','Input Octets','Input Unicast','Input Unknown','Input Total','Output Broadcast','Output Discard','Output Errors','Output MAC Pause Frames','Output Multicast','Output Unicast','Output Total','Last Clear','Input Rate','Load Interval','Output Rate','Timestamp'])
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interfaces = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','interface','description','enabled','status','access_vlan','native_vlan','switchport','switchport_mode','interface_type','bandwidth','auto_negotiate','speed','duplex','mtu','mac_address','physical_address','ip_address','medium','delay','encapsulation','flow_control_receive','flow_control_send','port_channel','port_channel_member_interfaces','port_channel_member','last_change','input_broadcast','input_crc_errors','input_errors','input_mac_pause_frames','input_multicast','input_octets','input_unicast','input_unknown','input_total','output_broadcast','output_discard','output_errors','output_mac_pause_frames','output_multicast','output_unicast','output_total','last_clear','input_rate','load_interval','output_rate','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_vlan_csv(request):
    return render(request, 'CSV/LearnVLAN/learn_vlan_csv.html')

def learn_vlan_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vlan_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VLAN','Interfaces','Mode','Name','Shutdown','State','Timestamp'])
    vlans = LearnVLAN.objects.all().values_list('pyats_alias','vlan','interfaces','mode','name','shutdown','state','timestamp')
    for vlan in vlans:
        writer.writerow(vlan)
    return response

def learn_vlan_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vlan_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VLAN','Interfaces','Mode','Name','Shutdown','State','Timestamp'])
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','vlan','interfaces','mode','name','shutdown','state','timestamp')
    for vlan in vlans:
        writer.writerow(vlan)
    return response

def learn_vrf_csv(request):
    return render(request, 'CSV/LearnVRF/learn_vrf_csv.html')    

def learn_vrf_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vrf_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VRF','Address Family IPv4','Address Family IPv6','Route Distinguisher','Timestamp'])
    vrfs = LearnVRF.objects.all().values_list('pyats_alias','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')
    for vrf in vrfs:
        writer.writerow(vrf)
    return response

def learn_vrf_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vrf_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VRF','Address Family IPv4','Address Family IPv6','Route Distinguisher','Timestamp'])
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')
    for vrf in vrfs:
        writer.writerow(vrf)
    return response

def show_inventory_csv(request):
    return render(request, 'CSV/ShowInventory/show_inventory_csv.html')    

def show_inventory_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_inventory_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Part','Description','Part ID','Serial Number','Timestamp'])
    inventory = ShowInventory.objects.all().values_list('pyats_alias','part','description','pid','serial_number','timestamp')
    for part in inventory:
        writer.writerow(part)
    return response

def show_inventory_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_inventory_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Part','Description','Part ID','Serial Number','Timestamp'])
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','part','description','pid','serial_number','timestamp')
    for part in inventory:
        writer.writerow(part)
    return response

def show_ip_int_brief_csv(request):
    return render(request, 'CSV/ShowIPInterfaceBrief/show_ip_int_brief.html')    

def show_ip_int_brief_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_ip_interface_brief_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Interface Status','IP Address','Timestamp'])
    interfaces = ShowIPIntBrief.objects.all().values_list('pyats_alias','interface','interface_status','ip_address','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def show_ip_int_brief_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_ip_interface_brief_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Interface Status','IP Address','Timestamp'])
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interfaces = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','interface','interface_status','ip_address','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def show_version_csv(request):
    return render(request, 'CSV/ShowVersion/show_version_csv.html')    

def show_version_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_version_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Bootflash','Chassis','CPU','Device Name','Memory','Model','Processor Board ID','RP','Slots','Days Up','Hours Up','Minutes Up','Seconds Up','Name','OS','Last Reload Reason','System Compile Time','Image File','Version','Chassis Serial Number','Compiled By','Current Config Register','Image ID','Label','License Leven','License Type','Non Volative Memory','Physical Memory','Next Reload License Level','Platform','Processor Type','Return to ROM by','Router Type','Uptime','Uptime this CP','Version (Short)','XE Version','Timestamp'])
    versions = ShowVersion.objects.all().values_list('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')
    for version in versions:
        writer.writerow(version)
    return response

def show_version_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_version_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Bootflash','Chassis','CPU','Device Name','Memory','Model','Processor Board ID','RP','Slots','Days Up','Hours Up','Minutes Up','Seconds Up','Name','OS','Last Reload Reason','System Compile Time','Image File','Version','Chassis Serial Number','Compiled By','Current Config Register','Image ID','Label','License Leven','License Type','Non Volative Memory','Physical Memory','Next Reload License Level','Platform','Processor Type','Return to ROM by','Router Type','Uptime','Uptime this CP','Version (Short)','XE Version','Timestamp'])
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    versions = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')
    for version in versions:
        writer.writerow(version)
    return response

# Latest
def latest(request):
    return render(request, 'Latest/latest.html')

def all_latest(request):
    acl_latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=acl_latest_timestamp.timestamp)
    arp_latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=arp_latest_timestamp.timestamp)
    arp_statistics_latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp=arp_statistics_latest_timestamp.timestamp)
    bgp_instances_latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    bgp_instances_list = LearnBGPInstances.objects.filter(timestamp=bgp_instances_latest_timestamp.timestamp)
    bgp_routes_latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    bgp_routes_list = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_routes_latest_timestamp.timestamp)
    bgp_tables_latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    bgp_tables_list = LearnBGPTables.objects.filter(timestamp=bgp_tables_latest_timestamp.timestamp)
    interface_latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=interface_latest_timestamp.timestamp)
    platform_latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=platform_latest_timestamp.timestamp)
    platform_slots_latest_timestamp = LearnPlatformSlots.objects.latest('timestamp')
    platform_slots_list = LearnPlatformSlots.objects.filter(timestamp=platform_slots_latest_timestamp.timestamp)
    platform_virtual_latest_timestamp = LearnPlatformVirtual.objects.latest('timestamp')
    platform_virtual_list = LearnPlatformVirtual.objects.filter(timestamp=platform_virtual_latest_timestamp.timestamp)
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlan_list = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp)
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrf_list = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp)
    inventory_latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=inventory_latest_timestamp.timestamp)
    ip_int_brief_latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    ip_int_brief_list = ShowIPIntBrief.objects.filter(timestamp=ip_int_brief_latest_timestamp.timestamp)    
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp)       
    context = {'acl_list': acl_list, 'arp_list': arp_list, 'arp_statistics_list': arp_statistics_list, 'bgp_instances_list': bgp_instances_list, 'bgp_routes_list': bgp_routes_list, 'bgp_tables_list': bgp_tables_list, 'interface_list': interface_list, 'platform_list': platform_list, 'platform_slots_list': platform_slots_list, 'platform_virtual_list': platform_virtual_list, 'vlan_list': vlan_list,'vrf_list': vrf_list,'version_list': version_list,'ip_int_brief_list': ip_int_brief_list,'inventory_list': inventory_list}
    return render(request, 'Latest/All/all_latest.html', context)

def learn_acl_latest(request):
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'acl_list': acl_list}
    return render(request, 'Latest/LearnACL/learn_acl_latest.html', context)

def learn_arp_latest(request):
    latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'arp_list': arp_list}
    return render(request, 'Latest/LearnARP/learn_arp_latest.html', context)

def learn_arp_statistics_latest(request):
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'arp_statistics_list': arp_statistics_list}
    return render(request, 'Latest/LearnARPStatistics/learn_arp_statistics_latest.html', context)    

def learn_bgp_instances_latest(request):
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    bgp_instances_list = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'bgp_instances_list': bgp_instances_list}
    return render(request, 'Latest/LearnBGP/learn_bgp_instances_latest.html', context)

def learn_bgp_routes_latest(request):
    latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    bgp_routes_list = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'bgp_routes_list': bgp_routes_list}
    return render(request, 'Latest/LearnBGP/learn_bgp_routes_latest.html', context)

def learn_bgp_tables_latest(request):
    latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    bgp_tables_list = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'bgp_tables_list': bgp_tables_list}
    return render(request, 'Latest/LearnBGP/learn_bgp_tables_latest.html', context)

def learn_interface_latest(request):
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'interface_list': interface_list}
    return render(request, 'Latest/LearnInterface/learn_interface_latest.html', context)

def learn_platform_latest(request):
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'platform_list': platform_list}
    return render(request, 'Latest/LearnPlatform/learn_platform_latest.html', context)

def learn_platform_slots_latest(request):
    latest_timestamp = LearnPlatformSlots.objects.latest('timestamp')
    platform_slots_list = LearnPlatformSlots.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'platform_slots_list': platform_slots_list}
    return render(request, 'Latest/LearnPlatform/learn_platform_slots_latest.html', context)

def learn_platform_virtual_latest(request):
    latest_timestamp = LearnPlatformVirtual.objects.latest('timestamp')
    platform_virtual_list = LearnPlatformVirtual.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'platform_virtual_list': platform_virtual_list}
    return render(request, 'Latest/LearnPlatform/learn_platform_virtual_latest.html', context)        

def learn_vlan_latest(request):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    v_list = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'vlan_list': v_list}
    return render(request, 'Latest/LearnVLAN/learn_vlan_latest.html', context)

def learn_vrf_latest(request):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    v_list = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'vrf_list': v_list}
    return render(request, 'Latest/LearnVRF/learn_vrf_latest.html', context)

def show_inventory_latest(request):
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'inventory_list': inventory_list}
    return render(request, 'Latest/ShowInventory/show_inventory_latest.html', context)

def show_ip_int_brief_latest(request):
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interface_list = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'interface_list': interface_list}
    return render(request, 'Latest/ShowIPInterfaceBrief/show_ip_int_brief_latest.html', context)

def show_version_latest(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    v_list = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'version_list': v_list}
    return render(request, 'Latest/ShowVersion/show_version_latest.html', context)