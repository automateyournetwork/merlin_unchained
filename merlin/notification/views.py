import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnInterface, TwilioCredentials, NumbersToCall, DropBoxCredentials
from gtts import gTTS
from twilio.rest import Client
import dropbox

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
                # Generate Message in Text
                text = f"Hello! At { latest_timestamp.timestamp }, on device { pyats_alias }, Merlin has detected the following interfaces are disabled { shut_interfaces }"
                # Convert to MP3
                mp3 = gTTS(text = text, lang='en-us')
                # Save MP3
                mp3.save('disabled_interfaces.mp3')
                # Dropbox 
                db_db_token = DropBoxCredentials.objects.all().values('token')
                account_token = db_db_token[0]['token']
                d = dropbox.Dropbox(account_token)
                # open the file and upload it
                with filepath.open("disabled_interfaces.mp3", "rb") as f:
                    meta = d.files_upload(f.read(), "disabled_interfaces.mp3", mode=dropbox.files.WriteMode("overwrite"))
                # Get link to file
                link = d.sharing_create_shared_link("disabled_interfaces.mp3")
                url = link.url                
                os.system("mv disabled_interfaces.mp3 merlin/static/notification/")                                  
                tw_db_token = TwilioCredentials.objects.all().values('token')
                tw_db_from = TwilioCredentials.objects.all().values('from_number')
                tw_db_to_call = NumbersToCall.objects.all().values('number_to_call')
                account_sid = tw_db_sid[0]['sid']
                auth_token = tw_db_token[0]['token']
                from_number = tw_db_from[0]['from_number']
                client = Client(account_sid, auth_token)     
                for number in db_to_call:
                    call = client.calls.create(
                        url=url,
                        to=number,
                        from_=from_number
                    )

            context = {'pyats_alias': pyats_alias}
            return render(request,"Notification/device_notifications.html", context)
    else:
        context = {'pyats_alias': pyats_alias}
        return render(request,"Notification/device_notifications.html", context)