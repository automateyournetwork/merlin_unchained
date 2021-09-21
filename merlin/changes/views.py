import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from merlin.models import Devices, DynamicJobInput, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnInterface, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

# Changes Buttons

def changes(request):
    return render(request, 'Changes/changes.html')

def all_changes(request):
    acl_latest_timestamp = LearnACL.objects.latest('timestamp')
    current_acls = LearnACL.objects.filter(timestamp=acl_latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    arp_latest_timestamp = LearnARP.objects.latest('timestamp')
    current_arp = LearnARP.objects.filter(timestamp=arp_latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_stats_latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")    
    bgp_latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_route_latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_table_latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    current_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
    interfaces_latest_timestamp = LearnInterface.objects.latest('timestamp')
    current_interface = LearnInterface.objects.filter(timestamp=interfaces_latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job populate_db_job.py')
    acl_new_timestamp = LearnACL.objects.latest('timestamp')
    latest_acls = LearnACL.objects.filter(timestamp=acl_new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    arp_new_timestamp = LearnARP.objects.latest('timestamp')
    latest_arp = LearnARP.objects.filter(timestamp=arp_new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_stats_new_timestamp = LearnARPStatistics.objects.latest('timestamp')
    latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    bgp_new_timestamp = LearnBGPInstances.objects.latest('timestamp')
    latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_route_new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_table_new_timestamp = LearnBGPTables.objects.latest('timestamp')
    latest_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
    interface_new_timestamp = LearnInterface.objects.latest('timestamp')
    latest_interface = LearnInterface.objects.filter(timestamp=interface_new_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
    vlan_new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=vlan_new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=vrf_new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=version_new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")    
    acl_removals = current_acls.difference(latest_acls)
    acl_additions = latest_acls.difference(current_acls)
    arp_removals = current_arp.difference(latest_arp)
    arp_additions = latest_arp.difference(current_arp)
    arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
    arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
    bgp_instances_removals = current_bgp_instances.difference(latest_bgp_instances)
    bgp_instances_additions = latest_bgp_instances.difference(current_bgp_instances)
    bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
    bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
    bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
    bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
    interface_removals = current_interface.difference(latest_interface)
    interface_additions = latest_interface.difference(current_interface)
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)       
    return render(request, 'Changes/all_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions, 'arp_removals': arp_removals,'arp_additions': arp_additions, 'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions, 'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions, 'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions, 'bgp_table_removals': bgp_table_removals,'bgp_table_additions': bgp_table_additions, 'interface_removals': interface_removals,'interface_additions': interface_additions, 'vlan_removals': vlan_removals, 'vlan_additions': vlan_additions, 'vlan_latest_timestamp': vlan_latest_timestamp.timestamp, 'vlan_new_timestamp': vlan_new_timestamp.timestamp, 'vrf_removals': vrf_removals, 'vrf_additions': vrf_additions, 'vrf_latest_timestamp': vrf_latest_timestamp.timestamp, 'vrf_new_timestamp': vrf_new_timestamp.timestamp, 'version_removals': version_removals, 'version_additions': version_additions, 'version_latest_timestamp': version_latest_timestamp.timestamp, 'version_new_timestamp': version_new_timestamp.timestamp})

def learn_acl_changes(request):
    latest_timestamp = LearnACL.objects.latest('timestamp')
    current_acls = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    os.system('pyats run job learn_vlan_job.py')
    new_timestamp = LearnACL.objects.latest('timestamp')
    latest_acls = LearnACL.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    acl_removals = current_acls.difference(latest_acls)
    acl_additions = latest_acls.difference(current_acls)
    return render(request, 'Changes/learn_acl_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions})

def learn_arp_changes(request):
    latest_timestamp = LearnARP.objects.latest('timestamp')
    current_arp = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    os.system('pyats run job learn_arp_job.py')
    new_timestamp = LearnARP.objects.latest('timestamp')
    latest_arp = LearnARP.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_removals = current_arp.difference(latest_arp)
    arp_additions = latest_arp.difference(current_arp)
    return render(request, 'Changes/learn_arp_changes.html', {'arp_removals': arp_removals,'arp_additions': arp_additions})

def learn_arp_statistics_changes(request):
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    os.system('pyats run job learn_arp_job.py')
    new_timestamp = LearnARPStatistics.objects.latest('timestamp')
    latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
    arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
    return render(request, 'Changes/learn_arp_statistics_changes.html', {'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions})

def learn_bgp_instances_changes(request):
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    os.system('pyats run job learn_bgp_job.py')
    new_timestamp = LearnBGPInstances.objects.latest('timestamp')
    latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_instances_removals = current_bgp_instances.difference(latest_bgp_instances)
    bgp_instances_additions = latest_bgp_instances.difference(current_bgp_instances)
    return render(request, 'Changes/learn_bgp_instances_changes.html', {'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions})

def learn_bgp_route_changes(request):
    latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    os.system('pyats run job learn_bgp_job.py')
    new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
    bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
    return render(request, 'Changes/learn_bgp_route_changes.html', {'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions})

def learn_bgp_table_changes(request):
    latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    current_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
    os.system('pyats run job learn_bgp_job.py')
    new_timestamp = LearnBGPTables.objects.latest('timestamp')
    latest_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
    bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
    bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
    return render(request, 'Changes/learn_bgp_table_changes.html', {'bgp_table_removals': bgp_table_removals,'bgp_table_additions': bgp_table_additions})

def learn_interface_changes(request):
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    current_interface = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
    os.system('pyats run job learn_interface_job.py')
    new_timestamp = LearnInterface.objects.latest('timestamp')
    latest_interface = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
    interface_removals = current_interface.difference(latest_interface)
    interface_additions = latest_interface.difference(current_interface)
    return render(request, 'Changes/learn_interface_changes.html', {'interface_removals': interface_removals,'interface_additions': interface_additions})

def learn_vlan_changes(request):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    os.system('pyats run job learn_vlan_job.py')
    new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    return render(request, 'Changes/learn_vlan_changes.html', {'vlan_removals': vlan_removals,'vlan_additions': vlan_additions})

def learn_vrf_changes(request):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    os.system('pyats run job learn_vrf_job.py')
    new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    return render(request, 'Changes/learn_vrf_changes.html', {'vrf_removals': vrf_removals,'vrf_additions': vrf_additions})

def show_inventory_changes(request):
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    current_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
    os.system('pyats run job show_inventory_job.py')
    new_timestamp = ShowInventory.objects.latest('timestamp')
    latest_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
    inventory_removals = current_inventory.difference(latest_inventory)
    inventory_additions = latest_inventory.difference(current_inventory)
    return render(request, 'Changes/show_inventory_changes.html', {'inventory_removals': inventory_removals,'inventory_additions': inventory_additions})

def show_ip_int_brief_changes(request):
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    current_interfaces = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
    os.system('pyats run job show_ip_int_brief_job.py')
    new_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    latest_interfaces = ShowIPIntBrief.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
    interface_removals = current_interfaces.difference(latest_interfaces)
    interface_additions = latest_interfaces.difference(current_interfaces)
    return render(request, 'Changes/show_ip_int_brief_changes.html', {'interface_removals': interface_removals,'interface_additions': interface_additions})

def show_version_changes(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job learn_vrf_job.py')
    new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)
    return render(request, 'Changes/show_version_changes.html', {'version_removals': version_removals,'version_additions': version_additions})

# Changes Filters / User Input

class ChangesResultAll(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        acl_latest_timestamp = LearnACL.objects.latest('timestamp')
        current_acls = LearnACL.objects.filter(timestamp=acl_latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
        arp_latest_timestamp = LearnARP.objects.latest('timestamp')
        current_arp = LearnARP.objects.filter(timestamp=arp_latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
        arp_stats_latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
        current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")    
        bgp_latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
        current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
        bgp_route_latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
        current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
        bgp_table_latest_timestamp = LearnBGPTables.objects.latest('timestamp')
        current_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
        interfaces_latest_timestamp = LearnInterface.objects.latest('timestamp')
        current_interface = LearnInterface.objects.filter(timestamp=interfaces_latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
        vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
        current_vlans = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
        vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
        current_vrfs = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
        version_latest_timestamp = ShowVersion.objects.latest('timestamp')
        current_version = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")        
        query = self.request.GET.get('get_all_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()          
        os.system('pyats run job populate_db_filter_job.py')
        acl_new_timestamp = LearnACL.objects.latest('timestamp')
        latest_acls = LearnACL.objects.filter(timestamp=acl_new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
        arp_new_timestamp = LearnARP.objects.latest('timestamp')
        latest_arp = LearnARP.objects.filter(timestamp=arp_new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
        arp_stats_new_timestamp = LearnARPStatistics.objects.latest('timestamp')
        latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
        bgp_new_timestamp = LearnBGPInstances.objects.latest('timestamp')
        latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
        bgp_route_new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
        latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
        bgp_table_new_timestamp = LearnBGPTables.objects.latest('timestamp')
        latest_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
        interface_new_timestamp = LearnInterface.objects.latest('timestamp')
        latest_interface = LearnInterface.objects.filter(timestamp=interface_new_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
        vlan_new_timestamp = LearnVLAN.objects.latest('timestamp')
        latest_vlans = LearnVLAN.objects.filter(timestamp=vlan_new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
        vrf_new_timestamp = LearnVRF.objects.latest('timestamp')
        latest_vrfs = LearnVRF.objects.filter(timestamp=vrf_new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
        version_new_timestamp = ShowVersion.objects.latest('timestamp')
        latest_version = ShowVersion.objects.filter(timestamp=version_new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")    
        acl_removals = current_acls.difference(latest_acls)
        acl_additions = latest_acls.difference(current_acls)
        arp_removals = current_arp.difference(latest_arp)
        arp_additions = latest_arp.difference(current_arp)
        arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
        arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
        bgp_instances_removals = current_bgp_instances.difference(latest_bgp_instances)
        bgp_instances_additions = latest_bgp_instances.difference(current_bgp_instances)
        bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
        bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
        bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
        bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
        interface_removals = current_interface.difference(latest_interface)
        interface_additions = latest_interface.difference(current_interface)
        vlan_removals = current_vlans.difference(latest_vlans)
        vlan_additions = latest_vlans.difference(current_vlans)
        vrf_removals = current_vrfs.difference(latest_vrfs)
        vrf_additions = latest_vrfs.difference(current_vrfs)
        version_removals = current_version.difference(latest_version)
        version_additions = latest_version.difference(current_version)
        return render(request, 'Changes/all_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions, 'arp_removals': arp_removals,'arp_additions': arp_additions, 'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions, 'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions, 'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions, 'bgp_table_removals': bgp_table_removals,'bgp_table_additions': bgp_table_additions, 'interface_removals': interface_removals,'interface_additions': interface_additions, 'vlan_removals': vlan_removals, 'vlan_additions': vlan_additions, 'vrf_removals': vrf_removals, 'vrf_additions': vrf_additions, 'version_removals': version_removals, 'version_additions': version_additions})

class ChangesResultACL(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnACL.objects.latest('timestamp')
        current_acls = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
        query = self.request.GET.get('learn_acl_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_acl_filter_job.py')
        new_timestamp = LearnACL.objects.latest('timestamp')
        latest_acls = LearnACL.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
        acl_removals = current_acls.difference(latest_acls)
        acl_additions = latest_acls.difference(current_acls)
        return render(request, 'Changes/learn_acl_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions})

class ChangesResultARP(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnARP.objects.latest('timestamp')
        current_arp = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
        query = self.request.GET.get('learn_arp_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_arp_filter_job.py')
        new_timestamp = LearnARP.objects.latest('timestamp')
        latest_arp = LearnARP.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
        arp_removals = current_arp.difference(latest_arp)
        arp_additions = latest_arp.difference(current_arp)
        return render(request, 'Changes/learn_arp_changes.html', {'arp_removals': arp_removals,'arp_additions': arp_additions})

class ChangesResultARPStatistics(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
        current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
        query = self.request.GET.get('learn_arp_statistics_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_arp_filter_job.py')
        new_timestamp = LearnARPStatistics.objects.latest('timestamp')
        latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
        arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
        arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
        return render(request, 'Changes/learn_arp_statistics_changes.html', {'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions})

class ChangesResultBGPInstance(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
        current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
        query = self.request.GET.get('learn_bgp_instance_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_bgp_filter_job.py')
        new_timestamp = LearnBGPInstances.objects.latest('timestamp')
        latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
        bgp_instances_removals = current_bgp_instances.difference(latest_bgp_instances)
        bgp_instances_additions = latest_bgp_instances.difference(current_bgp_instances)
        return render(request, 'Changes/learn_bgp_instance_changes.html', {'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions})        

class ChangesResultBGPRoute(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
        current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
        query = self.request.GET.get('learn_bgp_route_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_bgp_filter_job.py')
        new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
        latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
        bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
        bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
        return render(request, 'Changes/learn_bgp_route_changes.html', {'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions})        

class ChangesResultBGPTable(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnBGPTables.objects.latest('timestamp')
        current_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
        query = self.request.GET.get('learn_bgp_table_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_bgp_filter_job.py')
        new_timestamp = LearnBGPTables.objects.latest('timestamp')
        latest_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
        bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
        bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
        return render(request, 'Changes/learn_bgp_table_changes.html', {'bgp_table_removals': bgp_table_removals,'bgp_table_additions': bgp_table_additions})        

class ChangesResultInterface(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnInterface.objects.latest('timestamp')
        current_interface = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
        query = self.request.GET.get('learn_interface_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_interface_filter_job.py')
        new_timestamp = LearnInterface.objects.latest('timestamp')
        latest_interface = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_crc_errors', 'input_errors', 'input_unknown', 'output_discard', 'output_errors', 'last_clear')
        interface_removals = current_interface.difference(latest_interface)
        interface_additions = latest_interface.difference(current_interface)
        return render(request, 'Changes/learn_interface_changes.html', {'interface_removals': interface_removals,'interface_additions': interface_additions})

class ChangesResultVLAN(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnVLAN.objects.latest('timestamp')
        current_vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
        query = self.request.GET.get('learn_vlan_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_vlan_filter_job.py')
        new_timestamp = LearnVLAN.objects.latest('timestamp')
        latest_vlans = LearnVLAN.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
        vlan_removals = current_vlans.difference(latest_vlans)
        vlan_additions = latest_vlans.difference(current_vlans)
        return render(request, 'Changes/learn_vlan_changes.html', {'vlan_removals': vlan_removals,'vlan_additions': vlan_additions})

class ChangesResultVRF(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = LearnVRF.objects.latest('timestamp')
        current_vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
        query = self.request.GET.get('learn_vrf_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_vrf_filter_job.py')
        new_timestamp = LearnVRF.objects.latest('timestamp')
        latest_vrfs = LearnVRF.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
        vrf_removals = current_vrfs.difference(latest_vrfs)
        vrf_additions = latest_vrfs.difference(current_vrfs)
        return render(request, 'Changes/learn_vrf_changes.html', {'vrf_removals': vrf_removals,'vrf_additions': vrf_additions})

class ChangesResultInventory(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = ShowInventory.objects.latest('timestamp')
        current_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
        query = self.request.GET.get('show_inventory_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_inventory_filter_job.py')
        new_timestamp = ShowInventory.objects.latest('timestamp')
        latest_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
        inventory_removals = current_inventory.difference(latest_inventory)
        inventory_additions = latest_inventory.difference(current_inventory)
        return render(request, 'Changes/show_inventory_changes.html', {'inventory_removals': inventory_removals,'inventory_additions': inventory_additions})

class ChangesResultIPInterfaceBrief(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
        current_interfaces = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
        query = self.request.GET.get('show_ip_int_brief_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_ip_int_brief_filter_job.py')
        new_timestamp = ShowIPIntBrief.objects.latest('timestamp')
        latest_interfaces = ShowIPIntBrief.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
        interface_removals = current_interfaces.difference(latest_interfaces)
        interface_additions = latest_interfaces.difference(current_interfaces)
        return render(request, 'Changes/show_ip_int_brief_changes.html', {'interface_removals': interface_removals,'interface_additions': interface_additions})

class ChangesResultVersion(ListView):
    template_name = 'Changes/changes.html'

    def get(self, request):
        latest_timestamp = ShowVersion.objects.latest('timestamp')
        current_version = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
        query = self.request.GET.get('show_version_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_version_filter_job.py')
        new_timestamp = ShowVersion.objects.latest('timestamp')
        latest_version = ShowVersion.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
        version_removals = current_version.difference(latest_version)
        version_additions = latest_version.difference(current_version)
        return render(request, 'Changes/show_version_changes.html', {'version_removals': version_removals,'version_additions': version_additions})                        