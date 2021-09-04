from django.shortcuts import render
from .models import LearnVLAN, LearnVRF, ShowVersion
import os

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