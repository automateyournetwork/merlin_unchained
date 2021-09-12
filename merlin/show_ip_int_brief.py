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
from general_functionalities import ParseShowCommandFunction
from datetime import datetime
from merlin.models import ShowIPIntBrief

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
        for device in testbed:
            # Show IP Int Brief to JSON
            self.parsed_show_ip_brief=ParseShowCommandFunction.parse_show_command(steps, device, "show ip interface brief")
            if self.parsed_show_ip_brief is not None:
                # Set Django Database values from pyATS JSON
                for interface in self.parsed_show_ip_brief['interface']:
                    if "Vlan" in interface:
                        for vlan in self.parsed_show_ip_brief['interface'][interface]['vlan_id']:
                            showIPIntBrief=ShowIPIntBrief(pyats_alias=device.alias,os=device.os,interface=interface,interface_status=self.parsed_show_ip_brief['interface'][interface]['vlan_id'][vlan]['interface_status'],ip_address=self.parsed_show_ip_brief['interface'][interface]['vlan_id'][vlan]['ip_address'],timestamp=datetime.now().replace(microsecond=0))
                    else:
                        showIPIntBrief=ShowIPIntBrief(pyats_alias=device.alias,os=device.os,interface=interface,interface_status=self.parsed_show_ip_brief['interface'][interface]['interface_status'],ip_address=self.parsed_show_ip_brief['interface'][interface]['ip_address'],timestamp=datetime.now().replace(microsecond=0))
                        # Save the objects into the database.
                        
                    showIPIntBrief.save()