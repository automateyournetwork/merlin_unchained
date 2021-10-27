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
    markdown_header_rows = ["# Latest End of Life - Product ID\n","| Alias | Operating System | Part ID | Description | Bulletin Number | Bulletin URL | Published Date | End of Sale | End of Software Maintenance | End of Security | End of Routine Failure | End of Service Contract Renewal | Last Date of Support | End of SVC Attachment | Last Updated | Part ID Active | Migration Information | Migration Option | Migration Product ID | Migration Product Name | Migration Strategy | Migration Product Info URL | Timestamp | \n","| ----- | ---------------- | ------- | ----------- | --------------- | ------------ | -------------- | ----------- | --------------------------- | --------------- | ---------------------- | ------------------------------- | -------------------- | --------------------- | ------------ | -------------- | --------------------- | ---------------- | -------------------- | ---------------------- | ------------------ | -------------------------- | --------- |\n"]
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

def learn_platform_mindmap(request, pyats_alias):
    latest_timestamp = LearnPlatform.objects.latest('timestamp')
    platform_list = LearnPlatform.objects.filter(timestamp=latest_timestamp.timestamp)
    markdown = open("markdown.md", "w")
    markdown_header_rows = ["# Latest Learn Platform\n","| Alias | Operating System | Chassis | Chassis Serial Number | Free Disk Space | Total Disk Space | Used Disk Space | Image | Installed Packages | Main Memory | RP Uptime | Router Type | Version | Timestamp | \n","| ----- | ---------------- | ------- | --------------------- | --------------- | ---------------- | --------------- | ----- | ------------------ | ----------- | --------- | ----------- | ------- | --------- |\n"]
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