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
from merlin.models import LearnARP, LearnARPStatistics

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
            # Learn ARP to JSON
            self.learned_arp = ParseLearnFunction.parse_learn(steps, device, "arp")
            if self.learned_arp is not None:
                # Set Django Database values from pyATS JSON
                for interface in self.learned_arp['interfaces']:
                    if 'ipv4' in self.learned_arp['interfaces']:
                        for neighbor in self.learned_arp['interfaces'][interface]['ipv4']['neighbors']:
                            learnARP=LearnARP(pyats_alias=device.alias,os=device.os,interface=interface,neighbor_ip=neighbor,neighbor_mac=self.learned_arp['interfaces'][interface]['ipv4']['neighbors'][neighbor]['link_layer_address'],origin=self.learned_arp['interfaces'][interface]['ipv4']['neighbors'][neighbor]['origin'],local_proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['local_proxy_enable'],proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['proxy_enable'],timestamp=datetime.now().replace(microsecond=0))
                    else:
                            learnARP=LearnARP(pyats_alias=device.alias,os=device.os,interface=interface,neighbor_ip="null",neighbor_mac="null",origin="null",local_proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['local_proxy_enable'],proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['proxy_enable'],timestamp=datetime.now().replace(microsecond=0))
                    learnARP.save()
                
                learnARPStatistics = LearnARPStatistics(pyats_alias=device.alias,os=device.os,entries_total=self.learned_arp['statistics']['entries_total'],in_drops=self.learned_arp['statistics']['in_drops'],in_replies_pkts=self.learned_arp['statistics']['in_replies_pkts'],in_requests_pkts=self.learned_arp['statistics']['in_requests_pkts'],incomplete_total=self.learned_arp['statistics']['incomplete_total'],out_replies_pkts=self.learned_arp['statistics']['out_replies_pkts'],out_requests_pkts=self.learned_arp['statistics']['out_requests_pkts'],timestamp=datetime.now().replace(microsecond=0))
                learnARPStatistics.save()