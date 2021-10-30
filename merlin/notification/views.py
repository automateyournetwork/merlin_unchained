import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnInterface, TwilioCredentials, NumbersToCall
from gtts import gTTS
from twilio.rest import Client


db_sid = TwilioCredentials.objects.all().values('sid')
db_token = TwilioCredentials.objects.all().values('token')
db_from = TwilioCredentials.objects.all().values('from_number')
db_to_call = NumbersToCall.objects.all().values('to')
account_sid = db_sid[0]['sid']
auth_token = db_token[0]['token']
from_number = db_from[0]['from']
client = Client(account_sid, auth_token)

def device_list(request):
    device_list = Devices.objects.all()
    context = {'device_list': device_list}
    return render(request, 'Notification/device_list.html', context)    

def device_notifications(request, pyats_alias):
    if request.method == "POST":
        button_pressed = request.POST.dict()
        disabled_interfaces = button_pressed.get("disable_interface")

        if disabled_interfaces:
            # Learn Interface to JSON
            os.system('pyats run job learn_interface_job.py')
            latest_timestamp = LearnInterface.objects.latest('timestamp')
            interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp,enabled="False")
            shut_interfaces = []
            for interface in interface_list:
                if interface.interface != "Vlan1":
                    down_int = interface.interface
                    description = interface.description
                    shut_interfaces.append(down_int)
                    shut_interfaces.append(description)
            if shut_interfaces != "[]":
                text = f"Hello! At { latest_timestamp.timestamp }, on device { pyats_alias }, Merlin has detected the following interfaces are disabled { shut_interfaces }"
                mp3 = gTTS(text = text, lang='en-us')
                mp3.save('disabled_interfaces.mp3')
                os.system("mv disabled_interfaces.mp3 merlin/static/notification/")
                for number in db_to_call:
                    call = client.calls.create(
                        url='merlin/static/notification/disabled_interfaces.mp3',
                        to=number,
                        from_=from_number.phone.as_e164
                    )

            context = {'pyats_alias': pyats_alias}
            return render(request,"Notification/device_notifications.html", context)
    else:
        context = {'pyats_alias': pyats_alias}
        return render(request,"Notification/device_notifications.html", context)