import os
import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def voice_page(request):
    if request.method == "POST":
        voice_command = request.POST['send']
        os.system(f'pyats run job learn_{ voice_command }_job.py')
    else:
        message = "Please check the POST call"
    return render(request,"Voice/voice.html")