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
from merlin.models import ShowVersion

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
            # Show Version to JSON
            self.parsed_show_version = ParseShowCommandFunction.parse_show_command(steps, device, "show version")

            if self.parsed_show_version is not None:
                # Set Django Database values from pyATS JSON
                showVersion = ShowVersion(bootflash=self.parsed_show_version['platform']['hardware']['bootflash'],chassis=self.parsed_show_version['platform']['hardware']['chassis'],cpu=self.parsed_show_version['platform']['hardware']['cpu'],device_name=self.parsed_show_version['platform']['hardware']['device_name'],memory=self.parsed_show_version['platform']['hardware']['memory'],model=self.parsed_show_version['platform']['hardware']['model'],processor_board_id=self.parsed_show_version['platform']['hardware']['processor_board_id'],rp=self.parsed_show_version['platform']['hardware']['rp'],slots=self.parsed_show_version['platform']['hardware']['slots'],name=self.parsed_show_version['platform']['name'],os=self.parsed_show_version['platform']['os'],reason=self.parsed_show_version['platform']['reason'],days=self.parsed_show_version['platform']['kernel_uptime']['days'],hours=self.parsed_show_version['platform']['kernel_uptime']['hours'],minutes=self.parsed_show_version['platform']['kernel_uptime']['minutes'],seconds=self.parsed_show_version['platform']['kernel_uptime']['seconds'],system_compile_time=self.parsed_show_version['platform']['software']['system_compile_time'],system_image_file=self.parsed_show_version['platform']['software']['system_image_file'],system_version=self.parsed_show_version['platform']['software']['system_version'],timestamp=datetime.now())

                # Save the objects into the database.
                showVersion.save()