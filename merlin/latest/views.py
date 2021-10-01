from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, RecommendedRelease, ShowInventory, ShowIPIntBrief, ShowVersion

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
    config_latest_timestamp = LearnConfig.objects.latest('timestamp')
    config_list = LearnConfig.objects.filter(timestamp=config_latest_timestamp.timestamp)    
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
    recommended_latest_timestamp = RecommendedRelease.objects.latest('timestamp')
    recommended_list = RecommendedRelease.objects.filter(timestamp=recommended_latest_timestamp.timestamp)    
    inventory_latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=inventory_latest_timestamp.timestamp)
    ip_int_brief_latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    ip_int_brief_list = ShowIPIntBrief.objects.filter(timestamp=ip_int_brief_latest_timestamp.timestamp)    
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp)       
    context = {'acl_list': acl_list, 'arp_list': arp_list, 'arp_statistics_list': arp_statistics_list, 'bgp_instances_list': bgp_instances_list, 'bgp_routes_list': bgp_routes_list, 'bgp_tables_list': bgp_tables_list, 'config_list': config_list, 'interface_list': interface_list, 'platform_list': platform_list, 'platform_slots_list': platform_slots_list, 'platform_virtual_list': platform_virtual_list, 'vlan_list': vlan_list,'vrf_list': vrf_list,'version_list': version_list,'ip_int_brief_list': ip_int_brief_list,'inventory_list': inventory_list, 'recommended_list': recommended_list}
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

def learn_config_latest(request):
    latest_timestamp = LearnConfig.objects.latest('timestamp')
    config_list = LearnConfig.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'config_list': config_list}
    return render(request, 'Latest/LearnConfig/learn_config_latest.html', context)

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

def recommended_latest(request):
    latest_timestamp = RecommendedRelease.objects.latest('timestamp')
    recommended_list = RecommendedRelease.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'recommended_list': recommended_list}
    return render(request, 'Latest/Recommended/recommended_latest.html', context)

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