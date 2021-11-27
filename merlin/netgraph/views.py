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