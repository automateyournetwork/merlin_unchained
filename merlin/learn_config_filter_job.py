import os
import json
import sys
from pyats.topology import Testbed, Device
from genie.testbed import load
import django
django.setup()
from merlin.models import Devices, DynamicJobInput
from django.db.models import Q

def main(runtime):

    # Query the database for Filtered Devices
    search_input = DynamicJobInput.objects.latest('timestamp')
    device_list = Devices.objects.filter(Q(hostname=search_input.input_field) | Q(alias=search_input.input_field) | Q(device_type=search_input.input_field) | Q(os=search_input.input_field) | Q(username=search_input.input_field) | Q(ip_address=search_input.input_field) | Q(platform=search_input.input_field))

    # Flush Search
    delete_records = DynamicJobInput.objects.all()
    delete_records.delete()

    # Create Testbed
    testbed = Testbed('dynamicallyCreatedTestbed')

    # Create Devices
    for device in device_list:
        testbed_device = Device(device.hostname,
                    alias = device.alias,
                    type = device.device_type,
                    os = device.os,
                    credentials = {
                        'default': {
                            'username': device.username,
                            'password': device.password,
                        }
                    },
                    connections = {
                        'cli': {
                            'protocol': device.protocol,
                            'ip': device.ip_address,
                            'port': device.port,
                            'arguements': {
                                'connection_timeout': device.connection_timeout
                            }
                        }
                    })
        # define the relationship.
        testbed_device.testbed = testbed
   
    # ----------------
    # Load the testbed
    # ----------------
    if not runtime.testbed:
        # If no testbed is provided, load the default one.
        # Load default location of Testbed
        testbed = load(testbed)
    else:
        # Use the one provided
        testbed = runtime.testbed
    # Find the location of the script in relation to the job file
    testscript = os.path.join(os.path.dirname(__file__), 'learn_config.py')
    # run script
    runtime.tasks.run(testscript=testscript, testbed=testbed)