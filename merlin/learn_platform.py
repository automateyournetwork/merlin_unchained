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
from general_functionalities import ParseDictFunction
from datetime import datetime
from merlin.models import LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual

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
            # Learn Platform to JSON
            self.learned_platform = ParseDictFunction.parse_learn(steps, device, "platform")
            if self.learned_platform is not None:
                for slot in self.learned_platform['slot']:
                    for part in self.learned_platform['slot'][slot]:
                        slot = slot
                        slot_name = self.learned_platform['slot'][slot][part]['name']
                        slot_sn = self.learned_platform['slot'][slot][part]['sn']
                        slot_state = self.learned_platform['slot'][slot][part]['state']
                        if 'redundancy_state' in self.learned_platform['slot'][slot][part]:
                            slot_redundancy_state = self.learned_platform['slot'][slot][part]['redundancy_state']
                        else:
                            slot_redundancy_state = 'null'

                        if 'rp_boot_image' in self.learned_platform['slot'][slot][part]:
                            rp_boot_image = self.learned_platform['slot'][slot][part]['rp_boot_image']
                        else:
                            rp_boot_image = 'null'

                        if 'rp_uptime' in self.learned_platform['slot'][slot][part]:
                            rp_uptime = self.learned_platform['slot'][slot][part]['rp_uptime']
                        else:
                            rp_uptime = 'null'

                    # Set Django Database values from pyATS JSON
                    learnPlatformSlots=LearnPlatformSlots(pyats_alias=device.alias,os=device.os,slot=slot,slot_name=slot_name,slot_sn=slot_sn,slot_state=slot_state,slot_redundancy_state=slot_redundancy_state,rp_boot_image=rp_boot_image,slot_rp_uptime=rp_uptime,timestamp=datetime.now().replace(microsecond=0))

                    # Save the objects into the database.
                    learnPlatformSlots.save()

                for virtual_device in self.learned_platform['virtual_device']:
                    virtual_device_name = self.learned_platform['virtual_device'][virtual_device]['vd_name']
                    virtual_device_status = self.learned_platform['virtual_device'][virtual_device]['vd_status']
                    for member in self.learned_platform['virtual_device'][virtual_device]['membership']:
                        virtual_device_member = member
                        virtual_device_member_status = self.learned_platform['virtual_device'][virtual_device]['membership'][member]['status']
                        virtual_device_member_type = self.learned_platform['virtual_device'][virtual_device]['membership'][member]['type']
                
                        # Set Django Database values from pyATS JSON
                        learnPlatformVirtual=LearnPlatformVirtual(pyats_alias=device.alias,os=device.os,virtual_device_name=virtual_device_name,virtual_device_status=virtual_device_status,virtual_device_member=member,virtual_device_member_status=virtual_device_member_status,virtual_device_member_type=virtual_device_member_type,timestamp=datetime.now().replace(microsecond=0))

                        # Save the objects into the database.
                        learnPlatformVirtual.save()

                # Set Django Database values from pyATS JSON
                learnPlatform=LearnPlatform(pyats_alias=device.alias,os=device.os,chassis=self.learned_platform['chassis'],chassis_sn=self.learned_platform['chassis_sn'],disk_free_space=self.learned_platform['disk_free_space'],disk_total_space=self.learned_platform['disk_total_space'],disk_used_space=self.learned_platform['disk_used_space'],image=self.learned_platform['image'],installed_packages=self.learned_platform['installed_packages'],main_mem=self.learned_platform['main_mem'],rp_uptime=self.learned_platform['rp_uptime'],rtr_type=self.learned_platform['rtr_type'],version=self.learned_platform['version'],timestamp=datetime.now().replace(microsecond=0))

                # Save the objects into the database.
                learnPlatform.save()