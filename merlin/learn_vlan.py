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
from merlin.models import LearnVLAN

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
            # Learn VLAN to JSON
            self.learned_vlan = ParseLearnFunction.parse_learn(steps, device, "vlan")
            if self.learned_vlan is not None:
                # Set Django Database values from pyATS JSON
                for vlan in self.learned_vlan['vlans']:
                    if vlan != "configuration" and vlan !="interface_vlan_enabled" and vlan !="vn_segment_vlan_based_enabled":
                        if 'interfaces' in self.learned_vlan['vlans'][vlan]:                           
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces=self.learned_vlan['vlans'][vlan]['interfaces'],mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        else:
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces="null",mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                        learnVLAN.save()