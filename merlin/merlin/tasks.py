import base64
import json
import os
import time
import threading
from django_blender.celery import app, get_blender
from channels import Channel
from django.conf import settings
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import LearnInterface, NumbersToCall, TwilioCredentials
from gtts import gTTS
from twilio.rest import Client

@shared_task(name = "Schedule All Tasks")
def run_all_tasks_job():
    os.system('pyats run job populate_db_job.py')

@shared_task(name = "End of Life - Part ID")
def run_all_tasks_job():
    os.system('pyats run job eox_pid_job.py')

@shared_task(name = "End of Life - Serial Number")
def run_all_tasks_job():
    os.system('pyats run job eox_sn_job.py')

@shared_task(name = "End of Life - Software")
def run_all_tasks_job():
    os.system('pyats run job eox_sw_job.py')

@shared_task(name = "Learn ACL")
def run_all_tasks_job():
    os.system('pyats run job learn_acl_job.py')

@shared_task(name = "Learn ARP")
def run_all_tasks_job():
    os.system('pyats run job learn_arp_job.py')

@shared_task(name = "Learn BGP")
def run_all_tasks_job():
    os.system('pyats run job learn_bgp_job.py')

@shared_task(name = "Learn Configuration")
def run_all_tasks_job():
    os.system('pyats run job learn_config_job.py')

@shared_task(name = "Learn Interface")
def run_all_tasks_job():
    os.system('pyats run job learn_interface_job.py')

@shared_task(name = "Learn Platform")
def run_all_tasks_job():
    os.system('pyats run job learn_platform_job.py')

@shared_task(name = "Learn VLAN")
def run_all_tasks_job():
    os.system('pyats run job learn_vlan_job.py')

@shared_task(name = "Learn VRF")
def run_all_tasks_job():
    os.system('pyats run job learn_vrf_job.py')

@shared_task(name = "PSIRT")
def run_all_tasks_job():
    os.system('pyats run job psirt_job.py')

@shared_task(name = "Recommended Release")
def run_all_tasks_job():
    os.system('pyats run job recommended_job.py')

@shared_task(name = "Serial 2 Contract")
def run_all_tasks_job():
    os.system('pyats run job serial2contract_job.py')

@shared_task(name = "Show Inventory")
def run_all_tasks_job():
    os.system('pyats run job show_inventory_job.py')

@shared_task(name = "Show License Summary")
def run_all_tasks_job():
    os.system('pyats run job show_license_summary_job.py')

@shared_task(name = "Show IP Interface Brief")
def run_all_tasks_job():
    os.system('pyats run job show_ip_int_brief_job.py')

@shared_task(name = "Show Version")
def run_all_tasks_job():
    os.system('pyats run job show_version_job.py')

@shared_task(name = "Call If Interfaces Get Disabled")
def run_all_tasks_job():
    # Learn Interface to JSON
    os.system('pyats run job learn_interface_job.py')
    latest_timestamp = LearnInterface.objects.latest('timestamp')
    interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp,enabled="False")
    shut_interfaces = []
    for interface in interface_list:
        if interface.interface != "Vlan1":
            down_int = interface.interface
            description = interface.description
            device_alias = interface.pyats_alias
            shut_interfaces.append(down_int)
            shut_interfaces.append(description)
    if shut_interfaces != "[]":
        # Generate Message in Text
        text = f"Hello! At { latest_timestamp.timestamp }, on device { interface.pyats_alias }, Merlin has detected the following interfaces are disabled { shut_interfaces }"
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

@shared_task(name = "Text If Interfaces Get Disabled")
def run_all_tasks_job():
            os.system('pyats run job learn_interface_job.py')
            latest_timestamp = LearnInterface.objects.latest('timestamp')
            interface_list = LearnInterface.objects.filter(timestamp=latest_timestamp.timestamp,enabled="False")
            # Get Twilio stuff
            tw_db_sid = TwilioCredentials.objects.all().values('sid')
            tw_db_token = TwilioCredentials.objects.all().values('token')
            tw_db_from = TwilioCredentials.objects.all().values('from_number_sms')
            tw_db_to_call = NumbersToCall.objects.all().values('number_to_call')
            account_sid = tw_db_sid[0]['sid']
            auth_token = tw_db_token[0]['token']
            from_number = tw_db_from[0]['from_number_sms']
            client = Client(account_sid, auth_token)
            for interface in interface_list:
                if interface.interface != "Vlan1":
                    for number in tw_db_to_call:               
                        message = client.messages.create(
                            body=f"Hello! At { latest_timestamp.timestamp }, on device { pyats_alias }, Merlin has detected the following interface is now disabled { interface.interface } { interface.description }. Please visit http://localhost:8000/Latest/LearnPlatform/ for details",
                            from_=f"+1{ from_number }",
                            to=f"+1{ number['number_to_call'] }"
                            )

@app.task(bind=True, track_started=True)
def render(task, data, reply_channel):
    bpy = get_blender()
    setup_scene(bpy, data)

    context = {'rendering': True, 'filepath': os.path.join(settings.BLENDER_RENDER_TMP_DIR, task.request.id)}
    sync_thread = threading.Thread(target=sync_render, args=(bpy, context, reply_channel))
    sync_thread.start()
    bpy.ops.render.render()
    context['rendering'] = False
    sync_thread.join()

    if os.path.exists(context['filepath']):
        os.remove(context['filepath'])

    if reply_channel is not None:
        Channel(reply_channel).send({
            'text': json.dumps({
                'action': 'render_finished'
            })
        })


def setup_scene(bpy, data):
    try:
        levels = int(data['subsurf'])
    except ValueError:
        levels = 0
    bpy.context.object.modifiers[0].render_levels = levels


def sync_render(bpy, context, reply_channel):
    while context['rendering']:
        time.sleep(settings.BLENDER_RENDER_SYNC_INTERVAL)

        image = bpy.data.images['Render Result']
        image.save_render(filepath=context['filepath'])

        with open(context['filepath'], "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        if reply_channel is not None:
            Channel(reply_channel).send({
                'text': json.dumps({
                    'action': 'sync_render',
                    'image': encoded_string.decode()
                })
            })                            