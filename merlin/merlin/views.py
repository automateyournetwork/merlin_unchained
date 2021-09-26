from django.shortcuts import render
from django.http import HttpResponse
from .models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion
import os

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

def learn_config_all(request):
    alias_list = LearnConfig.objects.all().values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.all().values_list('timestamp')
    config_json_list = LearnConfig.objects.all().values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_all.html', context)

def learn_config_year_archive(request, year):
    alias_list = LearnConfig.objects.filter(timestamp__year=year).values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.filter(timestamp__year=year).values_list('timestamp')
    config_json_list = LearnConfig.objects.filter(timestamp__year=year).values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'year': year,'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_year_archive.html', context)

def learn_config_month_archive(request, year, month):
    alias_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month).values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month).values_list('timestamp')
    config_json_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month).values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'year': year, 'month': month, 'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_month_archive.html', context)

def learn_config_day_archive(request, year, month, day):
    alias_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day).values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day).values_list('timestamp')
    config_json_list = LearnConfig.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day).values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'year': year, 'month': month,'day': day, 'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_day_archive.html', context)

def learn_config_nxos_archive(request):
    alias_list = LearnConfig.objects.filter(os='nxos').values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.filter(os='nxos').values_list('timestamp')
    config_json_list = LearnConfig.objects.filter(os='nxos').values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'os': os,'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_nxos_archive.html', context)

def learn_config_alias_archive(request, pyats_alias):
    interface_list = LearnInterface.objects.filter()
    alias_list = LearnConfig.objects.filter(pyats_alias=pyats_alias).values_list('pyats_alias')
    timestamp_list = LearnConfig.objects.filter(pyats_alias=pyats_alias).values_list('timestamp')
    config_json_list = LearnConfig.objects.filter(pyats_alias=pyats_alias).values_list('config')
    inner_json = []
    for config in config_json_list:
        for timestamp in timestamp_list:
            for inner_config in config:
                for key,value in inner_config.items():
                    hit = { key: value }
                    inner_json.append(hit)
    context = {'pyats_alias': pyats_alias,'alias_list': alias_list, 'inner_json': inner_json,'timestamp_list': timestamp_list}
    return render(request, 'HTML/LearnConfig/learn_config_alias_archive.html', context)

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

def learn_platform_all(request):
    platform_list = LearnPlatform.objects.all()
    context = {'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_all.html', context)

def learn_platform_year_archive(request, year):
    platform_list = LearnPlatform.objects.filter(timestamp__year=year)
    context = {'year': year, 'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_year_archive.html', context)

def learn_platform_month_archive(request, year, month):
    platform_list = LearnPlatform.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_month_archive.html', context)

def learn_platform_day_archive(request, year, month, day):
    platform_list = LearnPlatform.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_day_archive.html', context)

def learn_platform_nxos_archive(request):
    platform_list = LearnPlatform.objects.filter(os='nxos')
    context = {'os': os, 'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_nxos_archive.html', context)

def learn_platform_alias_archive(request, pyats_alias):
    platform_list = LearnPlatform.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'platform_list': platform_list}
    return render(request, 'HTML/LearnPlatform/learn_platform_alias_archive.html', context)

def learn_platform_slots_all(request):
    platform_slots_list = LearnPlatformSlots.objects.all()
    context = {'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_all.html', context)

def learn_platform_slots_year_archive(request, year):
    platform_slots_list = LearnPlatformSlots.objects.filter(timestamp__year=year)
    context = {'year': year, 'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_year_archive.html', context)

def learn_platform_slots_month_archive(request, year, month):
    platform_slots_list = LearnPlatformSlots.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_month_archive.html', context)

def learn_platform_slots_day_archive(request, year, month, day):
    platform_slots_list = LearnPlatformSlots.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_day_archive.html', context)

def learn_platform_slots_nxos_archive(request):
    platform_slots_list = LearnPlatformSlots.objects.filter(os='nxos')
    context = {'os': os, 'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_nxos_archive.html', context)

def learn_platform_slots_alias_archive(request, pyats_alias):
    platform_slots_list = LearnPlatformSlots.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'platform_slots_list': platform_slots_list}
    return render(request, 'HTML/LearnPlatformSlots/learn_platform_slots_alias_archive.html', context)

def learn_platform_virtual_all(request):
    platform_virtual_list = LearnPlatformVirtual.objects.all()
    context = {'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_all.html', context)

def learn_platform_virtual_year_archive(request, year):
    platform_virtual_list = LearnPlatformVirtual.objects.filter(timestamp__year=year)
    context = {'year': year, 'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_year_archive.html', context)

def learn_platform_virtual_month_archive(request, year, month):
    platform_virtual_list = LearnPlatformVirtual.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_month_archive.html', context)

def learn_platform_virtual_day_archive(request, year, month, day):
    platform_virtual_list = LearnPlatformVirtual.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_day_archive.html', context)

def learn_platform_virtual_nxos_archive(request):
    platform_virtual_list = LearnPlatformVirtual.objects.filter(os='nxos')
    context = {'os': os, 'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_nxos_archive.html', context)

def learn_platform_virtual_alias_archive(request, pyats_alias):
    platform_virtual_list = LearnPlatformVirtual.objects.filter(pyats_alias=pyats_alias)
    context = {'pyats_alias': pyats_alias, 'platform_virtual_list': platform_virtual_list}
    return render(request, 'HTML/LearnPlatformVirtual/learn_platform_virtual_alias_archive.html', context)        

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