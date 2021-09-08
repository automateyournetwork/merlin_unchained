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
from merlin.models import LearnVRF

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
            # Learn VRF to JSON
            self.learned_vrf = ParseLearnFunction.parse_learn(steps, device, "vrf")            
            if self.learned_vrf is not None:
                # Set Django Database values from pyATS JSON
                for vrf in self.learned_vrf['vrfs']:
                    learnVRF=LearnVRF(pyats_alias=device.alias,os=device.os,vrf=vrf,address_family_ipv4=self.learned_vrf['vrfs'][vrf]['address_family']['ipv4'],address_family_ipv6=self.learned_vrf['vrfs'][vrf]['address_family']['ipv6'],route_distinguisher=self.learned_vrf['vrfs'][vrf]['route_distinguisher'],timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                    learnVRF.save()