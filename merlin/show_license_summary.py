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
from merlin.models import ShowLicenseSummary

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
            if device.os == "iosxe":
                # Show Version to JSON
                self.parsed_show_license_summary=ParseShowCommandFunction.parse_show_command(steps, device, "show license summary")
                if self.parsed_show_license_summary is not None:
                    print(self.parsed_show_license_summary)
                    # Set Django Database values from pyATS JSON
                    # showLicenseSummary=ShowLicenseSummary(pyats_alias=device.alias, os=device.os, license_name= ,entitlement= ,count= ,status= ,timestamp=datetime.now().replace(microsecond=0))
                    # # Save the objects into the database.
                    # showLicenseSummary.save()

                    # {'license_usage': {'network-advantage': {'entitlement': 'C9300-48 Network Advan...', 'count': '1', 'status': 'IN USE'}, 'dna-advantage': {'entitlement': 'C9300-48 DNA Advantage', 'count': '1', 'status': 'IN USE'}}}