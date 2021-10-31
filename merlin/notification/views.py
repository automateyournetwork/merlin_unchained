import os
from django.shortcuts import render
from django.http import HttpResponse
from merlin.models import Devices, LearnInterface, TwilioCredentials, NumbersToCall
from gtts import gTTS
from twilio.rest import Client


def device_list(request):
    device_list = Devices.objects.all()
    context = {'device_list': device_list}
    return render(request, 'Notification/device_list.html', context)    

def device_notifications(request, pyats_alias):
    if request.method == "POST":
        button_pressed = request.POST.dict()
        disabled_interfaces_voice = button_pressed.get("disable_interface_voice")
        disabled_interfaces_sms = button_pressed.get("disable_interface_sms")

        if disabled_interfaces_voice:
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
                # Move file into static folder
                os.system("mv disabled_interfaces.mp3 merlin/static/notification/")                
                # Get Twilio stuff
                tw_db_sid = TwilioCredentials.objects.all().values('sid')
                tw_db_token = TwilioCredentials.objects.all().values('token')
                tw_db_from = TwilioCredentials.objects.all().values('from_number')
                tw_db_to_call = NumbersToCall.objects.all().values('number_to_call')
                account_sid = tw_db_sid[0]['sid']
                auth_token = tw_db_token[0]['token']
                from_number = tw_db_from[0]['from_number']
                client = Client(account_sid, auth_token)
                # Make calls
                for number in tw_db_to_call:
                    call = client.calls.create(
                        url="https://www.automateyournetwork.ca/wp-content/uploads/2021/10/disabled_interfaces.mp3",
                        to=number['number_to_call'],
                        from_=from_number
                )
            context = {'pyats_alias': pyats_alias}
            return render(request,"Notification/device_notifications.html", context)

        if disabled_interfaces_sms:
            # Learn Interface to JSON
            os.system('pyats run job learn_interface_job.py')
            latest_timestamp = LearnInterface.objects.latest('timestamp')
            interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp,enabled="False")
            # Get Twilio stuff
            tw_db_sid = TwilioCredentials.objects.all().values('sid')
            tw_db_token = TwilioCredentials.objects.all().values('token')
            tw_db_from = TwilioSMS.objects.all().values('from_number')
            tw_db_to_text = TwilioSMS.objects.all().values('number_to_text')
            account_sid = tw_db_sid[0]['sid']
            auth_token = tw_db_token[0]['token']
            from_number = tw_db_from[0]['from_number']
            client = Client(account_sid, auth_token)
            for interface in interface_list:
                if interface.interface != "Vlan1":
                    for number in tw_db_to_text:               
                        message = client.messages.create(
                            body=f"Hello! At { latest_timestamp.timestamp }, on device { pyats_alias }, Merlin has detected the following interface is now disabled { interface.interface } { interface.description }",
                            from_=from_number,
                            to=number['number_to_text']
                            )                

            context = {'pyats_alias': pyats_alias}
            return render(request,"Notification/device_notifications.html", context)
    else:
        context = {'pyats_alias': pyats_alias}
        return render(request,"Notification/device_notifications.html", context)