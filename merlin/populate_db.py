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
from general_functionalities import ParseShowCommandFunction, ParseLearnFunction
from datetime import datetime
from merlin.models import LearnVLAN, LearnVRF, ShowVersion

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
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces=self.learned_vlan['vlans'][vlan]['interfaces'],mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now())
                        else:
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces="null",mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now())

                        learnVLAN.save()

            # Learn VRF to JSON
            self.learned_vrf = ParseLearnFunction.parse_learn(steps, device, "vrf")            
            if self.learned_vrf is not None:
                # Set Django Database values from pyATS JSON
                for vrf in self.learned_vrf['vrfs']:
                    learnVRF=LearnVRF(pyats_alias=device.alias,os=device.os,vrf=vrf,address_family_ipv4=self.learned_vrf['vrfs'][vrf]['address_family']['ipv4'],address_family_ipv6=self.learned_vrf['vrfs'][vrf]['address_family']['ipv6'],route_distinguisher=self.learned_vrf['vrfs'][vrf]['route_distinguisher'],timestamp=datetime.now())
                # Save the objects into the database.
                    learnVRF.save()

            # Show Version to JSON
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            if self.parsed_show_version is not None:
                # Set Django Database values from pyATS JSON
                if device.os == "nxos":
                    showVersion=ShowVersion(pyats_alias=device.alias,bootflash=self.parsed_show_version['platform']['hardware']['bootflash'],chassis=self.parsed_show_version['platform']['hardware']['chassis'],cpu=self.parsed_show_version['platform']['hardware']['cpu'],device_name=self.parsed_show_version['platform']['hardware']['device_name'],memory=self.parsed_show_version['platform']['hardware']['memory'],model=self.parsed_show_version['platform']['hardware']['model'],processor_board_id=self.parsed_show_version['platform']['hardware']['processor_board_id'],rp=self.parsed_show_version['platform']['hardware']['rp'],slots=self.parsed_show_version['platform']['hardware']['slots'],name=self.parsed_show_version['platform']['name'],os=device.os,reason=self.parsed_show_version['platform']['reason'],days=self.parsed_show_version['platform']['kernel_uptime']['days'],hours=self.parsed_show_version['platform']['kernel_uptime']['hours'],minutes=self.parsed_show_version['platform']['kernel_uptime']['minutes'],seconds=self.parsed_show_version['platform']['kernel_uptime']['seconds'],system_compile_time=self.parsed_show_version['platform']['software']['system_compile_time'],system_image_file=self.parsed_show_version['platform']['software']['system_image_file'],system_version=self.parsed_show_version['platform']['software']['system_version'],chassis_sn="null",compiled_by="null",curr_config_register="null",image_id="null",image_type="null",label="null",license_level="null",license_type="null",non_volatile="null",physical="null",next_reload_license_level="null",platform="null",processor_type="null",returned_to_rom_by="null",rom="null",rtr_type="null",uptime="null",uptime_this_cp="null",version_short="null",xe_version="null",timestamp=datetime.now())
                elif device.os == "iosxe":
                    showVersion=ShowVersion(pyats_alias=device.alias,bootflash=self.parsed_show_version['version']['system_image'],chassis=self.parsed_show_version['version']['chassis'],cpu="null",device_name=self.parsed_show_version['version']['hostname'],memory=self.parsed_show_version['version']['main_mem'],model=self.parsed_show_version['version']['platform'],processor_board_id="null",rp="null",slots="null",name="null",os=device.os,reason=self.parsed_show_version['version']['last_reload_reason'],days="null",hours="null",minutes="null",seconds="null",system_compile_time=self.parsed_show_version['version']['compiled_date'],system_image_file=self.parsed_show_version['version']['system_image'],system_version=self.parsed_show_version['version']['version'],chassis_sn=self.parsed_show_version['version']['chassis_sn'],compiled_by=self.parsed_show_version['version']['compiled_by'],curr_config_register=self.parsed_show_version['version']['curr_config_register'],image_id=self.parsed_show_version['version']['image_id'],image_type=self.parsed_show_version['version']['image_type'],label=self.parsed_show_version['version']['label'],license_level=self.parsed_show_version['version']['license_level'],license_type=self.parsed_show_version['version']['license_type'],non_volatile=self.parsed_show_version['version']['mem_size']['non-volatile configuration'],physical=self.parsed_show_version['version']['mem_size']['physical'],next_reload_license_level=self.parsed_show_version['version']['next_reload_license_level'],platform=self.parsed_show_version['version']['platform'],processor_type=self.parsed_show_version['version']['processor_type'],returned_to_rom_by=self.parsed_show_version['version']['returned_to_rom_by'],rom=self.parsed_show_version['version']['rom'],rtr_type=self.parsed_show_version['version']['rtr_type'],uptime=self.parsed_show_version['version']['uptime'],uptime_this_cp=self.parsed_show_version['version']['uptime_this_cp'],version_short=self.parsed_show_version['version']['version_short'],xe_version=self.parsed_show_version['version']['xe_version'],timestamp=datetime.now())
                # Save the objects into the database.
                showVersion.save()