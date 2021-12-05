import os
import time
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader
from merlin.models import Devices, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowIPIntBrief, ShowLicenseSummary, ShowVersion

template_dir = 'merlin/templates/Jinja2'
env = Environment(loader=FileSystemLoader(template_dir))

# VIEWS
def netgraph_page(request):
    device_list = Devices.objects.all()
    context = {'device_list': device_list}
    return render(request, 'Netgraph/netgraph.html', context) 

def eox_pid_netgraph(request):
    os.system('pyats run job eox_pid_job.py')
    latest_timestamp = EoX_PID.objects.latest('timestamp')
    eox_pid_list = EoX_PID.objects.filter(timestamp=latest_timestamp.timestamp)
    eox_pid_netjson_json_template = env.get_template('eox_netjson_json.j2')
    parsed_output_netjson_json = eox_pid_netjson_json_template.render(to_parse_eox=eox_pid_list)

    with open("merlin/templates/Netgraph/eox_pid_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/eox_pid_netgraph.html')

def eox_pid_json(request):
    return render(request, 'Netgraph/eox_pid_netgraph.json')

def eox_sn_netgraph(request):
    os.system('pyats run job eox_sn_job.py')
    latest_timestamp = EoX_SN.objects.latest('timestamp')
    eox_sn_list = EoX_SN.objects.filter(timestamp=latest_timestamp.timestamp)
    eox_sn_netjson_json_template = env.get_template('eox_netjson_json.j2')
    parsed_output_netjson_json = eox_sn_netjson_json_template.render(to_parse_eox=eox_sn_list)

    with open("merlin/templates/Netgraph/eox_sn_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/eox_sn_netgraph.html')

def eox_sn_json(request):
    return render(request, 'Netgraph/eox_sn_netgraph.json')

def eox_sw_netgraph(request):
    os.system('pyats run job eox_sw_job.py')
    latest_timestamp = EoX_IOS.objects.latest('timestamp')
    eox_sw_list = EoX_IOS.objects.filter(timestamp=latest_timestamp.timestamp)
    eox_sw_netjson_json_template = env.get_template('eox_netjson_json.j2')
    parsed_output_netjson_json = eox_sw_netjson_json_template.render(to_parse_eox=eox_sw_list)

    with open("merlin/templates/Netgraph/eox_sw_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/eox_sw_netgraph.html')

def eox_sw_json(request):
    return render(request, 'Netgraph/eox_sw_netgraph.json')    

def learn_acl_netgraph(request):
    os.system('pyats run job learn_acl_job.py')
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_acl_netjson_json_template = env.get_template('learned_acl_netjson_json.j2')
    parsed_output_netjson_json = learned_acl_netjson_json_template.render(to_parse_access_list=acl_list)

    with open("merlin/templates/Netgraph/learned_acl_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_acl_netgraph.html')

def learn_acl_json(request):
    return render(request, 'Netgraph/learned_acl_netgraph.json')

def learn_arp_netgraph(request):
    os.system('pyats run job learn_arp_job.py')
    latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_arp_netjson_json_template = env.get_template('learned_arp_netjson_json.j2')
    parsed_output_netjson_json = learned_arp_netjson_json_template.render(to_parse_arp_list=arp_list)

    with open("merlin/templates/Netgraph/learned_arp_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)

    return render(request, 'Netgraph/learned_arp_netgraph.html')

def learn_arp_json(request):
    return render(request, 'Netgraph/learned_arp_netgraph.json')

def learn_arp_statistics_netgraph(request):
    os.system('pyats run job learn_arp_job.py')
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_arp_statistics_netjson_json_template = env.get_template('learned_arp_statistics_netjson_json.j2')
    parsed_output_netjson_json = learned_arp_statistics_netjson_json_template.render(to_parse_arp_statistics_list=arp_statistics_list)

    with open("merlin/templates/Netgraph/learned_arp_statistics_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)

    return render(request, 'Netgraph/learned_arp_statistics_netgraph.html')

def learn_arp_statistics_json(request):
    return render(request, 'Netgraph/learned_arp_statistics_netgraph.json')

def learn_bgp_instances_netgraph(request):
    os.system('pyats run job learn_bgp_job.py')
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    bgp_instance_list = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_bgp_instances_netjson_json_template = env.get_template('learned_bgp_instances_netjson_json.j2')
    parsed_output_netjson_json = learned_bgp_instances_netjson_json_template.render(to_parse_bgp_instances=bgp_instance_list)

    with open("merlin/templates/Netgraph/learned_bgp_instances_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_bgp_instances_netgraph.html')

def learn_bgp_instances_json(request):
    return render(request, 'Netgraph/learned_bgp_instances_netgraph.json')

def learn_interface_netgraph(request):
    os.system('pyats run job learn_interface_job.py')
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_interface_netjson_json_template = env.get_template('learned_interface_netjson_json.j2')
    parsed_output_netjson_json = learned_interface_netjson_json_template.render(to_parse_interface=interface_list)

    with open("merlin/templates/Netgraph/learned_interface_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_interface_netgraph.html')

def learn_interface_json(request):
    return render(request, 'Netgraph/learned_interface_netgraph.json')

def learn_platform_netgraph(request):
    os.system('pyats run job learn_platform_job.py')
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_platform_netjson_json_template = env.get_template('learned_platform_netjson_json.j2')
    parsed_output_netjson_json = learned_platform_netjson_json_template.render(to_parse_platform=platform_list)

    with open("merlin/templates/Netgraph/learned_platform_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_platform_netgraph.html')

def learn_platform_json(request):
    return render(request, 'Netgraph/learned_platform_netgraph.json')

def learn_vlan_netgraph(request):
    os.system('pyats run job learn_vlan_job.py')
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlan_list = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_vlan_netjson_json_template = env.get_template('learned_vlan_netjson_json.j2')
    parsed_output_netjson_json = learned_vlan_netjson_json_template.render(to_parse_vlan=vlan_list)

    with open("merlin/templates/Netgraph/learned_vlan_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_vlan_netgraph.html')

def learn_vlan_json(request):
    return render(request, 'Netgraph/learned_vlan_netgraph.json')

def learn_vrf_netgraph(request):
    os.system('pyats run job learn_vrf_job.py')
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrf_list = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_vrf_netjson_json_template = env.get_template('learned_vrf_netjson_json.j2')
    parsed_output_netjson_json = learned_vrf_netjson_json_template.render(to_parse_vrf=vrf_list)

    with open("merlin/templates/Netgraph/learned_vrf_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/learned_vrf_netgraph.html')

def learn_vrf_json(request):
    return render(request, 'Netgraph/learned_vrf_netgraph.json')

def show_inventory_netgraph(request):
    os.system('pyats run job show_inventory_job.py')
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp)
    learned_inventory_netjson_json_template = env.get_template('show_inventory_netjson_json.j2')
    parsed_output_netjson_json = learned_inventory_netjson_json_template.render(to_parse_inventory=inventory_list)

    with open("merlin/templates/Netgraph/show_inventory_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/show_inventory_netgraph.html')

def show_inventory_json(request):
    return render(request, 'Netgraph/show_inventory_netgraph.json')

def show_ip_interface_brief_netgraph(request):
    os.system('pyats run job show_ip_int_brief_job.py')
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interface_list = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp)
    ip_int_brief_netjson_json_template = env.get_template('show_ip_interface_brief_netjson_json.j2')
    parsed_output_netjson_json = ip_int_brief_netjson_json_template.render(to_parse_interface=interface_list)

    with open("merlin/templates/Netgraph/show_ip_interface_brief_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/show_ip_interface_brief_netgraph.html')

def show_ip_interface_brief_json(request):
    return render(request, 'Netgraph/show_ip_interface_brief_netgraph.json')

def show_version_netgraph(request):
    os.system('pyats run job show_version_job.py')
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp)
    version_netjson_json_template = env.get_template('show_version_netjson_json.j2')
    parsed_output_netjson_json = version_netjson_json_template.render(to_parse_version=version_list)

    with open("merlin/templates/Netgraph/show_version_netgraph.json", "w") as fh:
        fh.write(parsed_output_netjson_json)    

    return render(request, 'Netgraph/show_version_netgraph.html')

def show_version_json(request):
    return render(request, 'Netgraph/show_version_netgraph.json')