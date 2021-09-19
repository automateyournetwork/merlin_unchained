import os
from pyats.topology import Testbed, Device
from genie.testbed import load
from merlin.models import Devices

def main(runtime):

    # Query the database for All Devices
    device_list = Devices.objects.all()

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
        testscript = os.path.join(os.path.dirname(__file__), 'learn_bgp.py')

        # run script
        runtime.tasks.run(testscript=testscript, testbed=testbed)