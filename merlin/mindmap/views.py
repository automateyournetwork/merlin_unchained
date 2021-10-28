import os
import time
from django.shortcuts import render
from merlin.models import Devices, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowIPIntBrief, ShowVersion

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
        markdown_data = "| %s | %s | %s | %s | %s | <%s> | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | <%s> | %s |\n" % (pid.pyats_alias,pid.os,pid.pid,pid.description,pid.bulletin_number,pid.bulletin_url,pid.external_date,pid.sale_date,pid.sw_maintenance,pid.security,pid.routine_failure,pid.service_contract,pid.last,pid.svc_attach,pid.last_updated,pid.pid_active,pid.migration_information,pid.migration_option,pid.migration_pid,pid.migration_name,pid.migration_strat,pid.migration_url,pid.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | <%s> | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | <%s> | %s |\n" % (sn.pyats_alias,sn.os,sn.pid,sn.description,sn.bulletin_number,sn.bulletin_url,sn.external_date,sn.sale_date,sn.sw_maintenance,sn.security,sn.routine_failure,sn.service_contract,sn.last,sn.svc_attach,sn.last_updated,sn.sn_active,sn.migration_information,sn.migration_option,sn.migration_sn,sn.migration_name,sn.migration_strat,sn.migration_url,sn.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | <%s> | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | <%s> | %s |\n" % (sw.pyats_alias,sw.os,sw.pid,sw.description,sw.bulletin_number,sw.bulletin_url,sw.external_date,sw.sale_date,sw.sw_maintenance,sw.security,sw.routine_failure,sw.service_contract,sw.last,sw.svc_attach,sw.last_updated,sw.sw_active,sw.migration_information,sw.migration_option,sw.migration_sw,sw.migration_name,sw.migration_strat,sw.migration_url,sw.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (acl.pyats_alias,acl.os,acl.acl,acl.ace,acl.permission,acl.logging,acl.source_network,acl.destination_network,acl.l3_protocol,acl.l4_protocol,acl.operator,acl.port,acl.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (arp.pyats_alias,arp.os,arp.interface,arp.neighbor_ip,arp.neighbor_mac,arp.origin,arp.local_proxy,arp.proxy,arp.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (arp.pyats_alias,arp.os,arp.entries_total,arp.in_drops,arp.in_replies_pkts,arp.in_requests_pkts,arp.incomplete_total,arp.out_replies_pkts,arp.out_requests_pkts,arp.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (instance.pyats_alias,instance.os,instance.instance,instance.bgp_id,instance.protocol_state,instance.nexthop_trigger_delay_critical,instance.nexthop_trigger_delay_noncritical,instance.nexthop_trigger_enabled,instance.vrf,instance.router_id,instance.cluster_id,instance.confederation_id,instance.neighbor,instance.version,instance.hold_time,instance.keep_alive_interval,instance.local_as,instance.remote_as,instance.neighbor_counters_received_bytes_in_queue,instance.neighbor_counters_received_capability,instance.neighbor_counters_received_keepalives,instance.neighbor_counters_received_notifications,instance.neighbor_counters_received_opens,instance.neighbor_counters_received_route_refresh,instance.neighbor_counters_received_total,instance.neighbor_counters_received_total_bytes,instance.neighbor_counters_received_updates,instance.neighbor_counters_sent_bytes_in_queue,instance.neighbor_counters_sent_capability,instance.neighbor_counters_sent_keepalives,instance.neighbor_counters_sent_notifications,instance.neighbor_counters_sent_opens,instance.neighbor_counters_sent_route_refresh,instance.neighbor_counters_sent_total,instance.neighbor_counters_sent_total_bytes,instance.neighbor_counters_sent_updates,instance.last_reset,instance.reset_reason,instance.timestamp)
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
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (route.pyats_alias,route.os,route.instance,route.vrf,route.neighbor,route.advertised,route.routes,route.remote_as,route.timestamp)
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_bgp_routes_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_bgp_routes_mind_map.html' % pyats_alias)    

def learn_platform_mindmap(request, pyats_alias):
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn Platform\n","| Alias | Operating System | Chassis | Chassis Serial Number | Free Disk Space | Total Disk Space | Used Disk Space | Image | Installed Packages | Main Memory | RP Uptime | Router Type | Version | Timestamp |\n","| ----- | ---------------- | ------- | --------------------- | --------------- | ---------------- | --------------- | ----- | ------------------ | ----------- | --------- | ----------- | ------- | --------- |\n"]
    markdown.writelines(markdown_header_rows)
    markdown.close()
    markdown = open("markdown.md", "a")
    for item in platform_list:
        markdown_data = "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (item.pyats_alias,item.os,item.chassis,item.chassis_sn,item.disk_free_space,item.disk_total_space,item.disk_used_space,item.image,item.installed_packages,item.main_mem,item.rp_uptime,item.rtr_type,item.version,item.timestamp)
        markdown.write(markdown_data)
    markdown.close
    markdown = open('markdown.md', 'r')
    print(markdown.read()) 
    os.system('markmap --no-open markdown.md --output merlin/templates/Mindmap/%s_learn_platform_mind_map.html' % pyats_alias)
    markdown.close
    os.remove("markdown.md")
    return render(request, 'Mindmap/%s_learn_platform_mind_map.html' % pyats_alias)