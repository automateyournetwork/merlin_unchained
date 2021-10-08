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
from general_functionalities import ParseConfigFunction
from datetime import datetime
from merlin.models import LearnConfig

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
            # Learn Config to JSON
            self.learned_config = ParseConfigFunction.parse_learn(steps, device, "config")            
            if self.learned_config is not None:
                # Set Django Database values from pyATS JSON
                learnConfig=LearnConfig(pyats_alias=device.alias,os=device.os,config=self.learned_config,timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                learnConfig.save()