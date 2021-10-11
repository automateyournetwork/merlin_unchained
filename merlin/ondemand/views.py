import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from merlin.models import Devices, DynamicJobInput

# On DEMAND VIEWS - BUTTONS
def button(request):
    return render(request, 'OnDemand/ondemand.html')

def get_all_all_ondemand(request):
    os.system('pyats run job populate_db_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def eox_pid_all_ondemand(request):
    os.system('pyats run job eox_pid_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_acl_all_ondemand(request):
    os.system('pyats run job learn_acl_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_arp_all_ondemand(request):
    os.system('pyats run job learn_arp_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_bgp_all_ondemand(request):
    os.system('pyats run job learn_bgp_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_config_all_ondemand(request):
    os.system('pyats run job learn_config_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_interface_all_ondemand(request):
    os.system('pyats run job learn_interface_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_platform_all_ondemand(request):
    os.system('pyats run job learn_platform_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_vlan_all_ondemand(request):
    os.system('pyats run job learn_vlan_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_vrf_all_ondemand(request):
    os.system('pyats run job learn_vrf_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def nmap_all_ondemand(request):
    os.system('python3 port_scanner_all.py')
    return render(request, 'OnDemand/ondemand_result.html')

def psirt_all_ondemand(request):
    os.system('pyats run job psirt_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def recommended_all_ondemand(request):
    os.system('pyats run job recommended_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def serial2contract_all_ondemand(request):
    os.system('pyats run job serial2contract_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_inventory_all_ondemand(request):
    os.system('pyats run job show_inventory_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_ip_int_brief_all_ondemand(request):
    os.system('pyats run job show_ip_int_brief_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_version_all_ondemand(request):
    os.system('pyats run job show_version_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

# ON DEMAND VIEWS - FILTERS / USER INPUT

class OnDemandResultAll(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('get_all_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job populate_db_filter_job.py')

class OnDemandResultEoPID(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('eox_pid_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job eox_pid_filter_job.py')

class OnDemandResultACL(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_acl_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_acl_filter_job.py')

class OnDemandResultARP(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_arp_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_arp_filter_job.py')

class OnDemandResultBGP(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_bgp_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_bgp_filter_job.py')

class OnDemandResultConfig(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_config_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_config_filter_job.py')

class OnDemandResultInterface(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_interface_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_interface_filter_job.py')

class OnDemandResultPlatform(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_platform_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_platform_filter_job.py')

class OnDemandResultVLAN(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_vlan_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_vlan_filter_job.py')

class OnDemandResultVRF(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('learn_vrf_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job learn_vrf_filter_job.py')

class OnDemandResultNMAP(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('nmap_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('python3 port_scanner_filter.py')

class OnDemandResultPSIRT(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('psirt_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job psirt_filter_job.py')

class OnDemandResultRecommended(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('recommended_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job recommended_filter_job.py')

class OnDemandResultSerial2Contract(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('serial2contract_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job serial2contract_filter_job.py')

class OnDemandResultInventory(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('show_inventory_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_inventory_filter_job.py')

class OnDemandResultIPInterfaceBrief(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('show_ip_int_brief_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_ip_int_brief_filter_job.py')

class OnDemandResultVersion(ListView):
    template_name = 'OnDemand/ondemand.html'

    def get_queryset(self):
        query = self.request.GET.get('show_version_filter')
        input_field = DynamicJobInput(input_field=query,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()
        os.system('pyats run job show_version_filter_job.py')        