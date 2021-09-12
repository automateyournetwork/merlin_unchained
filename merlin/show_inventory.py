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
from merlin.models import ShowInventory

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
            # Show Inventory to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            if self.parsed_show_inventory is not None:
                for part in self.parsed_show_inventory['name']:
                    # Set Django Database values from pyATS JSON
                    showInventory=ShowInventory(pyats_alias=device.alias,os=device.os,part=part,description=self.parsed_show_inventory['name'][part]['description'],pid=self.parsed_show_inventory['name'][part]['pid'],serial_number=self.parsed_show_inventory['name'][part]['serial_number'],timestamp=datetime.now().replace(microsecond=0))
                    # Save the objects into the database.
                    showInventory.save()