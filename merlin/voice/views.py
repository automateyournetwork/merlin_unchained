import os
import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from datetime import datetime
from merlin.models import DynamicJobInput

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
def config_voice_page(request):
    if request.method == "POST":
        voice_command = request.POST['send']
        input_field = DynamicJobInput(input_field=voice_command,timestamp=datetime.now().replace(microsecond=0))
        input_field.save()        
        os.system(f'pyats run job voice_config_job.py')
    else:
        message = "Please check the POST call"
    return render(request,"Voice/show_voice.html")    