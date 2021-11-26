import os
import time
from django.shortcuts import render
from merlin.models import Devices, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowIPIntBrief, ShowLicenseSummary, ShowVersion

# CSV VIEWS
def mindmap_page(request):
    device_list = Devices.objects.all()
    context = {'device_list': device_list}
    return render(request, 'Mindmap/mindmap.html', context) 

def eox_pid_mindmap(request, pyats_alias):
    latest_timestamp = EoX_PID.objects.latest('timestamp')
    pid_list = EoX_PID.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest End of Life - Product ID\n","| Alias | Operating System | Part ID | Description | Bulletin Number | Bulletin URL | Published Date | End of Sale | End of Software Maintenance | End of Security | End of Routine Failure | End of Service Contract Renewal | Last Date of Support | End of SVC Attachment | Last Updated | Part ID Active | Migration Information | Migration Option | Migration Product ID | Migration Product Name | Migration Strategy | Migration Product Info URL | Timestamp |\n","| ----- | ---------------- | ------- | ----------- | --------------- | ------------ | -------------- | ----------- | --------------------------- | --------------- | ---------------------- | ------------------------------- | -------------------- | --------------------- | ------------ | -------------- | --------------------- | ---------------- | -------------------- | ---------------------- | ------------------ | -------------------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for pid in pid_list:
        markdown_data = f"| { pid.pyats_alias } | { pid.os } | { pid.pid } | { pid.description } | { pid.bulletin_number } | <{ pid.bulletin_url }> | { pid.external_date } | { pid.sale_date } | { pid.sw_maintenance } | { pid.security } | { pid.routine_failure } | { pid.service_contract } | { pid.last } | { pid.svc_attach } | { pid.last_updated } | { pid.pid_active } | { pid.migration_information } | { pid.migration_option } | { pid.migration_pid } | { pid.migration_name } | { pid.migration_strat } | <{ pid.migration_url }> | { pid.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_eox_pid_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_eox_pid_mind_map.html' % pyats_alias)

def eox_sn_mindmap(request, pyats_alias):
    latest_timestamp = EoX_SN.objects.latest('timestamp')
    sn_list = EoX_SN.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest End of Life - Serial Number\n","| Alias | Operating System | Part ID | Description | Bulletin Number | Bulletin URL | Published Date | End of Sale | End of Software Maintenance | End of Security | End of Routine Failure | End of Service Contract Renewal | Last Date of Support | End of SVC Attachment | Last Updated | Part ID Active | Migration Information | Migration Option | Migration Product ID | Migration Product Name | Migration Strategy | Migration Product Info URL | Timestamp |\n","| ----- | ---------------- | ------- | ----------- | --------------- | ------------ | -------------- | ----------- | --------------------------- | --------------- | ---------------------- | ------------------------------- | -------------------- | --------------------- | ------------ | -------------- | --------------------- | ---------------- | -------------------- | ---------------------- | ------------------ | -------------------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for sn in sn_list:
        markdown_data = f"| { sn.pyats_alias} | { sn.os } | { sn.pid } | { sn.description } | { sn.bulletin_number } | { sn.bulletin_url } | { sn.external_date } | { sn.sale_date} | { sn.sw_maintenance } | { sn.security } | { sn.routine_failure } | { sn.service_contract,sn } | { last } | { sn.svc_attach } | { sn.last_updated } | { sn.sn_active } | { sn.migration_information } | { sn.migration_option } | { sn.migration_sn } | { sn.migration_name } | { sn.migration_strat } | <{ sn.migration_url }> | { sn.timestamp }|\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_eox_sn_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_eox_sn_mind_map.html' % pyats_alias)

def eox_sw_mindmap(request, pyats_alias):
    latest_timestamp = EoX_IOS.objects.latest('timestamp')
    sw_list = EoX_IOS.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest End of Life - Software\n","| Alias | Operating System | Part ID | Description | Bulletin Number | Bulletin URL | Published Date | End of Sale | End of Software Maintenance | End of Security | End of Routine Failure | End of Service Contract Renewal | Last Date of Support | End of SVC Attachment | Last Updated | Part ID Active | Migration Information | Migration Option | Migration Product ID | Migration Product Name | Migration Strategy | Migration Product Info URL | Timestamp |\n","| ----- | ---------------- | ------- | ----------- | --------------- | ------------ | -------------- | ----------- | --------------------------- | --------------- | ---------------------- | ------------------------------- | -------------------- | --------------------- | ------------ | -------------- | --------------------- | ---------------- | -------------------- | ---------------------- | ------------------ | -------------------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for sw in sw_list:
        markdown_data = f"| { sw.pyats_alias} | { sw.os } | { sw.pid } | { sw.description } | { sw.bulletin_number } | { sw.bulletin_url } | { sw.external_date } | { sw.sale_date} | { sw.sw_maintenance } | { sw.security } | { sw.routine_failure } | { sw.service_contract,sw } | { last } | { sw.svc_attach } | { sw.last_updated } | { sw.sw_active } | { sw.migration_information } | { sw.migration_option } | { sw.migration_sw } | { sw.migration_name } | { sw.migration_strat } | <{ sw.migration_url }> | { sw.timestamp }|\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_eox_sw_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_eox_sw_mind_map.html' % pyats_alias)    

def learn_acl_mindmap(request, pyats_alias):
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn ACL\n","| Alias | Operating System | Access Control List | Access Control Entry | Permission | Logging | Source Network | Destination Network | Layer 3 Protocol | Layer 4 Protocol | Operator | Port | Timestamp |\n","| ----- | ---------------- | ------------------- | -------------------- | ---------- | ------- | -------------- | ------------------- | ---------------- | ---------------- | -------- | ---- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for acl in acl_list:
        markdown_data = f"| { acl.pyats_alias } | { acl.os } | { acl.acl } | { acl.ace } | { acl.permission } | { acl.logging } | { acl.source_network } | { acl.destination_network } | { acl.l3_protocol } | { acl.l4_protocol } | { acl.operator } | { acl.port } | { acl.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_acl_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_acl_mind_map.html' % pyats_alias)

def learn_arp_mindmap(request, pyats_alias):
    latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn ARP\n","| Alias | Operating System | Interface | Neighbor IP | Neighbor MAC | Origin | Local Proxy | Proxy | Timestamp |\n","| ----- | ---------------- | --------- | ----------- | ------------ | ------ | ----------- | ----- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for arp in arp_list:
        markdown_data = f"| { arp.pyats_alias } | { arp.os } | { arp.interface } | { arp.neighbor_ip } | { arp.neighbor_mac } | { arp.origin } | { arp.local_proxy } | { arp.proxy } | { arp.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_arp_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_arp_mind_map.html' % pyats_alias)

def learn_arp_statistics_mindmap(request, pyats_alias):
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_list = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn ARP Statistics\n","| Alias | Operating System | Total Entries | Input Drops | Input Replies | Input Requests | Total Incomplete | Output Replies | Output Requests | Timestamp |\n","| ----- | ---------------- | ------------- | ----------- | ------------- | -------------- | ---------------- | -------------- | --------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for arp in arp_list:
        markdown_data = f"| { arp.pyats_alias } | { arp.os } | { arp.entries_total } | { arp.in_drops } | { arp.in_replies_pkts } | { arp.in_requests_pkts } | { arp.incomplete_total } | { arp.out_replies_pkts } | { arp.out_requests_pkts } | { arp.timestamp }|\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_arp_statistics_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_arp_statistics_mind_map.html' % pyats_alias)

def learn_bgp_instances_mindmap(request, pyats_alias):
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    bgp_instance_list = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn BGP Instances\n","| Alias | Operating System | Instance | BGP ID | Protocol State | Next Hop Trigger Critical Delay | Next Hop Trigger Delay | Next Hop Trigger Enabled | VRF | Router ID | Cluster ID | Confederation ID | Neighbor | Version | Hold Time | Keep Alive Interval | Local AS | Remote AS | Received Bytes in Queue | Received Capability | Received Keep Alives | Received Notifications | Received Opens | Received Route Refresh | Received Total | Received Total Bytes | Recieved Updates | Sent Bytes in Queue | Sent Capability | Sent Keep Alives | Sent Notifications | Sent Opens | Sent Route Refresh | Sent Total | Sent Total Bytes | Sent Updates | Last Reset | Reset Reason | Timestamp |\n","| ----- | ---------------- | -------- | ------ | -------------- | ------------------------------- | ---------------------- | ------------------------ | --- | --------- | ---------- | ---------------- | -------- | ------- | --------- | ------------------- | -------- | --------- | ----------------------- | ------------------- | -------------------- | ---------------------- | -------------- | ---------------------- | -------------- | -------------------- | ---------------- | ------------------- | --------------- | ---------------- | ------------------ | ---------- | ------------------ | ---------- | ---------------- | ------------ | ---------- | ------------ | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for instance in bgp_instance_list:
        markdown_data = f"| { instance.pyats_alias } | { instance.os } | { instance.instance } | { instance.bgp_id } | { instance.protocol_state } | { instance.nexthop_trigger_delay_critical } | { instance.nexthop_trigger_delay_noncritical } | { instance.nexthop_trigger_enabled } | { instance.vrf } | { instance.router_id } | { instance.cluster_id } | { instance.confederation_id } | { instance.neighbor } | { instance.version } | { instance.hold_time } | { instance.keep_alive_interval } | { instance.local_as } | { instance.remote_as } | { instance.neighbor_counters_received_bytes_in_queue } | { instance.neighbor_counters_received_capability } | { instance.neighbor_counters_received_keepalives } | { instance.neighbor_counters_received_notifications } | { instance.neighbor_counters_received_opens } | { instance.neighbor_counters_received_route_refresh } | { instance.neighbor_counters_received_total } | { instance.neighbor_counters_received_total_bytes } | { instance.neighbor_counters_received_updates } | { instance.neighbor_counters_sent_bytes_in_queue } | { instance.neighbor_counters_sent_capability } | { instance.neighbor_counters_sent_keepalives } | { instance.neighbor_counters_sent_notifications } | { instance.neighbor_counters_sent_opens } | { instance.neighbor_counters_sent_route_refresh } | { instance.neighbor_counters_sent_total } | { instance.neighbor_counters_sent_total_bytes } | { instance.neighbor_counters_sent_updates } | { instance.last_reset } | { instance.reset_reason } | { instance.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_bgp_instances_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_bgp_instances_mind_map.html' % pyats_alias)

def learn_bgp_route_mindmap(request, pyats_alias):
    latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    bgp_route_list = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn BGP Routes\n","| Alias | Operating System | Instance | VRF | Neighbor | Advertised | Routes | Remote AS | Timestamp |\n","| ----- | ---------------- | -------- | --- | -------- | ---------- | ------ | --------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for route in bgp_route_list:
        markdown_data = f"| { route.pyats_alias } | { route.os } | { route.instance } | { route.vrf } | { route.neighbor } | { route.advertised } | { route.routes } | { route.remote_as } | { route.timestamp } |\n" % ()
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_bgp_routes_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_bgp_routes_mind_map.html' % pyats_alias)

def learn_bgp_table_mindmap(request, pyats_alias):
    latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    bgp_table_list = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn BGP Tables\n","| Alias | Operating System | Instance | VRF | Table Version | Prefix | Index | Local Preference | Next Hop | Origin Code | Status Code | Weight | Timestamp |\n","| ----- | ---------------- | -------- | --- | ------------- | ------ | ----- | ---------------- | -------- | ----------- | ----------- | ------ | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for table in bgp_table_list:
        markdown_data = f"| { table.pyats_alias } | { table.os } | { table.instance } | { table.vrf } | { table.table_version } | { table.prefix } | { table.index } | { table.localpref } | { table.next_hop } | { table.origin_code } | { table.status_code } | { table.weight } | { table.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_bgp_tables_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_bgp_tables_mind_map.html' % pyats_alias)

def learn_interface_mindmap(request, pyats_alias):
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn Interface\n","| Alias | Operating System | Interface | Description | Enabled | Status | Access VLAN | Native VLAN | Switchport | Switchport Mode | Interface Type | Bandwidth | Auto Negotiate | Speed | Duplex | MTU | MAC Address | Physical Address | IP Address | Medium | Delay | Encapsulation | Flow Control Receive | Flow Control Send | Port Channel | Port Channel Member Interfaces | Port Channel Member | Last Change | Input Broadcast | Input CRC Errors | Input MAC Pause Frames | Input Multicast | Input Octets | Input Unicast | Input Unknown | Input Total | Output Broadcast | Output Discard | Output Errors | Output MAC Pause Frames | Output Multicast | Output Unicast | Output Total | Last Clear | Input Rate | Load Interval | Output Rate | Timestamp |\n","| ----- | ---------------- | --------- | ----------- | ------- | ------ | ----------- | ----------- | ---------- | --------------- | -------------- | --------- | -------------- | ----- | ------ | --- | ----------- | ---------------- | ---------- | ------ | ----- | ------------- | -------------------- | ----------------- | ------------ | ------------------------------ | ------------------- | ----------- | --------------- | ---------------- | ---------------------- | --------------- | ------------ | ------------- | ------------- | ----------- | ---------------- | -------------- | ------------- | ----------------------- | ---------------- | -------------- | ------------ | ---------- | ---------- | ------------- | ----------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for interface in interface_list:
        markdown_data = f"| { interface.pyats_alias } | { interface.os } | { interface.interface } | { interface.description } | { interface.enabled } | { interface.status } | { interface.access_vlan } | { interface.native_vlan } | { interface.switchport } | { interface.switchport_mode } | { interface.interface_type } | { interface.bandwidth } | { interface.auto_negotiate } | { interface.speed } | { interface.duplex } | { interface.mtu } | { interface.mac_address } | { interface.physical_address } | { interface.ip_address } | { interface.medium } | { interface.delay } | { interface.encapsulation } | { interface.flow_control_receive } | { interface.flow_control_send } | { interface.port_channel } | { interface.port_channel_member_interfaces } | { interface.port_channel_member } | { interface.last_change } | { interface.input_broadcast } | { interface.input_crc_errors } | { interface.input_errors } | { interface.input_mac_pause_frames } | { interface.input_multicast } | { interface.input_octets } | { interface.input_unicast } | { interface.input_unknown } | { interface.input_total } | { interface.output_broadcast } | { interface.output_discard } | { interface.output_errors } | { interface.output_mac_pause_frames } | { interface.output_multicast } | { interface.output_unicast } | { interface.output_total } | { interface.last_clear } | { interface.input_rate } | { interface.load_interval } | { interface.output_rate } | { interface.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_interface_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_interface_mind_map.html' % pyats_alias)

def learn_platform_mindmap(request, pyats_alias):
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn Platform\n","| Alias | Operating System | Chassis | Chassis Serial Number | Free Disk Space | Total Disk Space | Used Disk Space | Image | Installed Packages | Main Memory | RP Uptime | Router Type | Version | Timestamp |\n","| ----- | ---------------- | ------- | --------------------- | --------------- | ---------------- | --------------- | ----- | ------------------ | ----------- | --------- | ----------- | ------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for item in platform_list:
        markdown_data = f"| { item.pyats_alias } | { item.os } | { item.chassis } | { item.chassis_sn } | { item.disk_free_space } | { item.disk_total_space } | { item.disk_used_space } | { item.image } | { item.installed_packages } | { item.main_mem } | { item.rp_uptime } | { item.rtr_type } | { item.version } | { item.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_platform_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_platform_mind_map.html' % pyats_alias)

def learn_vlan_mindmap(request, pyats_alias):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlan_list = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn VLAN\n","| Alias | Operating System | VLAN | Interfaces | Mode | Name | Shutdown | State | Timestamp |\n","| ----- | ---------------- | ---- | ---------- | ---- | ---- | -------- | ----- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for vlan in vlan_list:
        markdown_data = f"| { vlan.pyats_alias } | { vlan.os } | { vlan.vlan } | { vlan.interfaces } | { vlan.mode } | { vlan.name } | { vlan.shutdown } | { vlan.state } | { vlan.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_vlan_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_vlan_mind_map.html' % pyats_alias)

def learn_vrf_mindmap(request, pyats_alias):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrf_list = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn VRF\n","| Alias | Operating System | VRF | Route Distinguisher | Timestamp |\n","| ----- | ---------------- | --- | ------------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for vrf in vrf_list:
        markdown_data = f"| { vrf.pyats_alias } | { vrf.os } | { vrf.vrf } | { vrf.route_distinguisher } | { vrf.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_vrf_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_vrf_mind_map.html' % pyats_alias)

def nmap_mindmap(request, pyats_alias):
    latest_timestamp = NMAP.objects.latest('timestamp')
    nmap_list = NMAP.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Network Map\n","| Alias | Operating System | Protocol | Port | Conf | CPE | Extra Info | Name | Product | Reason | State | Version | Timestamp |\n","| ----- | ---------------- | -------- | ---- | ---- | --- | ---------- | ---- | ------- | ------ | ----- | ------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for map in nmap_list:
        markdown_data = f"| { map.pyats_alias } | { map.os } | { map.protocol } | { map.port } | { map.conf } | { map.cpe } | { map.extra_info } | { map.name } | { map.product } | { map.reason } | { map.state } | { map.version } | { map.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_nmap_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_nmap_mind_map.html' % pyats_alias)

def show_inventory_mindmap(request, pyats_alias):
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Show Inventory\n","| Alias | Operating System | Part | Description | Part ID | Serial Number | Timestamp |\n","| ----- | ---------------- | ---- | ----------- | ------- | ------------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for item in inventory_list:
        markdown_data = f"| { item.pyats_alias } | { item.os } | { item.part } | { item.description } | { item.pid } | { item.serial_number } | { item.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_show_inventory_summary_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_show_inventory_summary_mind_map.html' % pyats_alias)

def show_ip_int_brief_mindmap(request, pyats_alias):
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interface_list = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Show IP Interface Brief\n","| Alias | Operating System | Interface | Interface Status | IP Address | Timestamp |\n","| ----- | ---------------- | --------- | ---------------- | ---------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for interface in interface_list:
        markdown_data = f"| { interface.pyats_alias } | { interface.os } | { interface.interface } | { interface.interface_status } | { interface.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_show_ip_interface_brief_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_show_ip_interface_brief_mind_map.html' % pyats_alias)

def show_license_summary_mindmap(request, pyats_alias):
    latest_timestamp = ShowLicenseSummary.objects.latest('timestamp')
    license_list = ShowLicenseSummary.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Show License Summary\n","| Alias | Operating System | License Name | Entitlement | Count | Status | Timestamp |\n","| ----- | ---------------- | ------------ | ----------- | ----- | ------ | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for license in license_list:
        markdown_data = f"| { license.pyats_alias } | { license.os } | { license.license_name } | { license.entitlement } | { license.count } | { license.status } | { license.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_show_license_summary_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_show_license_summary_mind_map.html' % pyats_alias)

def show_version_mindmap(request, pyats_alias):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Show Version\n","| Alias | Operating System | Bootflash | Chassis | CPU | Device Name | Memory | Model | Processor Board ID | RP | Slots | Uptime Days | Hours | Minutes | Seconds | Name | Last Reload Reason | System Compile Time | System Image File | System Version | Chassis Serial Number | Compiled By | Current Config Register | Image ID | Image Type | Label | License Level | License Type | Non Volatile | Physical | Next Reload License Level | Platform | Processor Type | Returned to ROM by | ROM | Router Type | Uptime | Uptime this CP | Version Short | XE Version | Timestamp |\n","| ----- | ---------------- | --------- | ------- | --- | ----------- | ------ | ----- | ------------------ | -- | ----- | ----------- | ----- | ------- | ------- | ---- | ------------------ | ------------------- | ----------------- | -------------- | --------------------- | ----------- | ----------------------- | -------- | ---------- | ----- | ------------- | ------------ | ------------ | -------- | ------------------------- | -------- | -------------- | ------------------ | --- | ----------- | ------ | -------------- | ------------- | ---------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for version in version_list:
        markdown_data = f"| { version.pyats_alias } | { version.os } | { version.bootflash } | { version.chassis } | { version.cpu } | { version.device_name } | { version.memory } | { version.model } | { version.processor_board_id } | { version.rp } | { version.slots } | { version.days } | { version.hours } | { version.minutes } | { version.seconds } | { version.name } | { version.os } | { version.reason } | { version.system_compile_time } | { version.system_image_file } | { version.system_version } | { version.chassis_sn } | { version.compiled_by } | { version.curr_config_register } | { version.image_id } | { version.image_type } | { version.label } | { version.license_level } | { version.license_type } | { version.non_volatile } | { version.physical } | { version.next_reload_license_level } | { version.platform } | { version.processor_type } | { version.returned_to_rom_by } | { version.rom } | { version.rtr_type } | { version.uptime } | { version.uptime_this_cp } | { version.version_short } | { version.xe_version } | { version.timestamp } |\n"
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_show_version_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_show_version_mind_map.html' % pyats_alias)    