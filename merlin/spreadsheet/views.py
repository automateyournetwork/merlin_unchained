from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, RecommendedRelease, ShowInventory, ShowIPIntBrief, ShowVersion
import csv

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

def learn_config_csv(request):
    return render(request, 'CSV/LearnConfig/learn_config_csv.html')

def learn_config_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_config_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Configuration Key','Configuration Value','Timestamp'])
    configs = LearnConfig.objects.all().values_list('pyats_alias','timestamp')
    config_json = LearnConfig.objects.all().values_list('config')
    newrow = []
    for config in configs: 
        for inner_config in config_json:
            for key in inner_config:
                for inner_key, value in key.items():
                    newrow = (config[0],inner_key,value,config[1])
                    writer.writerow(newrow)
                    newrow = []
    return response

def learn_config_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_config_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Configuration Key','Configuration Value','Timestamp'])
    latest_timestamp = LearnConfig.objects.latest('timestamp')
    configs = LearnConfig.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','timestamp')
    config_json = LearnConfig.objects.filter(timestamp=latest_timestamp.timestamp).values_list('config')
    newrow = []
    for config in configs: 
        for inner_config in config_json:
            for key in inner_config:
                for inner_key, value in key.items():
                    newrow = (config[0],inner_key,value,config[1])
                    writer.writerow(newrow)
                    newrow = []
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

def learn_platform_csv(request):
    return render(request, 'CSV/LearnPlatform/learn_platform_csv.html')

def learn_platform_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Chassis','Chassis Serial Number','Free Disk Space','Total Disk Space','Used Disk Space','Image','Installed Packages','Main Memory','RP Uptime','Router Type','Version','Timestamp'])
    platforms = LearnPlatform.objects.all().values_list('pyats_alias','chassis','chassis_sn','disk_free_space','disk_total_space','disk_used_space','image','installed_packages','main_mem','rp_uptime','rtr_type','version','timestamp')
    for platform in platforms:
        writer.writerow(platform)
    return response

def learn_platform_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Chassis','Chassis Serial Number','Free Disk Space','Total Disk Space','Used Disk Space','Image','Installed Packages','Main Memory','RP Uptime','Router Type','Version','Timestamp'])
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platforms = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','chassis','chassis_sn','disk_free_space','disk_total_space','disk_used_space','image','installed_packages','main_mem','rp_uptime','rtr_type','version','timestamp')
    for platform in platforms:
        writer.writerow(platform)
    return response

def learn_platform_slots_csv(request):
    return render(request, 'CSV/LearnPlatformSlots/learn_platform_slots_csv.html')

def learn_platform_slots_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_slots_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Slot','Slot Name','Slot Serial Number','Slot State','Slot Redundancy State','RP Boot Image','Slot RP Uptime','Timestamp'])
    platform_slots = LearnPlatformSlots.objects.all().values_list('pyats_alias','slot','slot_name','slot_sn','slot_state','slot_redundancy_state','rp_boot_image','slot_rp_uptime','timestamp')
    for platform_slot in platform_slots:
        writer.writerow(platform_slot)
    return response

def learn_platform_slots_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_slots_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Slot','Slot Name','Slot Serial Number','Slot State','Slot Redundancy State','RP Boot Image','Slot RP Uptime','Timestamp'])
    latest_timestamp = LearnPlatformSlots.objects.latest('timestamp')
    platform_slots = LearnPlatformSlots.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','slot','slot_name','slot_sn','slot_state','slot_redundancy_state','rp_boot_image','slot_rp_uptime','timestamp')
    for platform_slot in platform_slots:
        writer.writerow(platform_slot)
    return response      

def learn_platform_virtual_csv(request):
    return render(request, 'CSV/LearnPlatformVirtual/learn_platform_virtual_csv.html')

def learn_platform_virtual_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_virtual_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Virtual Device Name','Virtual Device Status','Virtual Device Member','Virtual Device Member Status','Virtual Device Member Type','Timestamp'])
    platform_virtuals = LearnPlatformVirtual.objects.all().values_list('pyats_alias','virtual_device_name','virtual_device_status','virtual_device_member','virtual_device_member_status','virtual_device_member_type','timestamp')
    for platform_virtual in platform_virtuals:
        writer.writerow(platform_virtual)
    return response

def learn_platform_virtual_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_platform_virtual_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Virtual Device Name','Virtual Device Status','Virtual Device Member','Virtual Device Member Status','Virtual Device Member Type','Timestamp'])
    latest_timestamp = LearnPlatformVirtual.objects.latest('timestamp')
    platform_virtuals = LearnPlatformVirtual.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','virtual_device_name','virtual_device_status','virtual_device_member','virtual_device_member_status','virtual_device_member_type','timestamp')
    for platform_virtual in platform_virtuals:
        writer.writerow(platform_virtual)
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

def recommended_csv(request):
    return render(request, 'CSV/Recommended/recommended_csv.html')    

def recommended_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="recommended_release_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Base PID','Product Name','Software Type','Image Name','Description','Feature Set','Image Size','Suggested Release','Major Release','Release Train','Release Display Name','Release Date','Release Lifecycle','Currently Installed Version','Complaint','Timestamp'])
    recommendations = RecommendedRelease.objects.all().values_list('pyats_alias','basePID','productName','softwareType','imageName','description','featureSet','imageSize','isSuggested','majorRelease','releaseTrain','relDispName','releaseDate','releaseLifeCycle','installed_version', 'compliant','timestamp')
    for recommended in recommendations:
        writer.writerow(recommended)
    return response

def recommended_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="recommended_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Base PID','Product Name','Software Type','Image Name','Description','Feature Set','Image Size','Suggested Release','Major Release','Release Train','Release Display Name','Release Date','Release Lifecycle','Currently Installed Version','Complaint','Timestamp'])
    latest_timestamp = RecommendedRelease.objects.latest('timestamp')
    recommendations = RecommendedRelease.objects.all().values_list('pyats_alias','basePID','productName','softwareType','imageName','description','featureSet','imageSize','isSuggested','majorRelease','releaseTrain','relDispName','releaseDate','releaseLifeCycle','installed_version', 'compliant','timestamp')
    for recommended in recommendations:
        writer.writerow(recommended)
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