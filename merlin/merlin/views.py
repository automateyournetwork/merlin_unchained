from django.shortcuts import render
from django.http import HttpResponse
from .models import LearnVLAN, LearnVRF, ShowVersion
import os
import csv

# HTML VIEWS #
def learn_vlan_year_archive(request, year):
    v_list = LearnVLAN.objects.filter(timestamp__year=year)
    context = {'year': year, 'vlan_list': v_list}
    return render(request, 'LearnVLAN/learn_vlan_year_archive.html', context)

def learn_vlan_month_archive(request, year, month):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vlan_list': v_list}
    return render(request, 'LearnVLAN/learn_vlan_month_archive.html', context)

def learn_vlan_day_archive(request, year, month, day):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vlan_list': v_list}
    return render(request, 'LearnVLAN/learn_vlan_day_archive.html', context)

def learn_vlan_os_archive(request, os):
    v_list = LearnVLAN.objects.filter(os=os)
    context = {'os': os, 'vlan_list': v_list}
    return render(request, 'LearnVLAN/learn_vlan_os_archive.html', context)

def learn_vlan_alias_archive(request, os, pyats_alias):
    v_list = LearnVLAN.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'vlan_list': v_list}
    return render(request, 'LearnVLAN/learn_vlan_alias_archive.html', context)

def learn_vrf_year_archive(request, year):
    v_list = LearnVRF.objects.filter(timestamp__year=year)
    context = {'year': year, 'vrf_list': v_list}
    return render(request, 'LearnVRF/learn_vrf_year_archive.html', context)

def learn_vrf_month_archive(request, year, month):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vrf_list': v_list}
    return render(request, 'LearnVRF/learn_vrf_month_archive.html', context)

def learn_vrf_day_archive(request, year, month, day):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vrf_list': v_list}
    return render(request, 'LearnVRF/learn_vrf_day_archive.html', context)

def learn_vrf_os_archive(request, os):
    v_list = LearnVRF.objects.filter(os=os)
    context = {'os': os, 'vrf_list': v_list}
    return render(request, 'LearnVRF/learn_vrf_os_archive.html', context)

def learn_vrf_alias_archive(request, os, pyats_alias):
    v_list = LearnVRF.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'vrf_list': v_list}
    return render(request, 'LearnVRF/learn_vrf_alias_archive.html', context)    

def show_version_year_archive(request, year):
    v_list = ShowVersion.objects.filter(timestamp__year=year)
    context = {'year': year, 'version_list': v_list}
    return render(request, 'ShowVersion/show_version_year_archive.html', context)

def show_version_month_archive(request, year, month):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'version_list': v_list}
    return render(request, 'ShowVersion/show_version_month_archive.html', context)

def show_version_day_archive(request, year, month, day):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'version_list': v_list}
    return render(request, 'ShowVersion/show_version_day_archive.html', context)

def show_version_os_archive(request, os):
    v_list = ShowVersion.objects.filter(os=os)
    context = {'os': os, 'version_list': v_list}
    return render(request, 'ShowVersion/show_version_os_archive.html', context)

def show_version_alias_archive(request, os, pyats_alias):
    v_list = ShowVersion.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'version_list': v_list}
    return render(request, 'ShowVersion/show_version_alias_archive.html', context)

# CSV VIEWS
def csv_page(request):
    return render(request, 'CSV/csv.html')    

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
    response['Content-Disposition'] = 'attachment; filename="learn_vrf_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VRF','Address Family IPv4','Address Family IPv6','Route Distinguisher','Timestamp'])
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrfs = LearnVRF.objects.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')
    for vrf in vrfs:
        writer.writerow(vrf)
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
    response['Content-Disposition'] = 'attachment; filename="show_version_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Bootflash','Chassis','CPU','Device Name','Memory','Model','Processor Board ID','RP','Slots','Days Up','Hours Up','Minutes Up','Seconds Up','Name','OS','Last Reload Reason','System Compile Time','Image File','Version','Chassis Serial Number','Compiled By','Current Config Register','Image ID','Label','License Leven','License Type','Non Volative Memory','Physical Memory','Next Reload License Level','Platform','Processor Type','Return to ROM by','Router Type','Uptime','Uptime this CP','Version (Short)','XE Version','Timestamp'])
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    versions = ShowVersion.objects.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')
    for version in versions:
        writer.writerow(version)
    return response

# On DEMAND VIEWS

def button(request):
    return render(request, 'OnDemand/ondemand.html')

def get_all_ondemand(request):
    os.system('pyats run job populate_db_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/get_all_result.html')

def learn_vlan_ondemand(request):
    os.system('pyats run job learn_vlan_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_vlan_result.html')

def learn_vrf_ondemand(request):
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_vrf_result.html')

def show_version_ondemand(request):
    os.system('pyats run job show_version_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/show_version_result.html')

# Latest
def latest(request):
    return render(request, 'Latest/latest.html')

def all_latest(request):
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlan_list = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp)
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrf_list = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp) 
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp)       
    context = {'vlan_list': vlan_list,'vrf_list': vrf_list,'version_list': version_list}
    return render(request, 'Latest/All/all_latest.html', context)

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

def show_version_latest(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    v_list = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'version_list': v_list}
    return render(request, 'Latest/ShowVersion/show_version_latest.html', context)

# Changes 

def changes(request):
    return render(request, 'Changes/changes.html')

def all_changes(request):
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job populate_db_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    vlan_new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=vlan_new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=vrf_new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=version_new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")    
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)       
    return render(request, 'Changes/all_changes.html', {'vlan_removals': vlan_removals,'vlan_additions': vlan_additions, 'vrf_removals': vrf_removals,'vrf_additions': vrf_additions,'version_removals': version_removals,'version_additions': version_additions})

def learn_vlan_changes(request):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    os.system('pyats run job learn_vlan_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    return render(request, 'Changes/learn_vlan_changes.html', {'vlan_removals': vlan_removals,'vlan_additions': vlan_additions})

def learn_vrf_changes(request):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    return render(request, 'Changes/learn_vrf_changes.html', {'vrf_removals': vrf_removals,'vrf_additions': vrf_additions})

def show_version_changes(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)
    return render(request, 'Changes/show_version_changes.html', {'version_removals': version_removals,'version_additions': version_additions})