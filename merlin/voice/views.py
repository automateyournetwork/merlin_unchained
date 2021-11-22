import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from merlin.models import DynamicJobInput, LearnInterface, InterfaceEnable

def voice_page(request):
    return render(request, 'Voice/voice.html')  

@csrf_exempt
def learn_voice_page(request):
    if request.method == "POST":
        voice_command = request.POST['send']
        os.system(f'pyats run job learn_{ voice_command }_job.py')
    else:
        message = "Please check the POST call"
    return render(request,"Voice/learn_voice.html")

@csrf_exempt
def show_voice_page(request):
    if request.method == "POST":
        voice_command = request.POST['send']
        os.system(f'pyats run job show_{ voice_command }_job.py')
    else:
        message = "Please check the POST call"
    return render(request,"Voice/show_voice.html")

@csrf_exempt
def config_voice_page(request, pyats_alias, interface):
    if request.method == "POST":
        voice_command = request.POST['send']
        interface_enable = InterfaceEnable(pyats_alias=pyats_alias,interface=interface.replace("_","/"))
        interface_enable.save()        
        input_field = DynamicJobInput(input_field=voice_command,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()      
        os.system(f'pyats run job voice_config_job.py')
    else:
        message = "Please check the POST call"
    # Learn Interface to JSON
    os.system('pyats run job learn_interface_job.py')        
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    parsed_interface = interface.replace("_","/")
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp,interface=parsed_interface)
    context = {'pyats_alias': pyats_alias, 'interface_list': interface_list, 'user_interface': interface}
    return render(request,"Voice/config_voice.html", context)   