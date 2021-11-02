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