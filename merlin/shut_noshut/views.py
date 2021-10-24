import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnInterface, InterfaceEnable
    
def shut_noshut(request, pyats_alias):
    if request.method == "POST":
        desired_state = request.POST.dict()
        interface_to_enable = desired_state.get("enable")
        interface_to_disable = desired_state.get("disable")
        
        if interface_to_enable:
            # Enable interface
            interface_enable=InterfaceEnable(pyats_alias=pyats_alias,interface=interface_to_enable)
            interface_enable.save()
            os.system('pyats run job no_shut_interface_job.py')
            delete_records = InterfaceEnable.objects.all()
            delete_records.delete()

        if interface_to_disable:
            # Disable interface
            interface_to_disable=InterfaceEnable(pyats_alias=pyats_alias,interface=interface_to_disable)
            interface_to_disable.save()            
            os.system('pyats run job shut_interface_job.py')
            delete_records = InterfaceEnable.objects.all()
            delete_records.delete()
    
    # Learn Interface to JSON
    os.system('pyats run job learn_interface_job.py')        
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'pyats_alias': pyats_alias, 'interface_list': interface_list}
    return render(request,"Shut_NoShut/shut_noshut.html", context)
