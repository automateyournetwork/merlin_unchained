# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import yaml
import time
import json
import shutil
import logging
import requests
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from general_functionalities import ParseLearnFunction
from datetime import datetime
from merlin.models import LearnInterface, InterfaceEnable
from jinja2 import Environment, FileSystemLoader

template_dir = 'merlin/templates/Jinja2'
env = Environment(loader=FileSystemLoader(template_dir))
device_with_interface_key = InterfaceEnable.objects.all().values('pyats_alias')
device_with_interface = device_with_interface_key[0]['pyats_alias']
interface_to_shut_key = InterfaceEnable.objects.all().values('interface')
interface_to_shut = interface_to_shut_key[0]['interface']
shut_template = env.get_template('shut.j2')

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect(learn_hostname=True)

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed.devices.values():
            if device.alias in device_with_interface:
                # Shut the Interface
                templated_interface = shut_template.render(interface=interface_to_shut)
                with steps.start("Shut the Interface", continue_=True) as step:
                    try:
                        device.configure(templated_interface)
                    except Exception as e:
                        step.failed('Could not shut the interface correctly\n{e}'.format(e=e))